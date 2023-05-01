import requests

#Список работодателей
companies_list = ['Сбер. IT', 'Enjoypro', 'X5 Tech', 'КИБЕР-РОМ', 'Тензор', 'ООО АЙТИ.СПЕЙС', 'Eqvanta',
                  'YADRO', 'DIGITAL FUTURE SYSTEMS', 'ООО Лаборатория Наносемантика']

class HH():
    def get_request(self, companies_list):
        """Получение id работодателя по названию компании из списка"""
        companies_id = []
        for i in companies_list:
            url = f"https://api.hh.ru/employers?text={i}"
            response = requests.get(url)
            data = response.json()
            company_id = data['items'][0]['id']
            companies_id.append(company_id)
        return companies_id

    def get_url(self, companies_id):
        """Получение ссылок на список вакансий всех компаний"""
        vacancies_list = []
        for i in companies_id:
            url = f"https://api.hh.ru/employers/{i}"
            response = requests.get(url)
            data = response.json()
            vacancies_list.append(data['vacancies_url'])
        return vacancies_list

    @staticmethod
    def get_salary(salary):
        """Обрабатываем salary(зарплата): выводим 'от' и 'до', если оба поля присутствуют, если одно из полей
        отсутствует, то выводим то, что известно. Или выводим 0, если поле отсутствует"""
        if salary:
            if salary.get('to') and salary.get('from'):
                return salary['to']
            elif salary.get('to') and not salary.get('from'):
                return salary['to']
            elif salary.get('from') and not salary.get('to'):
                return salary['from']
        else:
            return 0


    def get_vacancy(self, vacancies_list):
        """Получение списка вакансий по каждому работодателю"""
        jobs = []
        for item in vacancies_list:
            response = requests.get(f"{item}", params={'per_page': '100', 'page': 0})
            data = response.json()
            for i in data['items']:
                jobs.append({
                    "vacancy_id": i['id'],
                    "company_id": i['employer']['id'],
                    "vacancy_name": i['name'],
                    "company_name": i['employer']['name'],
                    "vacancy_link": i['alternate_url'],
                    "area": i['area']['name'],
                    "salary": self.get_salary(i['salary']),
                    "experience": i['experience']['name'],
                    "employment": i['employment']['name']
                })
        return jobs
