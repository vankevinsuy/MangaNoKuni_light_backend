import pymongo
import boto3
import datetime

def Launch():
    myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
    mydb = myclient["MangaNoKuni"]
    mycol_manga = mydb["Manga"]
    mycol_chapitre = mydb["Chapitre"]

    # insérer les données dans Dynamodb depuis MongoDB
    dynamodb = boto3.resource('dynamodb')
    tableManga = dynamodb.Table('Manga-hdsfapoi3rdyfeji6ir65yknoq-dev')
    TIME = datetime.datetime.now()

    # envoyer les mangas dans DynamoDB
    for manga in mycol_manga.find():

        data = {
            '_typename' : "Manga",
            'createdAt' : "{}T{}Z".format(TIME.date(), TIME.time()),
            'updatedAt' : "{}T{}Z".format(TIME.date(), TIME.time()),
            'id' : str(manga['_id']),

            'Mal_id' : int(manga['Mal_id']),
            'Url' : manga['Url'],
            'from' : manga['from']
        }

        # Creating a new item in DynamoDB
        try :
            tableManga.put_item(
                Item=data
            )
            print("{}  inserted".format(data))
        except Exception as e:
            print("data not inserted {}".format(data))
            print(e)




    # envoyer les chapitres dans DynamoDB
    tableChapitre = dynamodb.Table('Chapitre-hdsfapoi3rdyfeji6ir65yknoq-dev')

    for chapitre in mycol_chapitre.find():

        data = {
            '_typename' : "Manga",
            'createdAt' : "{}T{}Z".format(TIME.date(), TIME.time()),
            'updatedAt' : "{}T{}Z".format(TIME.date(), TIME.time()),
            'id' : str(chapitre['_id']),

            'Mal_id' : int(chapitre['Mal_id']),
            'title' : chapitre['title'],
            'num_chapitre': int(chapitre['num_chapitre']),
            'url' : chapitre['url'],
            'images_html' : chapitre['images_html']
        }

        # Creating a new item in DynamoDB
        try :
            tableChapitre.put_item(
                Item=data
            )
            print("{}  inserted".format(data))
        except Exception as e:
            print("data not inserted {}".format(data))
            print(e)