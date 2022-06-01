from yandex_disc import YaUploader
from tokens import token_yandex
import os
import time
from tqdm import tqdm

DIR_NAME = 'files'
BASE_PATH = os.getcwd()
file_names = os.listdir(DIR_NAME)
TOKEN = token_yandex  # указываем свой токен
uploader = YaUploader(TOKEN)


t = tqdm(total=len(file_names))

for files in file_names:
    path_to_file = os.path.join(BASE_PATH, DIR_NAME, files)
    uploader.upload(path_to_file)
    t.update(1)
t.close()

print(f'Все файлы из папки {os.path.join(BASE_PATH, DIR_NAME, files)} загружены')

