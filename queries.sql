1. Получает список всех компаний и количество вакансий у каждой компании:
SELECT companies.company_name, COUNT(*) FROM vacancies JOIN companies USING(company_id) GROUP BY company_name;
2. Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию:
SELECT companies.company_name, vacancy_name, salary, vacancy_link FROM vacancies JOIN companies USING(company_id);
3. Получает среднюю зарплату по вакансиям:
SELECT AVG(salary) FROM vacancies;
4. Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям:
SELECT vacancy_name, vacancy_link, salary FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies);
5. Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например "python":
SELECT vacancy_name, vacancy_link, salary FROM vacancies WHERE vacancy_name LIKE '%Python%';