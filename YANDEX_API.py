import requests


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {"Content-Type": "application/json",
                "Authorization": f"OAuth {self.token}"}

    def get_folder(self, path):
        url_folder = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        response = requests.put(f"{url_folder}?path={path}", headers=headers)
        return response.status_code
        # if response.status_code == 201:
        #     print(f"Папка {path_folder} создана.")
        # else:
        #     response.raise_for_status()
        #     if response.status_code == 409:
        #         print(f"Папка {path_folder} уже существует! Введите другое название.")


if __name__ == '__main__':
    with open('token.txt', 'r', encoding='utf-8') as file:
        token = file.read().strip()
        path_folder = input("Введите имя папки на Yandex диске: ")
        uploader = YaUploader(token).get_folder(path_folder)
