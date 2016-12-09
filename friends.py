from base_client import BaseClient
from urllib import parse
import requests
import json
from datetime import datetime


class Friends(BaseClient):
    BASE_URL = 'https://api.vk.com/method/friends.get'
    http_method = 'GET'

    def __init__(self, uid):
        self.uid = uid

    # Получение GET параметров запроса
    def get_params(self):
         return parse.urlencode({'user_id': self.uid,'fields' : 'bdate'})

        # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        response = requests.get(self.BASE_URL + '?' + self.get_params())
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        try:
            age = []
            uobj = json.loads(response.text)
            friends = uobj.get('response')
            for friend in friends:
                bdate = friend.get('bdate')
                if bdate is None or bdate.count('.') < 2:
                    continue
                bdate = datetime.strptime(bdate, "%d.%m.%Y")
                ndate = datetime.now()
                age.append(int((ndate - bdate).days) // 365)

            unage = list(set(age))
            return sorted((x,age.count(x)) for x in unage)
        except:
            raise Exception("Couldn't handle response for friends of uid {}".format(self.uid))