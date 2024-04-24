from src.class_vacancy import Vacancy


def filter_vacancies(vacancies_list: list[Vacancy], filter_words: list) -> list:
    """
    Функция для фильтрации списка вакансий по словам.
    :param vacancies_list: Список для фильтрации по словам.
    :param filter_words: Список слов введенных пользователем.
    :return: Отфильтрованный по словам список.
    """
    filter_list = []

    for vacancy in vacancies_list:
        for word in filter_words:
            if word in vacancy.responsibility or vacancy.requirement:
                filter_list.append(vacancy)
                break
    return filter_list


def get_top_vacancies(sorted_vacancies, top_n: int):
    """
    Функция для возвращения списка топ в количестве указанного пользователем
    :return: Количество N вакансий
    """

    list_filter_top = sorted_vacancies[:top_n]
    return list_filter_top


def print_vacancies(top_vacancies: list[Vacancy]):
    """
    Функция для вывода в консоль списка вакансий
    :return:
    """
    for top in top_vacancies:
        print(top)
    return


def sal_range():
    """
    Функция для возвращения диапазона зарплаты от пользователя
    salary_min, salary_max
    :return:
    """
    salary_range = input('Введите диапазон зарплат: ')
    two_salary = []

    for salary in salary_range.split():
        if salary.isdigit():
            two_salary.append(int(salary))

    if len(two_salary) >= 2:
        salary_min = int(min(two_salary))
        salary_max = int(max(two_salary))
        salary = [int(salary_min), int(salary_max)]
        return salary
    else:
        return two_salary


def get_vacancies_by_salary(filtered_vacancies: list[Vacancy], salary_range):
    """
    Функция для получения вакансии по зарплате
    :return:
    """
    salary_vacancies = []

    for vacancy in filtered_vacancies:
        if len(salary_range) == 1:
            for salary in filtered_vacancies:
                if salary.salary_min >= int(min(salary_range)):
                    salary_vacancies.append(vacancy)

        if len(salary_range) == 2:
            for salary in filtered_vacancies:
                if salary.salary_min >= salary_range[0]:
                    salary_vacancies.append(salary)

    return salary_vacancies


def sort_vacancies(ranged_vacancies):
    """
    Отсортировываем информацию о вакансиях для вывода на первые позиции
    вакансии с большей зарплатой
    :param ranged_vacancies:
    :return:
    """
    list_range = sorted(ranged_vacancies, reverse=True)
    return list_range
