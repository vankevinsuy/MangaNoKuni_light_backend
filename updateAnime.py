import pymongo

from Fillers import FillMongoDB

myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@192.168.1.22:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["MangaNoKuni_dev"]
mycol_failed = mydb["Failed_anime"]
mycol_failed.drop()

FillMongoDB.UpdateAnime()

FillMongoDB.UpdateEpisodes()

