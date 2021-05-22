from pathlib import Path
import os
import requests
from pprint import pprint
class YaUploader:
    def __init__(self, token: str):
        self.token = token
    def get_headers(self):
        return {'Contetn-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)}
    def get_upload_link (self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()
    def upload(self, disk_file_path, file_name):
        path = Path(pathlib.Path.cwd())
        file_path = os.path.join(path, file_name)
        print(disk_file_path+file_name)
        href = self.get_upload_link(disk_file_path=disk_file_path+file_name).get("href")
        response = requests.put(href, data=open(file_path, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
           print ("success")
if __name__ == '__main__':
    uploader = YaUploader('')
    upload= uploader.upload(disk_file_path='test_upload/', file_name = 'test_file.txt')
