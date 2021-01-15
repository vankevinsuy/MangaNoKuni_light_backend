import requests
from bs4 import BeautifulSoup
import time


def extract_episodes(dic, url):
    episodes = getEpisodeLink(url)

    for episode_url in episodes :

        # dictionnaire à insérer dans la liste finale
        res_data = {'mal_id': int(dic['mal_id']), 'title': "", 'num_episode': -1, 'url': ""}

        # récupérer le titre de l'episode
        req = requests.get(episode_url)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, "html.parser")
            res_data['title'] = soup.title.string

            print(res_data['title'])

            # récupérer l'url du chapitre
            res_data['url'] = soup.find("source")['src']


            # récupérer le numéro du chapitre
            try:
                res_data['num_episode'] = int(res_data['title'].split()[-1])
            except:
                res_data['num_episode'] = float(res_data['title'].split()[-1])


            # verifier que les valeurs de res_data sont complétées
            if res_data['mal_id'] != int(dic['mal_id']) :
                return -1
            if res_data['title'] == "" :
                return -1
            if res_data['num_episode'] == -1 :
                return -1
            if res_data['url'] == "" :
                return -1

            yield res_data


# recup lien des chapitres + nom des chapitres
def getEpisodeLink(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    ul_content = soup.find('ul', {'class':"episodes range active"})

    liens = []
    for link in ul_content.findAll('a'):
        liens.append(link.get('href'))

    return liens