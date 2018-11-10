from random import randint
import urllib
import json


class Giphy:
    def __init__(self, key):
        self.url = 'https://api.giphy.com/v1/gifs'
        self.key = key

    def search_random(self):
        url = f'{self.url}/random?api_key={self.key}&limit=1'
        data = json.loads(urllib.request.urlopen(url).read())
        return data["data"]["image_original_url"]

    def search_keyword(self, keyword, limit=100):
        url = f'{self.url}/search?q={keyword}&api_key={self.key}&limit={limit}'
        data = json.loads(urllib.request.urlopen(url).read())

        # if empty
        if (len(data["data"]) == 0):
            return "not dank enough (empty results)"

        # get a random gif from pool
        num = randint(1, len(data["data"]) - 1)
        return data["data"][num]["bitly_gif_url"]
