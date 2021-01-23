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
tableAnime = dynamodb.Table('Anime-7zccm6vrw5dhhpi5o5zg6qpzya-dev')
tableEpisode = dynamodb.Table('Episode-7zccm6vrw5dhhpi5o5zg6qpzya-dev')

myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@192.168.1.22:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["MangaNoKuni_dev"]
mycol_manga = mydb["Manga"]
mycol_chapitre = mydb["Chapitre"]
mycol_anime = mydb["Anime"]
mycol_episode = mydb["Episode"]

def insertManga():
    print("INERTION MANGAS IN DYNAMODB")

    # envoyer les mangas dans DynamoDB
    for manga in mycol_manga.find():

        manga['id'] = str(manga['_id'])
        manga.pop('_id')
        manga['_typename'] = "Manga"
        manga['createdAt'] = "{}T{}Z".format(TIME.date(), TIME.time())
        manga['updatedAt'] = "{}T{}Z".format(TIME.date(), TIME.time())

        manga = json.loads(json.dumps(manga), parse_float=Decimal)

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

def insertAnime():
    print("INERTION ANIME IN DYNAMODB")

    # envoyer les mangas dans DynamoDB
    for anime in mycol_anime.find():

        anime['id'] = str(anime['_id'])
        anime.pop('_id')
        anime['_typename'] = "Anime"
        anime['createdAt'] = "{}T{}Z".format(TIME.date(), TIME.time())
        anime['updatedAt'] = "{}T{}Z".format(TIME.date(), TIME.time())

        anime = json.loads(json.dumps(anime), parse_float=Decimal)

        # Creating a new item in DynamoDB
        try:
            tableAnime.put_item(
                Item=anime
            )
            print("{}  inserted".format(anime))
        except Exception as e:
            print("anime not inserted in Dynamo{}".format(anime))
            print(e)


def insertEpisode():
    print("INERTION EPISODE IN DYNAMODB")

    # envoyer les mangas dans DynamoDB
    for episode in mycol_episode.find():

        episode['id'] = str(episode['_id'])
        episode.pop('_id')
        episode['_typename'] = "Episode"
        episode['createdAt'] = "{}T{}Z".format(TIME.date(), TIME.time())
        episode['updatedAt'] = "{}T{}Z".format(TIME.date(), TIME.time())

        episode = json.loads(json.dumps(episode), parse_float=Decimal)

        # Creating a new item in DynamoDB
        try:
            tableEpisode.put_item(
                Item=episode
            )
            print("{}  inserted".format(episode))
        except Exception as e:
            print("episode not inserted in Dynamo{}".format(episode))
            print(e)