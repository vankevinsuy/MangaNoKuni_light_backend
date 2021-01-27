import unittest
import requests
import pymongo
from bs4 import BeautifulSoup

myclient = pymongo.MongoClient("mongodb://snoozy:deadoralive@192.168.1.22:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["MangaNoKuni_dev"]
mycol_manga = mydb["Manga"]

class TestMalUrl(unittest.TestCase):

    # verifier que les données existes toujours dans myanimeList
    def test_url_exist(self):
        list_status = []
        for manga in mycol_manga.find():
            url = "https://myanimelist.net/manga/{}".format(str(manga['mal_id']))
            status = requests.get(url).status_code
            if(status == 200):
                list_status.append(True)

        self.assertEqual(True, any(list_status))

    # vérifier que les balises du sites sont les même qu'avant
    def test_website_structure(self):
        url = "https://myanimelist.net/manga/13"
        html_content = requests.get(url).text

        soup = BeautifulSoup(html_content, "html.parser")
        print(soup)

if __name__ == '__main__':
    unittest.main()
