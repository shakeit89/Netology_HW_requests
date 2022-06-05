import sys
from tokens import token_yandex
import requests
import datetime

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
        params = {'path': path, 'overwrite': 'true'}

        try:
            r = requests.get(link, headers=headers, params=params, timeout=5)
        except requests.ConnectionError:
            print(f'Нет соединения с сервером. Возможно, отсутствует подключение к интернету')
            sys.exit()

        if r.status_code == 200:
            with open('log.txt', 'a') as log:
                log.write(
                    f'{datetime.datetime.now().strftime("%H:%M:%S:%f %d/%m/%Y")} | Связь с сервером установлена\n')
        else:
            print(f'Внимание! ошибка {r.status_code}')
            print(r.json()['message'])
            sys.exit()

        return r.json()['href']

    def _get_file_name_from_path(self, path):  # возвращает имя файла из пути (для Windows \ для linux /! )
        return path[path.rfind('\\') + 1:]  #сделать автоматически!!!

    def upload(self, upload_file: str):
        file_name = f"/files_for_netology/" + self._get_file_name_from_path(upload_file)
        with open(upload_file, 'rb') as f:
            r = requests.put(self.get_link_to_upload(path=file_name), data=f.read())
            with open('log.txt', 'a') as log:
                if r.status_code == 201:
                    log.write(
                        f'{datetime.datetime.now().strftime(f"%H:%M:%S:%f %d/%m/%Y")} | Файл '
                        f'{self._get_file_name_from_path(file_name)} успешно загружен на Я.Диск\n')
                    print(f'\t{datetime.datetime.now().strftime(f"%H:%M:%S:%f %d/%m/%Y")} | Файл '
                        f'{file_name[file_name.rfind("/")+1:]} успешно загружен на Я.Диск', end="")
                else:
                    log.write(
                        f'{datetime.datetime.now().strftime(f"%H:%M:%S:%f %d/%m/%Y")} | При загрузке файла '
                        f'{self._get_file_name_from_path(file_name)} произошла ошибка {r.status_code}\n'
                    )
                    print(f'При загрузке файла произошла ошибка {r.status_code}')



if __name__ == '__main__':
    path_to_file = 'files/test_ya_disc.txt'
    uploader = YaUploader(TOKEN)
    uploader.upload(path_to_file)
