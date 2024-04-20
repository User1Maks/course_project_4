import json


class SaveVacancyJson:
    """
    Класс для сохранения информации о вакансии в JSON-файл
    """

    def __init__(self, list_vacancy):
        self.list_vacancy = list_vacancy

    def save_to_json(self):
        with open('data.json', mode='w', encoding='utf-8') as f:
            json.dump([v.to_json() for v in self.list_vacancy], f, indent=4,
                      ensure_ascii=False)


class SaveVacancyTxt:
    """
    Класс для сохранения информации о вакансии в TXT-файл
    """

    def __init__(self, list_vacancy):
        self.list_vacancy = list_vacancy

    def save_to_json(self):
        with open('data.txt', mode='w', encoding='utf-8') as f:
            json.dump([v.to_json() for v in self.list_vacancy], f, indent=4,
                      ensure_ascii=False)
