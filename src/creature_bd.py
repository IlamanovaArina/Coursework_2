import psycopg2
import requests

from psycopg2 import errors as Perrors


def creature_bd(params):
    """ Создание/подключение к базе данных """
    # -*- coding: utf-8 -*-

    conn = psycopg2.connect(database="postgres", **params)
    conn.autocommit = True

    with conn.cursor() as curs:
        curs.execute("DROP DATABASE Data_HeadHunter;")
        curs.execute("CREATE DATABASE Data_HeadHunter;")

    # curs.execute("ALTER DATABASE Data_HeadHunter CHARACTER SET utf8 COLLATE utf8_unicode_ci;")
    conn.close()
    # print('Победа №1')


def creature_table(params):
    # try:
    con = psycopg2.connect(database="data_headhunter", **params)

    with con.cursor() as cur:
        # cur.execute("DROP TABLE vacancies")
        # cur.execute("DROP TABLE employers")

        cur.execute("""CREATE TABLE employers (
                        id_employers INT PRIMARY KEY,
                        name VARCHAR,
                        alternate_url TEXT,
                        open_vacancies INT)""")

        cur.execute("""CREATE TABLE vacancies (
                        id_vacancies INT PRIMARY KEY,
                        id_employers INT,
                        name VARCHAR,
                        salary INT,
                        alternate_url TEXT,
                        
                        FOREIGN KEY (id_employers) REFERENCES employers(id_employers)
                        )""")

    con.commit()
    con.close()
    # print('Победа №2')


# except Exception as e:
#     print(e)


def save_data_to_database(hh_data: list[dict], params: dict):
    """ Функция для записи данных в таблицы """
    # try:
    conn = psycopg2.connect(database="data_headhunter", **params)
    for data in hh_data:
        with conn.cursor() as cur:

            cur.execute("TRUNCATE TABLE vacancies CASCADE")
            cur.execute("TRUNCATE TABLE employers CASCADE")

            cur.execute(
                "INSERT INTO employers(id_employers, name, alternate_url, open_vacancies) VALUES (%s, %s, %s, %s)",
                (data.get('id'), data.get('name'), data.get('alternate_url'), data.get('open_vacancies')))

            response = requests.get(data.get('vacancies_url'))
            if response.status_code == 200:
                list_vacancies: list[dict] = response.json()['items']

                for vac in list_vacancies:
                    if vac.get('salary') is not None:
                        cur.execute("INSERT INTO vacancies(id_vacancies, id_employers, name, alternate_url) "
                                    "VALUES (%s, %s, %s, %s)",
                                    (vac.get('id'), data.get('id'), vac.get('name'),
                                     vac.get('alternate_url')))

                    if vac.get('salary').get('to') is not None:
                        cur.execute("INSERT INTO vacancies(id_vacancies, id_employers, name, salary, alternate_url) "
                                    "VALUES (%s, %s, %s, %s, %s)",
                                    (vac.get('id'), data.get('id'), vac.get('name'), vac.get('salary').get('to'),
                                     vac.get('alternate_url')))
                    else:
                        cur.execute("INSERT INTO vacancies(id_vacancies, id_employers, name, salary, alternate_url) "
                                    "VALUES (%s, %s, %s, %s, %s)",
                                    (vac.get('id'), data.get('id'), vac.get('name'), vac.get('salary').get('from'),
                                     vac.get('alternate_url')))

    conn.commit()
    conn.close()
    # print('Победа №3')

    # except Exception as e:
    #     print(e)


e = [{'id': '11454714', 'name': 'Lalu beauty (ИП Магние Мариам Хуссейновна)',
          'url': 'https://api.hh.ru/employers/11454714', 'alternate_url': 'https://hh.ru/employer/11454714',
          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1336405.png',
                        '240': 'https://img.hhcdn.ru/employer-logo/6965627.png',
                        '90': 'https://img.hhcdn.ru/employer-logo/6965626.png'},
          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=11454714', 'open_vacancies': 1}]

# v = {"items": [
#     {"id": "112710304", "premium": false, "name": "Мастер маникюра и педикюра", "department": null, "has_test": false,
#      "response_letter_required": false, "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
#      "salary": {"from": 50000, "to": 150000, "currency": "RUR", "gross": false},
#      "type": {"id": "open", "name": "Открытая"},
#      "address": {"city": "Москва", "street": "Егерская улица", "building": "3", "lat": 55.793657, "lng": 37.683482,
#                  "description": null, "raw": "Москва, Егерская улица, 3",
#                  "metro": {"station_name": "Красносельская", "line_name": "Сокольническая", "station_id": "1.60",
#                            "line_id": "1", "lat": 55.780014, "lng": 37.666097}, "metro_stations": [
#              {"station_name": "Красносельская", "line_name": "Сокольническая", "station_id": "1.60", "line_id": "1",
#               "lat": 55.780014, "lng": 37.666097},
#              {"station_name": "Митьково", "line_name": "МЦД-3", "station_id": "135.852", "line_id": "135",
#               "lat": 55.786389, "lng": 37.6675},
#              {"station_name": "Сокольники", "line_name": "Сокольническая", "station_id": "1.134", "line_id": "1",
#               "lat": 55.789282, "lng": 37.679895},
#              {"station_name": "Сокольники", "line_name": "Большая кольцевая линия", "station_id": "97.823",
#               "line_id": "97", "lat": 55.791111, "lng": 37.678889}], "id": "16590883"}, "response_url": null,
#      "sort_point_distance": null, "published_at": "2024-12-06T16:29:55+0300", "created_at": "2024-12-06T16:29:55+0300",
#      "archived": false, "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=112710304",
#      "show_logo_in_search": null, "insider_interview": null, "url": "https://api.hh.ru/vacancies/112710304?host=hh.ru",
#      "alternate_url": "https://hh.ru/vacancy/112710304", "relations": [],
#      "employer": {"id": "11454714", "name": "Lalu beauty (ИП Магние Мариам Хуссейновна)",
#                   "url": "https://api.hh.ru/employers/11454714", "alternate_url": "https://hh.ru/employer/11454714",
#                   "logo_urls": {"240": "https://img.hhcdn.ru/employer-logo/6965627.png",
#                                 "original": "https://img.hhcdn.ru/employer-logo-original/1336405.png",
#                                 "90": "https://img.hhcdn.ru/employer-logo/6965626.png"},
#                   "vacancies_url": "https://api.hh.ru/vacancies?employer_id=11454714", "accredited_it_employer": false,
#                   "trusted": true}, "snippet": {"requirement": null,
#                                                 "responsibility": "уметь делать комбинированный маникюр и покрытие гель лак с выравниванием. Пиши и рассказывай о себе!"},
#      "contacts": null, "schedule": {"id": "fullDay", "name": "Полный день"}, "working_days": [],
#      "working_time_intervals": [], "working_time_modes": [], "accept_temporary": false,
#      "professional_roles": [{"id": "40", "name": "Другое"}], "accept_incomplete_resumes": true,
#      "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
#      "employment": {"id": "full", "name": "Полная занятость"}, "adv_response_url": null, "is_adv_vacancy": false,
#      "adv_context": null}], "found": 1, "pages": 1, "page": 0, "per_page": 20, "clusters": null, "arguments": null,
#       "fixes": null, "suggests": null,
#       "alternate_url": "https://hh.ru/search/vacancy?employer_id=11454714&enable_snippets=true"}

if __name__ == "__main__":
    params = {"host": "localhost",
              "user": "postgres",
              "password": 1650,
              "port": 5432,
              "client_encoding": "utf-8"}

    creature_bd(params)
    creature_table(params)
    save_data_to_database(e, params)
