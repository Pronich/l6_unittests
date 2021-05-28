import requests
from pprint import pprint
import os
from settings import ya_token


token = ya_token

class yaUpLoader:
    def __init__(self, token):
        self.token = token
        self.url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        self.headers = {'Content-Type': 'Application/json', 'Authorization': 'OAuth ' + self.token}

    def create_folder(self, path):
        params = {'path': path}
        resp = requests.put(self.url, params=params, headers=self.headers)
        return resp.status_code

    def check_folder(self, path):
        params = {'path': path}
        resp = requests.get(self.url, params=params, headers=self.headers)
        return (resp.status_code, resp.json()['path'])

    def delete_folder(self, path):
        params = {'path': path}
        resp = requests.delete(self.url, params=params, headers=self.headers)
        return resp.status_code



if __name__ == '__main__':
    uploader = yaUpLoader(token)
    file_name = 'netology_tests'
    file_to = f'netology/{file_name}'
    print(uploader.create_folder(file_to))
    print(uploader.check_folder(file_to))
    print(uploader.delete_folder(file_to))