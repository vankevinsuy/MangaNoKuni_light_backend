import unittest
from Scrapers.Anime import four_anime


class MyTestCase(unittest.TestCase):
    #### DATA
    input_dic = {"mal_id":20,
                 "url":[{"from":"4anime","url":"https://4anime.to/anime/naruto"}],
                 "image_url":"https://cdn.myanimelist.net/images/anime/13/17405.jpg",
                 "synopsys":"Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the village, the Fourth Hokage, sacrificed his life and sealed the monstrous beast inside the newborn Naruto.\n\r\nNow, Naruto is a hyperactive and knuckle-headed ninja still living in Konohagakure. Shunned because of the Kyuubi inside him, Naruto struggles to find his place in the village, while his burning desire to become the Hokage of Konohagakure leads him not only to some great new friends, but also some deadly foes.\n\r\n[Written by MAL Rewrite]",
                 "title":"Naruto",
                 "title_japanese":"ナルト",
                 "score":"7.91",
                 "authors":"Studio Pierrot",
                 "genre":["Action","Adventure","Comedy","Super Power","Martial Arts","Shounen"],
                 "title_search":"NARUTO"}

    def test_getEpisodesLink(self):

        #### LAUNCH
        result = four_anime.getEpisodeLink(self.input_dic['url'][0]['url'])

        #### VERIFY
        self.assertTrue(len(result) == 220)

    def test_extract_episodes(self):

        #### LAUNCH
        result = four_anime.extract_episodes(self.input_dic, self.input_dic['url'][0]['url'])

        #### VERIFY
        self.assertTrue(result.__next__() != {})


if __name__ == '__main__':
    unittest.main()
