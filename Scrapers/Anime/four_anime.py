import requests
from bs4 import BeautifulSoup

def extract_episodes(dic, url, failedFile):

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

            # récupérer l'url de l'épisode
            for script in soup.findAll('script',{'type':'text/javascript'}):
                str_script = str(script)
                if "mirror_dl" in str_script:
                    for element in str_script.split():
                        if "href" in element :
                            res_data['url'] = element.replace('href=\\"', '').replace('\\"><i', '')

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
        else:
            print("fail : " + episode_url)
            failedFile.add_link(episode_url)

# recup lien des chapitres + nom des chapitres
def getEpisodeLink(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    ul_content = soup.find('ul', {'class':"episodes range active"})

    liens = []
    for link in ul_content.findAll('a'):
        liens.append(link.get('href'))

    return liens