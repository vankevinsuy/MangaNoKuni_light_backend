import pymongo
import Scrapers.mangaNelo as mangaNelo

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
            if mycol_chapitre.count_documents({"Mal_id": dico["Mal_id"],"num_chapitre": dico["num_chapitre"]}) == 0:
                data_to_insert.append(dico)

        try:
            print("insertion MAL_ID : {}".format(manga['Mal_id']))
            mycol_chapitre.insert_one(data_to_insert)
        except:
            print("insertion failed MAL_ID : {}".format(manga['Mal_id']))