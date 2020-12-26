import pymongo
import boto3
import datetime
from decimal import Decimal
import json
import time

def insertManga():
    print("INERTION MANGAS IN DYNAMODB")
    myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
    mydb = myclient["MangaNoKuni"]
    mycol_manga = mydb["Manga"]

    # insérer les données dans Dynamodb depuis MongoDB
    dynamodb = boto3.resource('dynamodb')
    tableManga = dynamodb.Table('Manga-nvyqnuhtenbrfmeatpaukmpv24-myenv')
    TIME = datetime.datetime.now()


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
    myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
    mydb = myclient["MangaNoKuni"]
    mycol_chapitre = mydb["Chapitre"]

    # insérer les données dans Dynamodb depuis MongoDB
    dynamodb = boto3.resource('dynamodb')
    TIME = datetime.datetime.now()


    # envoyer les chapitres dans DynamoDB
    tableChapitre = dynamodb.Table('Chapitre-nvyqnuhtenbrfmeatpaukmpv24-myenv')

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