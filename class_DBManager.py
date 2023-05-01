import psycopg2


class DBManager():
    def get_connection(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="headhunter_db",
            user="postgres",
            password="simba2106"
        )
        return self.conn


    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT companies.company_name, COUNT(*) FROM vacancies JOIN companies USING(company_id) GROUP BY company_name")
                    rows = cur.fetchall()
                    return rows
        finally:
            self.conn.close()


    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT companies.company_name, vacancy_name, salary, vacancy_link FROM vacancies JOIN companies USING(company_id)")
                    rows = cur.fetchall()
                    return rows
        finally:
            self.conn.close()


    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT AVG(salary) FROM vacancies")
                    rows = cur.fetchall()
                    return rows
        finally:
            self.conn.close()
            
            
    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT vacancy_name, vacancy_link, salary FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies)")
                    rows = cur.fetchall()
                    return rows
        finally:
            self.conn.close()


    def get_vacancies_with_keyword(self):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”"""
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT vacancy_name, vacancy_link, salary FROM vacancies WHERE vacancy_name LIKE '%Python%'")
                    rows = cur.fetchall()
                    return rows
        finally:
            self.conn.close()

