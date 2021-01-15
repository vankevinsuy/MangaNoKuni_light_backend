import unittest
from Scrapers.Manga import mangallama


class MyTestCase(unittest.TestCase):
    #### DATA
    input_dic = \
        {"_id": {"$oid": "5fe0b8ee71e34d0a90f76efa"},
         "mal_id": 86337,
         "url": [{"from": "manganelo", "url": "https://manganelo.com/manga/black_clover"},
                 {"from": "mangallama", "url": "https://mangallama.com/manga.php?manga=Black-Clover"}],
         "image_url": "https://cdn.myanimelist.net/images/manga/2/166254.jpg",
         "synopsys": "In a world full of magic, Asta—an orphan who is overly loud and energetic—possesses none whatsoever. Despite this, he dreams of becoming the Wizard King, a title bestowed upon the strongest mage in the Clover Kingdom. Possessing the same aspiration, Asta's childhood friend and rival Yuno has been blessed with the ability to control powerful wind magic. Even with this overwhelming gap between them, hoping to somehow awaken his magical abilities and catch up to Yuno, Asta trains his body relentlessly every day.\n\r\nIn the Clover Kingdom, once a person turns 15 years old, it is time for them to receive their Grimoire, an item allowing its wielder to use their magic to its full capacity. At the ceremony, Yuno obtains a Grimoire with a legendary four-leaf clover, indicating the exceptional strength of its wielder, while Asta pointlessly waits for his. Feeling dejected, yet unwilling to give up, Asta sees Yuno caught by a mage who is trying to steal Yuno's special Grimoire. Despite being completely overpowered by Yuno's captor, Asta's will to keep fighting rewards him with his very own Grimoire—one with an unheard-of black five-leaf clover.\n\r\n[Written by MAL Rewrite]",
         "title": "Black Clover", "title_japanese": "ブラッククローバー", "authors": "Tabata  Yuuki (Story & Art)",
         "genre": ["Action", "Comedy", "Fantasy", "Magic", "Shounen"], "score": "7.67",
         "title_search": "BLACKCLOVER"}

    def test_getChaptersLink(self):

        #### LAUNCH
        result = mangallama.getChaptersLink(self.input_dic['url'][1]['url'])

        #### VERIFY
        self.assertTrue(len(result) > 0)


    def test_extract_chapters(self):

        #### LAUNCH
        result = mangallama.extract_chapters(self.input_dic, self.input_dic['url'][1]['url'])

        #### VERIFY
        self.assertTrue(result != None)


if __name__ == '__main__':
    unittest.main()
