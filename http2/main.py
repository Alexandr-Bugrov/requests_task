import requests


class YaUploader:
    def __init__(self, token:str):
        self.token = token


    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}


    def upload(self, file_path:str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'True'}
        response = requests.get(upload_url, params = params, headers = headers)
        href_json = response.json()
        href = href_json['href']
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Загружено')



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'new_file.txt'
    token =
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
