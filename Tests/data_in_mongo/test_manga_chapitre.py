import unittest
import pymongo

myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@192.168.1.22:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["MangaNoKuni_dev"]
mycol_manga = mydb["Manga"]
mycol_chapitre = mydb["Chapitre"]

class MyTestCase(unittest.TestCase):
    # verifier que chaque manga possède au moins un chapitre
    def test_manga_have_chapter(self):
        res = []
        for anime in mycol_manga.find() :
            nb_chapitre = mycol_chapitre.count_documents({'mal_id':anime['mal_id']})

            print("mal id : {} title : {} nb chapitre : {}".format (anime['mal_id'], anime['title'], nb_chapitre ))
            if nb_chapitre >= 1 :
                res.append(True)

        self.assertEqual(all(res), True)


if __name__ == '__main__':
    unittest.main()
