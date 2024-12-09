from src.classes import DBManager
from src.config import config
from src.connecting_API import HeadHunterAPI
from src.creature_bd import creature_bd, save_data_to_database, creature_table


def main():
    hh_api = HeadHunterAPI()

    # search_query: list[str] = input("Введите поисковый запрос: ").split(", ")

    employer = ["магнит", "авто"]
    hh_data: list = hh_api.load_vacancies(employer)

    # Создание базы данных
    # params = config()
    params = {"host": "localhost",
              "user": "postgres",
              "password": 1650,
              "port": 5432,
              "client_encoding": "utf-8"}
    creature_bd(params)

    # Создание таблиц
    creature_table(params)

    # Запись информации в таблицы
    e = [{'id': '11454714', 'name': 'Lalu beauty (ИП Магние Мариам Хуссейновна)',
          'url': 'https://api.hh.ru/employers/11454714', 'alternate_url': 'https://hh.ru/employer/11454714',
          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1336405.png',
                        '240': 'https://img.hhcdn.ru/employer-logo/6965627.png',
                        '90': 'https://img.hhcdn.ru/employer-logo/6965626.png'},
          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=11454714', 'open_vacancies': 1},
         {'id': '5961775', 'name': 'ИП ООО Магнит Средняя Азия', 'url': 'https://api.hh.ru/employers/5961775',
          'alternate_url': 'https://hh.ru/employer/5961775',
          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1270989.png',
                        '240': 'https://img.hhcdn.ru/employer-logo/6704267.png',
                        '90': 'https://img.hhcdn.ru/employer-logo/6704266.png'},
          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=5961775', 'open_vacancies': 9},
         {'id': '9493373', 'name': 'Кабельный Завод Магна', 'url': 'https://api.hh.ru/employers/9493373',
          'alternate_url': 'https://hh.ru/employer/9493373',
          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1180713.jpg',
                        '240': 'https://img.hhcdn.ru/employer-logo/6343279.jpeg',
                        '90': 'https://img.hhcdn.ru/employer-logo/6343278.jpeg'},
          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9493373', 'open_vacancies': 7},
         {'id': '3863038', 'name': 'Авто-К', 'url': 'https://api.hh.ru/employers/3863038',
          'alternate_url': 'https://hh.ru/employer/3863038', 'logo_urls': None,
          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3863038', 'open_vacancies': 3},
         {'id': '10365880', 'name': 'Авто Клиника', 'url': 'https://api.hh.ru/employers/10365880',
          'alternate_url': 'https://hh.ru/employer/10365880', 'logo_urls': None,
          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10365880', 'open_vacancies': 1},
         {'id': '932741', 'name': 'Авто-Комби', 'url': 'https://api.hh.ru/employers/932741',
          'alternate_url': 'https://hh.ru/employer/932741', 'logo_urls': None,
          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=932741', 'open_vacancies': 1}]

    v = {'id': '112671007', 'premium': False, 'name': 'Продавец-консультант в сеть магазинов M COSMETIC',
         'department': None, 'has_test': False, 'response_letter_required': False,
         'area': {'id': '2759', 'name': 'Ташкент', 'url': 'https://api.hh.ru/areas/2759'},
         'salary': {'from': 2800000, 'to': None, 'currency': 'UZS', 'gross': False},
         'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-12-06T09:31:05+0300', 'created_at': '2024-12-06T09:31:05+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=112671007',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/112671007?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/112671007',
         'relations': [], 'employer': {'id': '5961775', 'name': 'ИП ООО Магнит Средняя Азия',
                                       'url': 'https://api.hh.ru/employers/5961775',
                                       'alternate_url': 'https://hh.ru/employer/5961775',
                                       'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/6704267.png',
                                                     'original': 'https://img.hhcdn.ru/employer-logo-original/1270989.png',
                                                     '90': 'https://img.hhcdn.ru/employer-logo/6704266.png'},
                                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=5961775',
                                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'образование средне-специальное или среднее. -опыт работы (приветствуется, но не обязателен). -владение ПК. -наличие медицинской книжки. -знание программы 1С...',
            'responsibility': 'консультация покупателей. -выкладка товара в зале. -контроль сроков годности и качества продукции. -установка и актуализация ценников. -работа за кассой. -'},
         'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '97', 'name': 'Продавец-консультант, продавец-кассир'}],
         'accept_incomplete_resumes': True, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None}

    print(11, hh_data[0:3])
    save_data_to_database(hh_data, params)

    dbm = DBManager(params)

    # print("get_companies_and_vacancies_count", dbm.get_companies_and_vacancies_count())
    # print("get_all_vacancies", dbm.get_all_vacancies())
    # print("get_avg_salary", dbm.get_avg_salary())
    # print("get_vacancies_with_higher_salary", dbm.get_vacancies_with_higher_salary())
    # print("get_vacancies_with_keyword", dbm.get_vacancies_with_keyword("продаж"))

    print(12, "len:", len(hh_data))
    # search = input("Введите название компании: ")


if __name__ == "__main__":
    main()

a = [{'id': '11454714', 'name': 'Lalu beauty (ИП Магние Мариам Хуссейновна)',
      'url': 'https://api.hh.ru/employers/11454714', 'alternate_url': 'https://hh.ru/employer/11454714',
      'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1336405.png',
                    '240': 'https://img.hhcdn.ru/employer-logo/6965627.png',
                    '90': 'https://img.hhcdn.ru/employer-logo/6965626.png'},
      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=11454714', 'open_vacancies': 0},
     {'id': '10220070', 'name': 'Автомагазин Магнит', 'url': 'https://api.hh.ru/employers/10220070',
      'alternate_url': 'https://hh.ru/employer/10220070',
      'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1151496.jpg',
                    '240': 'https://img.hhcdn.ru/employer-logo/6226447.jpeg',
                    '90': 'https://img.hhcdn.ru/employer-logo/6226446.jpeg'},
      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10220070', 'open_vacancies': 0},
     {'id': '1969819', 'name': 'АН Магнит-Инвест', 'url': 'https://api.hh.ru/employers/1969819',
      'alternate_url': 'https://hh.ru/employer/1969819',
      'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/414452.jpg',
                    '240': 'https://img.hhcdn.ru/employer-logo/2099883.jpeg',
                    '90': 'https://img.hhcdn.ru/employer-logo/2099882.jpeg'},
      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1969819', 'open_vacancies': 0}]

b = [{'id': '10844173', 'name': '32 Улыбки', 'url': 'https://api.hh.ru/employers/10844173',
      'alternate_url': 'https://hh.ru/employer/10844173', 'logo_urls': None,
      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10844173', 'open_vacancies': 0},
     {'id': '10250195', 'name': '4hands (ИП Толстых Евгения Александровна)',
      'url': 'https://api.hh.ru/employers/10250195', 'alternate_url': 'https://hh.ru/employer/10250195',
      'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10250195', 'open_vacancies': 0},
     {'id': '3649674', 'name': 'ADN OTAU', 'url': 'https://api.hh.ru/employers/3649674',
      'alternate_url': 'https://hh.ru/employer/3649674',
      'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/632374.jpg',
                    '240': 'https://img.hhcdn.ru/employer-logo/2970649.jpeg',
                    '90': 'https://img.hhcdn.ru/employer-logo/2970648.jpeg'},
      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3649674', 'open_vacancies': 0}]
