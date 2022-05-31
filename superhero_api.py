import requests
from tokens import token_superhero
from pprint import pprint

TOKEN = token_superhero


class Superhero:

    def __init__(self, name, token=TOKEN):
        self.token = token
        self.name = name
        self.id = None
        self.intelligence = None

    def get_hero_id(self):
        url = f'https://superheroapi.com/api/{self.token}/search/{self.name}'
        try:
            response = requests.get(url, timeout=5)
        except requests.ConnectionError:
            print(f'Нет соединения с сервером. Супергерой {self.name} не будет учтен в дальнейшем')
            self.id = ''
            return self.id
        # response.raise_for_status()
        if response.status_code != 200:
            print(f'При получении данных возникла ошибка {response.status_code}, супергерой {self.name} не будет '
                  f'учтен в дальнейшем')
            self.id = ''
            return self.id
        if response.json()['response'] != 'error':
            self.id = response.json()['results'][0]['id']
            return self.id
        else:
            print(f'При поиске супергероя {self.name} возникла ошибка: {response.json()["error"]}')
            self.id = ''

    def get_intelligence(self):
        self.get_hero_id()
        if not self.id:  # проверка на несуществующего супергероя
            self.intelligence = 0
            return 0
        url = f'https://superheroapi.com/api/{self.token}/{self.id}/powerstats'
        response = requests.get(url)
        response.raise_for_status()
        r = response.json()
        self.intelligence = int(r['intelligence'])
        return self.intelligence


if __name__ == "__main__":
    hulk = Superhero('Hulk')
    pprint(hulk.get_hero_id())
    pprint(hulk.get_intelligence())
    print(hulk.id, hulk.intelligence)
