import psycopg2


class DBCreate():
    def get_connection(self):
        """Подключение к базе данных headhunter_db"""
        self.conn = psycopg2.connect(
            host="localhost",
            database="headhunter_db",
            user="postgres",
            password="simba2106"
        )
        return self.conn

    def get_table(self):
        """Создание таблиц companies, vacancies"""
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("CREATE TABLE companies (company_id int PRIMARY KEY, company_name varchar(100))")
                    cur.execute("CREATE TABLE vacancies (vacancy_id int PRIMARY KEY, company_id int, vacancy_name varchar(100), "
                                "vacancy_link varchar(200), area varchar(100), salary int, experience varchar(100), employment varchar(100))")
        finally:
            self.conn.close()
