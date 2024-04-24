import json


class JSONSaver:
    """
    Класс для сохранения информации о вакансиях
    """

    def __init__(self, path):
        """
        :param path: Путь к файлу.
        """
        self.path = path

    def upload_vacancies(self):
        """ Загрузить вакансии """

        with open(self.path, mode='r', encoding='utf-8') as file:
            return json.load(file)

    def save_vacancies(self, vacancies):
        """ Сохранить вакансии """
        with open(self.path, mode='w', encoding='utf-8') as file:
            save_vacancies = []
            for vacancy in vacancies:
                save_vacancies.append(vacancy.__dict__)
            json.dump(save_vacancies, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancies):
        """ Метод для добавления вакансий """

        with open(self.path, mode='r', encoding='utf-8') as file:
            old_data = json.load(file)
            for vacancy in vacancies:
                old_data.append(vacancy.__dict__)
        with open(self.path, mode='w', encoding='utf-8') as file:
            json.dump(old_data, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy):
        """ Метод для удаления всех вакансий """
        with open(self.path, mode='r', encoding='utf-8') as file:
            old_data = json.load(file)
            while vacancy in old_data:
                old_data.remove(vacancy)
        with open(self.path, mode='w', encoding='utf-8') as file:
            json.dump(old_data, file, indent=4, ensure_ascii=False)
