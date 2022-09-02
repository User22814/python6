import requests
from bs4 import BeautifulSoup

count = int(input("Какое количество картинок нужно скачать?\n"))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def write_image_from_url(image_name: str) -> None:
    with open(f'tmp/{image_name}.jpg', mode='wb') as file:
        file.write(requests.get(url='https://picsum.photos/600/600/', headers=headers).content)
        print(f'File {image_name}.jpg скачан')


for i in range(1, count + 1):
    write_image_from_url(image_name=f'img{i}')
