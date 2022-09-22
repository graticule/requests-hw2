from typing import List
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type':'application/json',
                'Authorization': f'OAuth {self.token}'}

    def upload(self, file_path: str):
        """Метод загружает файл на яндекс диск"""
        url_upload = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(url_upload, params=params, headers=self.get_headers())
        href = response.json()['href']
        return requests.put(href, data=open(file_path, 'rb'))

    def upload_group(self, file_paths: List[str]):
        """Метод загружает файлы из списка на яндекс диск"""
        if file_paths:
            for f in file_paths:
                self.upload(f)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)