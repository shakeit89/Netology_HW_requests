import requests
from time import sleep
from datetime import datetime, timedelta


class Stack_question:
    def __init__(self, tag="python", days=2):
        self.tag = tag
        self.days = days

    def _get_unix_time_to_day(self):
        new_date = datetime.now() - timedelta(days=self.days)
        date_unix = str(int(datetime.timestamp(new_date)))
        return date_unix

    # запрос через строку
    # def get_questions(self):
    #     for page in range(1, 26): #максимальное число доступных страниц без токена
    #         url = f'https://api.stackexchange.com/2.3/questions?fromdate={self._get_unix_time_to_day()}&page={page}&site=stackoverflow&tagged={self.tag}&ord=desc&sort=creation'
    #         r = requests.get(url)
    #         sleep(0.4)
    #         required_link = r.json()['items'][0]['link']
    #         required_date = datetime.fromtimestamp(r.json()['items'][0]['creation_date'])
    #         print(f'Ссылка не вопрос: {required_link}. Дата публикации: {required_date}')

    # запрос через параметры

    def get_questions(self):
        params = {
            'fromdate': self._get_unix_time_to_day(),
            'tagged': self.tag,
            'ord': 'desc',
            'sort': 'creation',
            'site': 'stackoverflow'}

        for page in range(1, 26):  # максимальное число доступных страниц без токена 25
            params['page'] = page
            url = f'https://api.stackexchange.com/2.3/questions'
            r = requests.get(url, params=params)
            if r.status_code != 200:
                print(f'Ошибка! Имя ошибки: {r.json()["error_name"]}. Сообщение ошибки: {r.json()["error_message"]}')
                return
            sleep(0.4)
            required_link = r.json()['items'][0]['link']
            required_date = datetime.fromtimestamp(r.json()['items'][0]['creation_date'])

            print(f'Ссылка не вопрос: {required_link}. Дата публикации: {required_date}')


if __name__ == '__main__':
    overstack = Stack_question()
    overstack.get_questions()
