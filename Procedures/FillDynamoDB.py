import pymongo
import boto3
import datetime
from decimal import Decimal
import json
import time

# insérer les données dans Dynamodb depuis MongoDB
dynamodb = boto3.resource('dynamodb')
TIME = datetime.datetime.now()
tableManga = dynamodb.Table('Manga-7zccm6vrw5dhhpi5o5zg6qpzya-dev')
tableChapitre = dynamodb.Table('Chapitre-7zccm6vrw5dhhpi5o5zg6qpzya-dev')

myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@192.168.1.22:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["MangaNoKuni_dev"]
mycol_manga = mydb["Manga"]
mycol_chapitre = mydb["Chapitre"]

def insertManga():
    print("INERTION MANGAS IN DYNAMODB")

    # envoyer les mangas dans DynamoDB
    for manga in mycol_manga.find():

        manga['id'] = str(manga['_id'])
        manga.pop('_id')
        manga['_typename'] = "Manga"
        manga['createdAt'] = "{}T{}Z".format(TIME.date(), TIME.time())
        manga['updatedAt'] = "{}T{}Z".format(TIME.date(), TIME.time())

        # Creating a new item in DynamoDB
        try:
            tableManga.put_item(
                Item=manga
            )
            print("{}  inserted".format(manga))
        except Exception as e:
            print("manga not inserted in Dynamo{}".format(manga))
            print(e)

def insertChapitre():
    print("INERTION CHAPTERS IN DYNAMODB")

    # insérer les données dans Dynamodb depuis MongoDB
    TIME = datetime.datetime.now()


    # envoyer les chapitres dans DynamoDB

    for chapitre in mycol_chapitre.find():

        chapitre['_typename'] = "Chapitre"
        chapitre['createdAt'] = "{}T{}Z".format(TIME.date(), TIME.time())
        chapitre['updatedAt'] = "{}T{}Z".format(TIME.date(), TIME.time())
        chapitre['id'] = str(chapitre['_id'])
        chapitre.pop('_id')

        chapitre = json.loads(json.dumps(chapitre), parse_float=Decimal)
        # Creating a new item in DynamoDB
        try:
            tableChapitre.put_item(
                Item=chapitre
            )
            print("{}  inserted".format(chapitre))
        except Exception as e:
            print("chapitre not inserted in dynamo {}".format(chapitre))
            print(e)