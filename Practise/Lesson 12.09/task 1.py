import requests
import aiohttp
import asyncio
import re

url = "https://jsonplaceholder.typicode.com/photos/"
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
data = requests.get(url=url, headers=headers, timeout=5.0)

photos = data.json()
# print(photos)

# [
#   {
#     "albumId": 1,
#     "id": 1,
#     "title": "accusamus beatae ad facilis cum similique qui sunt",
#     "url": "https://via.placeholder.com/600/92c952",
#     "thumbnailUrl": "https://via.placeholder.com/150/92c952"
#   }

class Photo:
    def __init__(self, albumId: int, id: int, title: str, url: str, thumbnailUrl: str):
        self.albumId = albumId
        self._id = id
        self._title = title
        self._url = url
        self._thumbnailUrl = thumbnailUrl

    def check_valid_url(self) -> bool:
        """Проверка валидности ссылки через регулярные выражения"""
        return len(re.findall(r'\bhttp.*?\b', self._url)) > 0

    @staticmethod
    def check_valid_url_static(url: str) -> bool:
        """Проверка валидности внешней ссылки через регулярные выражения"""
        return len(re.findall(r'\bhttp.*?\b', url)) > 0

    def __repr__(self):
        return f" | {self._id}, {self._title} | "

photo_list = []

for photo in photos:
    photo_list.append(Photo(albumId=photo['albumId'],
    id=photo['id'],
    title=photo['title'],
    url=photo['url'],
    thumbnailUrl=photo['thumbnailUrl']))

print(photo_list)

# photos = Photo(
#     albumId=photos['albumId'],
#     id=photos['id'],
#     title=photos['title'],
#     url=photos['url'],
#     thumbnailUrl=photos['thumbnailUrl']
#     )

print(Photo.check_valid_url_static(url='https://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python'))
print(Photo.check_valid_url_static(url='hps://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python'))
Photo.check_valid_url_static(url='https://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python')
# async def get_photos():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url=url, headers=headers, timeout=5.0) as response_object:
#             response = await response_object.read()
#             print(response)
#
#
# asyncio.run(get_photos())

