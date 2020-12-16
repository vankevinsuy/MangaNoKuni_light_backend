import pymongo
import Scrapers.mangaNelo as mangaNelo
from jikanpy import Jikan
jikan = Jikan()

def Launch():
    myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
    mydb = myclient["MangaNoKuni"]
    mycol_manga = mydb["Manga"]
    mycol_chapitre = mydb["Chapitre"]

    # récupérer les données et les stocker dans mongodb
    for manga in mycol_manga.find():
        # scrap de manga.Url pour récupérer les objets Chapitres
        print(manga)
        data = None

        if manga['from'] == "manganelo" :
            data = mangaNelo.extract_chapters(manga)

        # vérifier que les données ne sont pas déjà dans la BDD
        data_to_insert = []
        for dico in data :
            if mycol_chapitre.count_documents({"mal_id": dico["mal_id"],"num_chapitre": dico["num_chapitre"]}) == 0:
                data_to_insert.append(dico)

        try:
            print("insertion mal_id : {}".format(manga['mal_id']))
            mycol_chapitre.insert_many(data_to_insert)
        except Exception as e:
            print("insertion failed in mongo mal_id : {}".format(manga['mal_id']))
            print(e)

    # ajouter les champs supplémentaires
    mycol_manga.update_many({}, { "$set": {
        "title": "",
        "title_japanese" : "",
        "synopsys" : "",
        "image_url" : "",
        "score" : "",
         "genre" : [],
        "authors" : []
    } })

    # ajouter les données de Jikan
    for manga in mycol_manga.find():

        data = jikan.manga(int(manga["mal_id"]))

        try :
            mycol_manga.update_one({"_id" : manga["_id"]},
               {
                "$set" : {
                    "title": data["title"],
                    "title_japanese" : data["title_japanese"],
                    "synopsys" : data["synopsis"],
                    "image_url" : data["image_url"],
                    "score" : str(data['score']),
                    "genre" : [x['name'] for x in data['genres']],
                    "authors": [x['name'] for x in data['authors']]
                }})
        except Exception as e:
            print(manga)
            print(e)