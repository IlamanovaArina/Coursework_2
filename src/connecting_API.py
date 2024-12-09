import requests
from requests import RequestException


class HeadHunterAPI:
    """ Класс для работы с API HeadHunter """

    def __init__(self):
        self.__url = 'https://api.hh.ru/employers'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__employers = []

    def __connect(self):
        """ Метод для get запроса """
        try:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                return response
            else:
                raise RequestException
        except Exception as e:
            print(e)

    def load_vacancies(self, keyword: list[str]):
        """ Данный метод позволяет отобрать всю информацию по вакансиям,
        в котором есть ключевое слово (переменная - keyword) """
        for key in keyword[0:10]:
            self.__params['text'] = key
            self.__params['page'] = 0

            while self.__params.get('page') != 10:
                response = self.__connect()
                employers: list[dict] = response.json()['items']
                for emp in employers:
                    if emp["open_vacancies"] > 0:
                        self.__employers.append(emp)
                self.__params['page'] += 1
        return self.__employers


# a = [{'id': '11347515', 'name': 'Aliev HR Services & solutions', 'url': 'https://api.hh.ru/employers/11347515',
#        'alternate_url': 'https://hh.ru/employer/11347515',
#        'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1318413.PNG',
#                      '240': 'https://img.hhcdn.ru/employer-logo/6893827.png',
#                      '90': 'https://img.hhcdn.ru/employer-logo/6893826.png'},
#        'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=11347515', 'open_vacancies': 3},
#       {'id': '9024300', 'name': 'Anex Tour (ООО Регнум)', 'url': 'https://api.hh.ru/employers/9024300',
#        'alternate_url': 'https://hh.ru/employer/9024300',
#        'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/984858.jpg',
#                      '240': 'https://img.hhcdn.ru/employer-logo/5560253.jpeg',
#                      '90': 'https://img.hhcdn.ru/employer-logo/5560252.jpeg'},
#        'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9024300', 'open_vacancies': 1},
#       {'id': '11332012', 'name': 'Galaxy Groom', 'url': 'https://api.hh.ru/employers/11332012',
#        'alternate_url': 'https://hh.ru/employer/11332012',
#        'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1315542.png',
#                      '240': 'https://img.hhcdn.ru/employer-logo/6882403.png',
#                      '90': 'https://img.hhcdn.ru/employer-logo/6882402.png'},
#        'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=11332012', 'open_vacancies': 1}]
