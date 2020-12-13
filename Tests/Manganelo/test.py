import unittest
from Scrapers import mangaNelo
from Tests.Manganelo import testExpectedResult


class MyTestCase(unittest.TestCase):
    def test_getChaptersLink(self):
        #### DATA
        input_dic = {'Mal_id': '116778', 'Url': 'https://manganelo.com/manga/ix917953', 'from': 'manganelo'}

        #### LAUNCH
        result = mangaNelo.getChaptersLink(input_dic)

        #### VERIFY
        self.assertEqual(result, testExpectedResult.test_getChaptersLink)

    def test_getImages(self):
        #### DATA
        input = "https://manganelo.com/chapter/ix917953/chapter_46"

        #### LAUNCH
        result = mangaNelo.getImgages(input)

        #### VERIFY
        self.assertEqual(result, testExpectedResult.test_getImages)

    def test_extract_chapters(self):
        #### DATA
        input = {'Mal_id': '116778', 'Url': 'https://manganelo.com/manga/ix917953', 'from': 'manganelo'}

        #### LAUNCH
        result = mangaNelo.extract_chapters(input)
        expected = testExpectedResult.test_extract_chapters

        #### VERIFY
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
