import json
import os
from config import ROOT_DIR

# PATH_TO_OPERATIONS = os.path.join(ROOT_DIR, 'data', file_name)


class JSONSaver:
    """
    Класс для сохранения информации о вакансиях
    """

    def __init__(self, path):
        """
        :param path: Путь к файлу.
        """
        self.path = path

    def save_to_json(self, vacancies):
        with open(self.path, mode='w', encoding='utf-8') as file:
            save_vacancies = []
            for vacancy in vacancies:
                save_vacancies.append(vacancy)
            json.dump(vacancy, file, indent=4, ensure_ascii=False)

    def save_to_txt(self):
        with open('data.txt', mode='w', encoding='utf-8') as file:
            json.dump([v.to_json() for v in self.list_vacancy], file, indent=4,
                      ensure_ascii=False)

    def add_vacancy(self, vacancy):
        """
        Метод для добавления вакансий
        :param vacancy: Список вакансии
        """
        pass

    def delete_vacancy(self, vacancy):
        """
        Метод для удаления вакансии
        :param vacancy:
        :return:
        """
        pass
