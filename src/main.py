from pprint import pprint

from src.class_savevacancy import SaveVacancy
from src.class_vacancy import Vacancy
from src.class_hh import HeadHunter
from utils.functions import lict_vacancies


def main():
    search_query = input('Введите поисковой запрос: ')
    job_vacancy = HeadHunter().load_vacancies(search_query)
    job_vacancy = sorted(job_vacancy, reverse=True)

    quantity_requests = int(input('Сколько позиций Вы хотите вывести? '))

    pprint(job_vacancy[:quantity_requests])
    SaveVacancy(job_vacancy)


main()
