from yandex_disc import YaUploader
from tokens import token_yandex

TOKEN = token_yandex #указываем свой токен
uploader = YaUploader(TOKEN)
path_to_file = 'files/test_ya_disc.txt'
uploader.upload(path_to_file)