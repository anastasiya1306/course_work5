from hh_request import*
import psycopg2


hh = HH()
companies_id = hh.get_request(companies_list)
companies_dict = dict(zip(companies_id, companies_list))
vacancies_link = hh.get_url(companies_id)
vacancies_list = hh.get_vacancy(vacancies_link)


"""Подключение к базе данных headhunter_db"""
conn = psycopg2.connect(
    host="localhost",
    database="headhunter_db",
    user="postgres",
    password="simba2106"
)

"""Заполнение таблиц companies, vacancies"""
try:
    with conn:
        with conn.cursor() as cur:
            for id_company, name in companies_dict.items():
                cur.execute('INSERT INTO companies VALUES (%s, %s)', (id_company, name))
            for i in vacancies_list:
                cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s)', (i['vacancy_id'], i['company_id'],
                                                                                          i['vacancy_name'], i['vacancy_link'],
                                                                                          i['area'], i['salary'],
                                                                                          i['experience'], i['employment']))
finally:
    conn.close()
