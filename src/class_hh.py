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

    def load_vacancies(self, keyword: str) -> list[Vacancy]:
        """
        Метод для получения списка вакансий.
        :param keyword: Слово для поиска по вакансиям.
        :return: Cписок вакансий полученных с hh.ru.
        """
        params = {'query': keyword, 'area': '113', 'per_page': 100}
        response = requests.get(url=self.url, params=params)
        return self.__convert_to_vacancy(response.json())

    def __convert_to_vacancy(self, data) -> list[Vacancy]:
        """
        Метод для конвертации вывода в нужный формат. Он является приватным
        потому, что он используется только внутри метода load_vacancies.
        :param data: Массив вакансий с сайта hh.ru
        :return: Список вакансий.
        """
        return [
            Vacancy(
                job_title=item['name'],
                link_to_vacancy=
                (item.get('employer', {}) or {}
                 ).get('alternate_url', 'Не указано'),
                salary_min=
                (item.get('salary', {}) or {}).get('from'),
                salary_max=
                (item.get('salary', {}) or {}).get('to'),
                requirement=item['snippet']['requirement'],
                responsibility=item['snippet']['responsibility'],
                publication_date=item['published_at'],
                employment=item['employment']['name'],
                address=
                (item.get('address', {}) or {}).get('raw', 'Не указан'))
            for item in data.get('items')

        ]
