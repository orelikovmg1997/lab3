from base_client import BaseClient
import requests
import json

class Id(BaseClient):
    BASE_URL = 'https://api.vk.com/method/users.get'
    http_method = 'GET'

    def __init__(self, name):
        self.name = name

    def get_params(self):
        return 'user_ids=' + self.name

        # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        response = None
        response = requests.get(self.BASE_URL + '?' + self.get_params())
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        try:
            uobj = json.loads(response.text)
            print ('ID пользователя: '+ str((uobj.get('response')[0].get('uid'))))
            return uobj.get('response')[0].get('uid')
        except:
            raise Exception("Couldn't handle response for username {}".format(self.name))