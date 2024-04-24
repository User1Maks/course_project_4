from utils.functions import get_top_vacancies, print_vacancies, \
    filter_vacancies, sal_range, get_vacancies_by_salary, sort_vacancies


def test_get_top_vacancies(vacancies2):
    """
    Тест для проверки возвращения топ вакансий в количестве N указанная
    пользователем
    """
    assert get_top_vacancies(vacancies2, 2) == vacancies2[:2]


def test_print_vacancies(vacancies):
    """ Тест для тестирования вывода в консоль """
    assert print_vacancies(vacancies) is None


def test_filter_vacancies(vacancies, filter_words):
    """ Тест на фильтрацию списка по словам """
    assert filter_vacancies(vacancies, filter_words) == [vacancies[0]]


def test_sal_range():
    """ Тест на возвращения диапазона зарплаты от пользователя """
    assert sal_range == sal_range


def test_get_vacancies_by_salary(vacancies, salary_range2):
    """ Тест на фильтрацию вакансий по словам """
    assert get_vacancies_by_salary(vacancies, salary_range2) == [vacancies[0]]


def test_sort_vacancies(vacancies):
    """
    Тест на сортировку вакансий по убыванию по ЗП без учета курсов
    денежных валют
    """
    assert sort_vacancies(vacancies) == vacancies

