import pymongo
import Scrapers.mangaNelo as mangaNelo
from Scrapers.MALscraper.malScraper import malScraper



def UpdateManga() :
    print("UPDATE MANGA TABLE")
    myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
    mydb = myclient["MangaNoKuni"]
    mycol_manga = mydb["Manga"]

    # ajouter les champs supplémentaires
    mycol_manga.update_many({}, {"$set": {
        "title": "",
        "title_japanese": "",
        "synopsys": "",
        "image_url": "",
        "score": "",
        "genre": [],
        "authors": ""
    }})

    # ajouter les données de Jikan
    for manga in mycol_manga.find():
        data = malScraper().manga(int(manga["mal_id"]))

        try:
            mycol_manga.update_one({"_id": manga["_id"]},
                                   {
                                       "$set": {
                                           "title": data["title"],
                                           "title_japanese": data["title_japanese"],
                                           "synopsys": data["synopsys"],
                                           "image_url": data["image_url"],
                                           "score": data['score'],
                                           "genre": data['genres'],
                                           "authors": data['authors']
                                       }})
            print(data)
        except Exception as e:
            print(e)


def UpdateChapters():
    print("UPDATE CHAPTER TABLE")

    myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
    mydb = myclient["MangaNoKuni"]
    mycol_manga = mydb["Manga"]
    mycol_chapitre = mydb["Chapitre"]

    # récupérer les données et les stocker dans mongodb
    for manga in mycol_manga.find():
        # scrap de manga.Url pour récupérer les objets Chapitres
        print(manga)
        chapters_data = None

        if manga['from'] == "manganelo" :
            chapters_data = mangaNelo.extract_chapters(manga)

            for data in chapters_data :
                # il y a un problème
                if mycol_chapitre.count_documents({'mal_id': data['mal_id'], 'num_chapitre': data['num_chapitre']}) > 1:
                    raise Exception("duplicate chapters in database mal_id : {}  chapter : {}".format(data['mal_id'], data['num_chapitre']))


                # nouveau chapitre => on créé un nouveau document
                if mycol_chapitre.count_documents({'mal_id' : data['mal_id'], 'num_chapitre': data['num_chapitre']}) == 0:
                    try:
                        #print("insertion new chapter mal_id : {}".format(data['mal_id']))
                        mycol_chapitre.insert_one(data)
                    except Exception as e:
                        print("insertion chapter failed in mongo mal_id : {}".format(data['mal_id']))
                        print(e)

                # update le document existant
                if mycol_chapitre.count_documents({'mal_id': data['mal_id'], 'num_chapitre': data['num_chapitre']}) == 1:
                    mycol_chapitre.update_one({'mal_id': data['mal_id'], 'num_chapitre': data['num_chapitre']},
                                               { "$set":
                                                     { "url": data['mal_id'],
                                                       'images_html' : data['images_html']
                                                       }
                                                 })