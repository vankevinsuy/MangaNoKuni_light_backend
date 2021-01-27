import unittest
import pymongo

myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@192.168.1.22:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["MangaNoKuni_dev"]
mycol_anime = mydb["Anime"]
mycol_episode = mydb["Episode"]


class MyTestCase(unittest.TestCase):
    # verifier que chaque anime possède au moins un épisode
    def test_anime_have_episode(self):
        res = []
        for anime in mycol_anime.find() :
            nb_episode = mycol_episode.count_documents({'mal_id':anime['mal_id']})

            print("mal id : {} title : {} nb episode : {}".format (anime['mal_id'], anime['title'], nb_episode ))
            if nb_episode >= 1 :
                res.append(True)

        self.assertEqual(all(res), True)


if __name__ == '__main__':
    unittest.main()
