from src.abstract_classes import Api
import requests
from src.class_vacancy import Vacancy


class HeadHunter(Api):
    """
    Класс для работы с API HeadHunter.
    """

    def __init__(self):
        """
        Конструктор класса HeadHunter, который получает массив вакансии с сайта
        HeadHunter - hh.ru.
        """
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword: str) -> list[Vacancy]:
        """
        :param keyword: Слово для поиска по вакансиям.
        """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers,
                                    params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies
