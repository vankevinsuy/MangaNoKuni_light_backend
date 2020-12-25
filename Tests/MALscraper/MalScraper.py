import unittest
from Scrapers.MALscraper.malScraper import malScraper
from testExpectedResults import *


class MalScraper(unittest.TestCase):

    # verifier que les données récoltées par le scraper sont correctes
    def test_manga(self):
        data = malScraper().manga(13)
        self.assertEqual(manga_scraper_result, data)


if __name__ == '__main__':
    unittest.main()
