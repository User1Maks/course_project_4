import json
from typing import Union


class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, job_title: str, link_to_vacancy: str, salary_min: int,
                 salary_max: int, requirement: str, responsibility: str,
                 publication_date: str, employment: str, address: str):
        """
        Конструктор класса Vacancies.
        :param job_title: Должность.
        :param link_to_vacancy: Ссылка на вакансию.
        :param salary_min: Минимальная зарплата.
        :param salary_max: Максимальная зарплата.
        :param requirement: Требования к вакансии.
        :param requirement responsibility: Описание обязанностей.
        :param publication_date: Дата публикации вакансии.
        :param employment: Занятость.
        :param address: Адрес.
        """

        self.job_title = job_title
        self.link_to_vacancy = link_to_vacancy
        self.salary_min = self._validate_salary(salary_min) or 0
        self.salary_max = self._validate_salary(salary_max) or 0
        self.requirement = requirement
        self.responsibility = responsibility
        self.publication_date = publication_date
        self.employment = employment
        self.address = address

    @staticmethod
    def _validate_salary(salary):
        """
         Метод для проверки зарплаты. Если зарплата не указана выставиться
         значение по умолчанию "Не указано".
        """
        if salary is not None:
            return salary
        else:
            return 0

    def to_json(self) -> dict:
        """ Метод для возвращения полного описания вакансии """

        return {
            'Должность': self.job_title,
            'Зарплата': f'{self.salary_min} до {self.salary_max}',
            'Требования к вакансии': self.requirement,
            'Описание обязанностей': self.responsibility,
            'Занятость': self.employment,
            'Адрес': self.address,
            'Дата публикации вакансии': self.publication_date,
            'Ссылка на вакансию': self.link_to_vacancy
        }

    @staticmethod
    def save_to_json(vacs):
        """
        Метод для сохранения отобранных вакансии в json файл.
        """
        with open('data.json', mode='w', encoding='utf-8') as f:
            json.dump([vacancy.to_json() for vacancy in vacs], f, indent=4,
                      ensure_ascii=False)

    def __str__(self) -> str:
        """ Метод для вывода информации класса Vacancy"""
        return (
            f'Должность: {self.job_title}\n'
            f'Зарплата: {self.salary_min} - {self.salary_max}\n'
            f'Требования к вакансии: {self.requirement}\n'
            f'Описание обязанностей: {self.responsibility}\n'
            f'Занятость: {self.employment}\n'
            f'Адрес:{self.address}\n'
            f'Дата публикации вакансии: {self.publication_date}\n'
            f'Ссылка на вакансию: {self.link_to_vacancy}\n'
        )

    def __repr__(self) -> str:
        """ Метод для отладки класса Vacancy"""
        return (
            f'{self.__class__.__name__}:\n'
            f'Должность: {self.job_title}\n'
            f'Зарплата: {self.salary_min} - {self.salary_max}\n'
            f'Требования к вакансии: {self.requirement}\n'
            f'Описание обязанностей: {self.responsibility}\n'
            f'Занятость: {self.employment}\n'
            f'Адрес:{self.address}\n'
            f'Дата публикации вакансии: {self.publication_date}\n'
            f'Ссылка на вакансию: {self.link_to_vacancy}\n'
        )

    def __lt__(self, other):
        """
        Магический метод для определения работы метода sorted
        :param other:
        :return:
        """
        return self.salary_min < other.salary_min

