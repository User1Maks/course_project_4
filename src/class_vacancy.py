import json


class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, job_title: str, link_to_vacancy: str,
                 salary_min: int, salary_max: int,
                 requirement: str, responsibility: str, publication_date: str,
                 employment: str, address: str):
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
        self.salary_min = self._validate_salary(salary_min)
        self.salary_max = self._validate_salary(salary_max)
        self.requirement = requirement
        self.responsibility = responsibility
        self.publication_date = publication_date
        self.employment = employment
        self.address = address

    @staticmethod
    def _validate_salary(salary):
        """
         Метод для проверки зарплаты. Если зарплата не указана выставиться
         значение по умолчанию 0.
        """
        if salary is not None:
            return salary
        else:
            return 0

    def to_json(self):
        """ Метод для возвращения полного описания вакансии """
        return {
            'Должность': {self.job_title},
            'Минимальная зарплата': {self.salary_min},
            'Максимальная зарплата': {self.salary_max},
            'Требования к вакансии': {self.requirement},
            'Описание обязанностей': {self.responsibility},
            'Занятость': {self.employment},
            'Адрес': {self.address},
            'Дата публикации вакансии': {self.publication_date},
            'Ссылка на вакансию': {self.link_to_vacancy}
        }

    @staticmethod
    def save_to_json(vacs):
        """ Метод для сохранения отобранных вакансии в json файл."""
        with open('data.json', mode='w', encoding='utf-8') as file:
            json.dump([vacancy.to_json() for vacancy in vacs], file, indent=4,
                      ensure_ascii=False)

    def __repr__(self) -> object:
        """ Метод для отладки класса Vacancy"""
        return (
            f'{self.__class__.__name__}: '
            f'{self.job_title}',
            {self.link_to_vacancy},
            {self.salary_min},
            {self.salary_max},
            {self.requirement},
            {self.responsibility},
            {self.publication_date},
            {self.employment},
            {self.address}
        )

    def __str__(self) -> str:
        """ Метод для вывода информации класса Vacancy"""
        return (
            f'Должность: {self.job_title}\n'
            f'Минимальная зарплата: {self.salary_min}\n'
            f'Максимальная зарплата: {self.salary_max}\n'
            f'Требования к вакансии: {self.requirement}\n'
            f'Описание обязанностей: {self.responsibility}\n'
            f'Занятость: {self.employment}\n'
            f'Адрес:{self.address}\n'
            f'Дата публикации вакансии: {self.publication_date}\n'
            f'Ссылка на вакансию: {self.link_to_vacancy}'
        )


if __name__ == '__main__':
    a = Vacancy('Develope', 'https', 50_000,
                80_000,
                'Huarith', 'jang',
                '2.02.2024', 'JOPA', 'Ni')
    print(a.__repr__())
    print()
    print(a)
