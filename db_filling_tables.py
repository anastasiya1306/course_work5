import psycopg2


class DBFilling():
    def get_connection(self):
        """Подключение к базе данных headhunter_db"""
        self.conn = psycopg2.connect(
            host="localhost",
            database="headhunter_db",
            user="postgres",
            password="simba2106"
        )
        return self.conn


    def db_filling(self, companies_dict, vacancies_list):
        """Заполнение таблиц companies, vacancies"""
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    for id_company, name in companies_dict.items():
                        cur.execute('INSERT INTO companies VALUES (%s, %s)', (id_company, name))
                    for i in vacancies_list:
                        cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (i['vacancy_id'], i['company_id'],
                                                                                                  i['vacancy_name'], i['vacancy_link'],
                                                                                                  i['area'], i['salary'],
                                                                                                  i['experience'], i['employment']))
        finally:
            self.conn.close()
