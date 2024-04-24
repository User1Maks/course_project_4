from abc import ABC, abstractmethod


class Api(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями. Является
    родительским классом для класса HeadHunter.
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """ Метод для получения списка вакансий с сайта hh.ru """
        pass


class WorkingWithFiles(ABC):
    """
    Абстрактный класс для класса JSONSaver, который будет работать с файлами.
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def upload_vacancies(self):
        pass

    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def add_vacancy(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @staticmethod
    @abstractmethod
    def work_with_the_file():
        pass
