from hh_request import*
from db_create import*
from db_filling_tables import*
from class_DBManager import*


# Список работодателей
companies_list = ['Сбер. IT', 'Enjoypro', 'X5 Tech', 'КИБЕР-РОМ', 'Тензор', 'ООО АЙТИ.СПЕЙС', 'Eqvanta',
                  'YADRO', 'DIGITAL FUTURE SYSTEMS', 'ООО Лаборатория Наносемантика']

hh = HH()
companies_id = hh.get_request(companies_list)
companies_dict = dict(zip(companies_id, companies_list))
vacancies_link = hh.get_url(companies_id)
vacancies_list = hh.get_vacancy(vacancies_link)
database = DBCreate()
database_conn = database.get_connection()
database_table = database.get_table()
db_headhunter = DBFilling()
db_conn = db_headhunter.get_connection()
db_filling = db_headhunter.db_filling(companies_dict, vacancies_list)


print("Собраны данные о 10 работодателях и их вакансиях с сайта hh.ru.\n"
      "Выберите номер для дальнейшего действия:\nНажмите 1, чтобы вывести список всех компаний и количество вакансий у каждой компании\n"
      "Нажмите 2, чтобы вывести список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n"
      "Нажмите 3, чтобы вывести среднюю зарплату по вакансиям\n"
      "Нажмите 4, чтобы вывести список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
      "Нажмите 5, чтобы вывести список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”\n"
      "Нажмите 'stop', чтобы завершить программу")

user_input = input(f'Введите команду: ')

while user_input != 'stop':
    if user_input == '1':
        db_hh = DBManager()
        conn = db_hh.get_connection()
        vacancies_count = db_hh.get_companies_and_vacancies_count()
        for i in vacancies_count:
            print(i)
        user_input = input(f'Введите команду: ')

    if user_input == '2':
        db_hh = DBManager()
        conn = db_hh.get_connection()
        all_vacancies = db_hh.get_all_vacancies()
        for i in all_vacancies:
            print(i)
        user_input = input(f'Введите команду: ')

    if user_input == '3':
        db_hh = DBManager()
        conn = db_hh.get_connection()
        avg_salary = db_hh.get_avg_salary()
        print(avg_salary)
        user_input = input(f'Введите команду: ')

    if user_input == '4':
        db_hh = DBManager()
        conn = db_hh.get_connection()
        vacancies_with_higher_salary = db_hh.get_vacancies_with_higher_salary()
        for i in vacancies_with_higher_salary:
            print(i)
        user_input = input(f'Введите команду: ')

    if user_input == '5':
        keyword = input(f'Введите слово: ')
        db_hh = DBManager()
        conn = db_hh.get_connection()
        vacancies_with_keyword = db_hh.get_vacancies_with_keyword(keyword)
        for i in vacancies_with_keyword:
            print(i)
        user_input = input(f'Введите команду: ')

print('Работа окончена')


