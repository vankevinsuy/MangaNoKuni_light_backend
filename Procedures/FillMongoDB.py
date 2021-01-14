import pymongo
import Scrapers.mangaNelo as mangaNelo
import Scrapers.mangallama as mangallama
from Scrapers.MALscraper.malScraper import malScraper

myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@192.168.1.22:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["MangaNoKuni_dev"]
mycol_manga = mydb["Manga"]
mycol_chapitre = mydb["Chapitre"]


def UpdateManga() :
    print("UPDATE MANGA TABLE")

    # ajouter les champs supplémentaires
    mycol_manga.update_many({}, {"$set": {
        "title": "",
        "title_japanese": "",
        "synopsys": "",
        "image_url": "",
        "score": "",
        "genre": [],
        "authors": "",
        "title_search": ""
    }})

    # ajouter les données de Jikan
    for manga in mycol_manga.find():
        data = malScraper().manga(int(manga["mal_id"]))

        title_search = str(data["title"]).upper().replace(" ", "")
        title_search =  ''.join(x for x in title_search if x.isalpha())

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
                                           "authors": data['authors'],
                                           "title_search": title_search
                                       }})
            print(data)
        except Exception as e:
            print(e)


def UpdateChapters():
    print("UPDATE CHAPTER TABLE")

    # récupérer les données et les stocker dans mongodb
    for manga in mycol_manga.find():
        # scrap de manga.Url pour récupérer les objets Chapitres
        print(manga)
        chapters_data = []

        for source in manga['url']:
            if source['from'] == "manganelo" :
                for data in mangaNelo.extract_chapters(manga, source['url']):
                    if data['num_chapitre'] not in [x["num_chapitre"] for x in chapters_data]:
                        chapters_data.append(data)

            if source['from'] == "mangallama" :
                for data in mangallama.extract_chapters(manga, source['url']):
                    if data['num_chapitre'] not in [x["num_chapitre"] for x in chapters_data]:
                        chapters_data.append(data)

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
                                                 { "url": data['url'],
                                                   'images_html' : data['images_html']
                                                   }
                                             })