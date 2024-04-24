from datetime import datetime


class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, name: str, link_to_vacancy: str, salary_min: int,
                 salary_max: int, requirement: str, responsibility: str,
                 publication_date: str, employment: str, address: str,
                 currency: str):
        """
        Конструктор класса Vacancies.
        :param name: Должность.
        :param link_to_vacancy: Ссылка на вакансию.
        :param salary_min: Минимальная зарплата.
        :param salary_max: Максимальная зарплата.
        :param requirement: Требования к вакансии.
        :param requirement responsibility: Описание обязанностей.
        :param publication_date: Дата публикации вакансии.
        :param employment: Занятость.
        :param address: Адрес.
        """

        self.name = name
        self.link_to_vacancy = link_to_vacancy
        self.salary_min = self._validate_salary(salary_min)
        self.salary_max = self._validate_salary(salary_max)
        self.requirement = self.check_data_str(requirement)
        self.responsibility = self.check_data_str(responsibility)
        self.publication_date = self._date_formatting(publication_date)
        self.employment = employment
        self.address = address
        self.currency = currency

    @staticmethod
    def convert_to_vacancy(data):

        return [
            Vacancy(
                name=item.get('name'),
                link_to_vacancy=item.get('alternate_url', 'Не указано'),
                salary_min=(item.get('salary', {}) or {}).get('from'),
                salary_max=(item.get('salary', {}) or {}).get('to'),
                requirement=item.get('snippet').get('requirement'),
                responsibility=item.get('snippet').get('responsibility'),
                publication_date=item.get('published_at'),
                employment=item.get('employment').get('name'),
                address=(item.get('address', {}) or {}).get('raw', 'Не указан'),
                currency=(item.get('salary', {}) or {}).get('currency',
                                                            'Не указана'))
            for item in data

        ]

    @staticmethod
    def check_data_str(value):
        """ Валидатор для строковых значений """
        if value:
            return value
        return 'Информация не указана'

    @staticmethod
    def _validate_salary(salary) -> int:
        """
         Метод для проверки зарплаты. Если зарплата не указана выставиться
         значение по умолчанию 0.
        """
        if salary is not None:
            return salary
        else:
            return 0

    def __print_salary(self) -> str:
        """
        Метод для корректного выведения заработной платы(ЗП) пользователю.
        Если ЗП указана в объявлении с диапазоном, тогда
        выводится диапазон ЗП. Если одного из параметров нет, тогда выводится
        тот, который есть. В случае отсутствия информации выводится 'Не указана'
        :return: Строку содержащую информацию о зарплате.
        """
        if self.salary_min and self.salary_max:
            return f'{self.salary_min} - {self.salary_max}'
        elif {self.salary_min} and not self.salary_max:
            return f'{self.salary_min}'
        elif not {self.salary_min} and {self.salary_max}:
            return f'{self.salary_max}'
        else:
            return 'Не указана'

    def to_json(self) -> dict:
        """ Метод для возвращения полного описания вакансии """

        return {
            'Должность': self.name,
            'Зарплата': f'{self.__print_salary()} - {self.currency}',
            'Требования к вакансии': self.requirement,
            'Описание обязанностей': self.responsibility,
            'Занятость': self.employment,
            'Адрес': self.address,
            'Дата публикации вакансии': self.publication_date,
            'Ссылка на вакансию': self.link_to_vacancy
        }

    @staticmethod
    def _date_formatting(date):
        """
        Метод для конвертации даты
        :return:
        """
        date_format = datetime.fromisoformat(date)
        date_format = date_format.strftime('%d.%m.%Y %H:%M')
        return date_format

    def __str__(self) -> str:
        """ Метод для вывода информации класса Vacancy"""
        return (
            f'Должность: {self.name}\n'
            f'Зарплата: {self.__print_salary()} {self.currency}\n'
            f'Требования к вакансии: {self.requirement}\n'
            f'Описание обязанностей: {self.responsibility}\n'
            f'Занятость: {self.employment}\n'
            f'Адрес: {self.address}\n'
            f'Дата публикации вакансии: {self.publication_date}\n'
            f'Ссылка на вакансию: {self.link_to_vacancy}\n'
        )

    def __repr__(self) -> str:
        """ Метод для отладки класса Vacancy"""
        return (
            f'{self.__class__.__name__}:\n'
            f'Должность: {self.name}\n'
            f'Зарплата: {self.__print_salary()} {self.currency}\n'
            f'Требования к вакансии: {self.requirement}\n'
            f'Описание обязанностей: {self.responsibility}\n'
            f'Занятость: {self.employment}\n'
            f'Адрес: {self.address}\n'
            f'Дата публикации вакансии: {self.publication_date}\n'
            f'Ссылка на вакансию: {self.link_to_vacancy}\n'
        )

    def __lt__(self, other) -> bool:
        """
        Магический метод для определения работы метода sorted
        :param other: Второй аргумент для сравнения с первым.
        :return: Условие для определения метода sorted.
        """

        if not isinstance(other, (Vacancy, int)):
            raise TypeError('Аргумент должен иметь тип int или Vacancy')
        if type(other) is type(self):
            return self.salary_min < other.salary_min
        return self.salary_min < other.salary_min
