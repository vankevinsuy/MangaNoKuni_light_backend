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

            'mal_id' : int(manga['mal_id']),
            'url' : manga['url'],
            'from' : manga['from'],
            'title' : manga['title'],
            'title_japanese': manga['title_japanese'],
            'synopsys': manga['synopsys'],
            'image_url': manga['image_url'],
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

            'mal_id' : int(chapitre['mal_id']),
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