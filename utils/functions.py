import json


from src.class_hh import HeadHunter


def salary_comparison(vacancy, salary_min):
    """ Метод для сравнения вакансий между собой по зарплате"""

    vacancy_with_filtered_salary = []

    for vac in vacancy:
        if vac['salary']['from'] >= salary_min:
            vacancy_with_filtered_salary.extend(vac)
    return vacancy_with_filtered_salary


def lict_vacancies(word):
    """ Метод для сохранения списка вакансий """
    list_vac = []

    for v in HeadHunter().load_vacancies(word):
        list_vac.append(v)

    return list_vac
