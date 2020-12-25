import requests
from bs4 import BeautifulSoup


class malScraper :
    def __init__(self):
        self.base_url = "https://myanimelist.net/{}/{}"

    def manga(self, mal_id : int) -> dict:
        res = {
                "image_url": "",
                "synopsys": "",
                "title": "",
                "title_japanese": "",
                "score": "",
                "authors": "",
                "genres": []
                }

        url = self.base_url.format("manga", str(mal_id))
        mal_html = requests.get(url)
        soup = BeautifulSoup(mal_html.text, "html.parser")

        img = soup.find("img", itemprop="image")
        res["image_url"] = img['data-src']

        synopsys = soup.find("span", itemprop="description")
        res["synopsys"] = synopsys.text

        title = soup.findAll("div", class_="spaceit_pad")
        for t in title:
            if("English" in t.text):
                res["title"] = t.text.split(':')[1].lstrip()
            if ("Japanese" in t.text):
                res["title_japanese"] = t.text.split(':')[1].lstrip()

        score = soup.find("div", attrs={"data-title":"score"})
        res['score'] = str(float(score.text))

        authors_soup = soup.find("span", class_="information studio author")
        authors = str(authors_soup.text)
        authors = authors.replace(",", " ").replace('\n','').rstrip()
        res['authors'] = authors


        div_soup = soup.findAll("span", itemprop="genre")
        for div in div_soup :
            res['genres'].append(div.text)



        return res