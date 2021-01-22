import requests
from bs4 import BeautifulSoup


def extract_chapters(dic, url):
    res = []
    chapitres = getChaptersLink(url)

    for chapitre_url in chapitres :

        # dictionnaire à insérer dans la liste finale
        res_data = {'mal_id': int(dic['mal_id']), 'title': "", 'num_chapitre': -1, 'url': "", "images_html": "",
                    'images_html': "future update"}

        # récupérer le titre du chapitre
        req = requests.get(chapitre_url)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, "html.parser")
            res_data['title'] = soup.title.string

            # récupérer l'url du chapitre
            res_data['url'] = chapitre_url

            # récupérer le numéro du chapitre
            try :
                res_data['num_chapitre'] = int(chapitre_url.split('/')[-1].split('_')[-1])
            except :
                res_data['num_chapitre'] = float(chapitre_url.split('/')[-1].split('_')[-1])


            # verifier que les valeurs de res_data sont complétées
            if res_data['mal_id'] != int(dic['mal_id']) :
                return -1
            if res_data['title'] == "" :
                return -1
            if res_data['num_chapitre'] == -1 :
                return -1
            if res_data['url'] == "" :
                return -1
            if res_data['images_html'] == "" :
                return -1

            yield res_data


# recup lien des chapitres + nom des chapitres
def getChaptersLink(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    liens = []
    for link in soup.findAll('a', attrs={'class': "chapter-name text-nowrap"}):
        liens.append(link.get('href'))

    return liens
