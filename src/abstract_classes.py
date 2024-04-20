from abc import ABC, abstractmethod


class Api(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями. Является
    родительским классом для класса HeadHunter.
    """

    @abstractmethod
    def __init__(self):
        """ Метод для инициализации """
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """ Метод для получения списка вакансий с сайта hh.ru """
        pass


class VacancyMethods(ABC):
    """
    Абстрактный класс для работы с классом.
    Содержит абстрактные методы для:
    - добавления вакансий в файл;
    - получения данных из файла по указанным критериям;
    - удаление информации о вакансиях.
    """

    @abstractmethod
    def add_vacancy(self):
        """ Добавление вакансии """
        pass

    @abstractmethod
    def fetch_data(self):
        """ Получение данных по указанным критериям """
        pass

    @abstractmethod
    def del_vacancy(self):
        """ Удаление информации о вакансии """
        pass
