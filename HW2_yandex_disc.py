from yandex_disc import YaUploader
from tokens import token_yandex
import os
from tqdm import tqdm

DIR_NAME = 'files'
BASE_PATH = os.getcwd()
print(os.listdir(os.path.join(BASE_PATH, DIR_NAME)))
file_names = [x for x in os.listdir(DIR_NAME) if os.path.isfile(os.path.join(DIR_NAME, x))]
# file_names = list(filter(lambda x: os.path.isfile(os.path.join(DIR_NAME, x)), os.listdir(DIR_NAME)))
TOKEN = token_yandex  # указываем свой токен
uploader = YaUploader(TOKEN)


t = tqdm(total=len(file_names))

for files in file_names:
    path_to_file = os.path.join(BASE_PATH, DIR_NAME, files)
    uploader.upload(path_to_file)
    t.update(1)
t.close()

print(f'Все файлы из папки {os.path.join(BASE_PATH, DIR_NAME)} загружены')


