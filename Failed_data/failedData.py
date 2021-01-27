import pymongo

myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@192.168.1.22:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["MangaNoKuni_dev"]
mycol_failed_anime = mydb["Failed_anime"]
mycol_failed_manga = mydb["Failed_manga"]

def add_failed_anime_in_base(dic):
    mycol_failed_anime.insert_one(dic)

def add_failed_manga_in_base(dic):
    mycol_failed_manga.insert_one(dic)