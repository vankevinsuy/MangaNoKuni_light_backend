import requests
from bs4 import BeautifulSoup


def extract_chapters(dic):
    res = []
    chapitres = getChaptersLink(dic)

    for chapitre_url in chapitres :

        # dictionnaire à insérer dans la liste finale
        res_data = {
            'mal_id': int(dic['mal_id']),
            'title': "",
            'num_chapitre': -1,
            'url': "",
            "images_html": ""
        }

        # # mettre les liens images sous formes de balises
        # images = getImgages(chapitre_url)
        # images_to_html = "<div style= margin:0;padding:0;display:flex;flex-direction:column;>"
        # for img_link in images:
        #     images_to_html  = images_to_html + "<img src=  {}  style=max-width:100%;height:auto; />".format(img_link)
        #
        # images_to_html = images_to_html + "</div>"
        # res_data['images_html'] = images_to_html
        res_data['images_html'] = "future update"

        # récupérer le titre du chapitre
        req = requests.get(chapitre_url)
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

        res.append(res_data)

    return res


# recup lien des chapitres + nom des chapitres
def getChaptersLink(dic):
    req = requests.get(dic["url"])
    soup = BeautifulSoup(req.text, "html.parser")

    liens = []
    for link in soup.findAll('a', attrs={'class': "chapter-name text-nowrap"}):
        liens.append(link.get('href'))

    return liens

# recup baslises des images
def getImgages(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    liens_images = []
    for link in soup.findAll('img'):

        if "themes" not in link.get('src').split('/'):
            liens_images.append(link.get('src'))

    return liens_images
