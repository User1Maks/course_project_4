import pytest

from src.class_vacancy import Vacancy


@pytest.fixture()
def filter_words():
    return ['Python']


@pytest.fixture()
def salary_range():
    return [100000 - 250000]


@pytest.fixture()
def salary_range2():
    return [100000]


@pytest.fixture()
def vacancies():
    return [Vacancy("Android Middle / Senior разработчик мобильных "
                    "приложений",
                    "https://hh.ru/vacancy/96970412",
                    250000,
                    600000,
                    "Требуемый опыт работы: не менее 1 года. "
                    "Знание <highlighttext>Python</highlighttext>-telegram-bot "
                    "и Django. Базовое знакомство с Docker и Nginx. ",
                    "Информация не указана",
                    "2024-04-21T13:46:04+0300",
                    "Полная занятость",
                    "Ташкент, улица Садыка Азимова, 68",
                    "UZS"
                    ),
            Vacancy('Backend Python Developer (Middle+)',
                    "https://hh.ru/vacancy/97631653",
                    80000,
                    130000,
                    "<highlighttext>Jva</highlighttext>. От 3-х лет "
                    "на backend-е. Опыт работы в создании "
                    "ИТ-архитектуры. Опыт работы в роли разработчика "
                    "с...",
                    "Недостаток времени на поездки в разные магазины "
                    "за набором желаемых товаров. Неудобство носить"
                    " покупки, при использовании общественного "
                    "транспорта. ",
                    "2024-04-21T13:46:04+0300",
                    "Полная занятость",
                    "Не указан",
                    "RUR"
                    )
            ]


@pytest.fixture
def vacancies2():
    return [{
        "name": "Android Middle / Senior разработчик мобильных приложений",
        "link_to_vacancy": "https://hh.ru/vacancy/96970412",
        "salary_min": 10000000,
        "salary_max": 0,
        "requirement": "Требуемый опыт работы: не менее 1 года. "
                       "Знание "
                       "<highlighttext>Python</highlighttext>-telegram-bot "
                       "и Django. Базовое знакомство с Docker и Nginx. ",
        "responsibility": "Информация не указана",
        "publication_date": "15.04.2024 08:26",
        "employment": "Полная занятость",
        "address": "Ташкент, улица Садыка Азимова, 68",
        "currency": "UZS"
    },
        {
            "name": "Backend Python Developer (Middle+)",
            "link_to_vacancy": "https://hh.ru/vacancy/97631653",
            "salary_min": 1000000,
            "salary_max": 1300000,
            "requirement": "<highlighttext>Python</highlighttext>. От 3-х лет "
                           "на backend-е. Опыт работы в создании "
                           "ИТ-архитектуры. Опыт работы в роли разработчика "
                           "с...",
            "responsibility": "Недостаток времени на поездки в разные магазины "
                              "за набором желаемых товаров. Неудобство носить"
                              " покупки, при использовании общественного "
                              "транспорта. ",
            "publication_date": "22.04.2024 14:47",
            "employment": "Полная занятость",
            "address": "Не указан",
            "currency": "KZT"
        },
        {
            "name": "Machine Learning Engineer "
                    "(специалист по машинному обучению)",
            "link_to_vacancy": "https://hh.ru/vacancy/96182192",
            "salary_min": 950000,
            "salary_max": 1200000,
            "requirement": "Знание основ Deep Learning в сфере CV и NLP "
                           "(работа с разнородными данными: изображения, "
                           "текст, табулярные данные). Владение "
                           "<highlighttext>Python</highlighttext> (опыт...",
            "responsibility": "Разрабатывать ML модели для широкого круга "
                              "задач."
                              " Участвовать в разработке сервиса на основе ML "
                              "на всех этапах: от сбора данных...",
            "publication_date": "04.04.2024 13:42",
            "employment": "Полная занятость",
            "address": "Алматы, улица Шевченко, 157",
            "currency": "KZT"
        },
        {
            "name": "CTO (AR/AI)",
            "link_to_vacancy": "https://hh.ru/vacancy/96291009",
            "salary_min": 800000,
            "salary_max": 1200000,
            "requirement": "Опыт работы с продуктами, основанными на "
                           "технологиях AR и AI, для мобильных и веб-платформ. "
                           "Глубокое понимание применения технологий AR...",
            "responsibility": "Разработка и реализация технологической "
                              "стратегии компании, с фокусом на продукты"
                              "AR/AI/VR. Управление техническими аспектами"
                              " жизненного цикла продукта, включая...",
            "publication_date": "23.04.2024 21:04",
            "employment": "Полная занятость",
            "address": "Москва, Тверской бульвар, 13с1",
            "currency": "RUR"
        },
        {
            "name": "Data Engineer / DevOps",
            "link_to_vacancy": "https://hh.ru/vacancy/97033829",
            "salary_min": 800000,
            "salary_max": 1000000,
            "requirement": "Опыт работы с базами данных PostgreSQL и "
                           "Clickhouse. — Хорошее знание "
                           "<highlighttext>Python</highlighttext>, "
                           "практические знания SQL, оптимизация больших "
                           "запросов. — Иметь опыт в...",
            "responsibility": "Создание нового и оптимизация имеющегося "
                              "функционала DWH. — Интеграция источников данных "
                              "в единое хранилище. — Разработка и поддержка "
                              "ETL/ELT процессов "
                              "(<highlighttext>Python</highlighttext>...",
            "publication_date": "21.04.2024 16:30",
            "employment": "Полная занятость",
            "address": "Алматы, улица Мынбаева, 151",
            "currency": "KZT"
        }]


@pytest.fixture()
def vacancy():
    return Vacancy("Android Middle / Senior разработчик мобильных "
                   "приложений",
                   "https://hh.ru/vacancy/96970412",
                   250000,
                   600000,
                   "Требуемый опыт работы: не менее 1 года. "
                   "Знание <highlighttext>Python</highlighttext>-telegram-bot "
                   "и Django. Базовое знакомство с Docker и Nginx. ",
                   "Информация не указана",
                   "2024-04-21T13:46:04+0300",
                   "Полная занятость",
                   "Ташкент, улица Садыка Азимова, 68",
                   "UZS"
                   )


@pytest.fixture()
def vacancy2():
    return [{
        "name": "Android Middle / Senior разработчик мобильных приложений",
        "link_to_vacancy": "https://hh.ru/vacancy/96970412",
        "salary_min": 10000000,
        "salary_max": 0,
        "requirement": "Требуемый опыт работы: не менее 1 года. "
                       "Знание "
                       "<highlighttext>Python</highlighttext>-telegram-bot "
                       "и Django. Базовое знакомство с Docker и Nginx. ",
        "responsibility": "Информация не указана",
        "publication_date": "15.04.2024 08:26",
        "employment": "Полная занятость",
        "address": "Ташкент, улица Садыка Азимова, 68",
        "currency": "UZS"
    }]