import unittest
from Scrapers import mangaNelo


class MyTestCase(unittest.TestCase):
    #### DATA
    input_dic = {'mal_id': '116778', 'url': 'https://manganelo.com/manga/ix917953', 'from': 'manganelo'}

    def test_getChaptersLink(self):

        #### LAUNCH
        result = mangaNelo.getChaptersLink(self.input_dic['url'])

        #### VERIFY
        self.assertTrue(len(result) > 0)

    def test_extract_chapters(self):

        #### LAUNCH
        result = mangaNelo.extract_chapters(self.input_dic)

        #### VERIFY
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
