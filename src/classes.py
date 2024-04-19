from abc import ABC
import requests


class Api(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями.
    """

    pass


class HH(Api):
    """
    Класс для работы с API HeadHunter.
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers,
                                    params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


class Vacancies:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, job_title: str, link_to_vacancy: str, salary: str,
                 requirement: str, responsibility: str):
        """
        Конструктор класса Vacancies.
        :param job_title: Должность.
        :param link_to_vacancy: Ссылка на вакансию.
        :param salary: Зарплата.
        :param requirement: Требования к вакансии.
        :param requirement responsibility: Описание обязанностей.
        """

        self.job_title = job_title
        self.link_to_vacancy = link_to_vacancy
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility



