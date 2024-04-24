from src.class_hh import HeadHunter
from utils.functions import get_top_vacancies, filter_vacancies, \
    get_vacancies_by_salary, print_vacancies, sort_vacancies, sal_range
from src.class_vacancy import Vacancy


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunter()

    search_query = input('Введите поисковой запрос: ')

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.load_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.convert_to_vacancy(hh_vacancies)

    # Сохранение информации о вакансиях в файл
    # json_saver = JSONSaver()
    # json_saver.add_vacancy(vacancy)
    # json_saver.delete_vacancy(vacancy)

    # platforms = ['HeadHunter']

    top_n = int(input('Введите количество вакансий для вывода в топ N: '))
    filter_words = input(
        "Введите ключевые слова для фильтрации вакансий: ").split()
    # salary_range = input(
    #     "Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    salary_range = sal_range()

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)

    #  Для вывода необходимого количества вакансий
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print_vacancies(top_vacancies)


if __name__ == '__main__':
    main()
