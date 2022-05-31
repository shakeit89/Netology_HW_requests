import sys
from tokens import token_yandex
import requests

TOKEN = token_yandex


class YaUploader:
    def __init__(self, token=TOKEN):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application.json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_link_to_upload(self, path):
        link = f'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': {path}, 'overwrite': 'true'}

        try:
            r = requests.get(link, headers=headers, params=params, timeout=5)
        except requests.ConnectionError:
            print(f'Нет соединения с сервером. Возможно, отсутствует подключение к интернету')
            sys.exit()

        if r.status_code == 200:
            print('Связь с сервером установлена')
        else:
            print(f'Внимание! ошибка {r.status_code}')
            print(r.json()['message'])
            sys.exit()

        return r.json()['href']

    def get_file_name_from_path(self, path):  # возвращает имя файла из пути (для Windows!)
        return path[path.rfind('/') + 1:]

    def upload(self, upload_file: str):
        file_name = self.get_file_name_from_path(upload_file)
        with open(upload_file, 'rb') as f:
            r = requests.put(self.get_link_to_upload(path=file_name), data=f.read())
            if r.status_code == 201:
                print(f'Файл {file_name} успешно загружен на Я.Диск')


if __name__ == '__main__':
    path_to_file = 'files/test_ya_disc.txt'
    uploader = YaUploader(TOKEN)
    uploader.upload(path_to_file)
