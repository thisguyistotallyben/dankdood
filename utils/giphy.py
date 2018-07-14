from random import randint
import urllib
import json


class Giphy:
    def __init__(self, key):
        self.key = key

    def search_random(self):
        url = f'http://api.giphy.com/v1/gifs/random?api_key={self.key}&limit=1'
        data = json.loads(urllib.request.urlopen(url).read())
        return data["data"]["image_original_url"]

    def search_keyword(self, keyword, num_results):
        return ''
