from typing import Any

import pytest

from src.vacancy import Vacancy


@pytest.fixture
def info_vacancies() -> Vacancy:
    """Пример вакансии для тестов"""
    return Vacancy(
        "Офис-менеджер",
        250000,
        "Алматы",
        "Желательно высшее образование. Опыт работы на...",
        "https://hh.ru/vacancy/123923267"
    )


@pytest.fixture
def info_vacancies_1() -> Vacancy:
    """Пример вакансии для тестов"""
    return Vacancy(
        "Семейный водитель",
        600000,
        "Алматы",
        "Рассматриваются только профессиональные автомобилисты...",
        "https://hh.ru/vacancy/124733111"
    )


@pytest.fixture
def info_vacancies_2() -> Vacancy:
    """Пример вакансии для тестов"""
    return Vacancy(
        "Специалист по прогулкам",
        80111,
        "Ставрополь",
        "Быстрый старт карьеры без опыта!",
        "https://hh.ru/vacancy/123486611")


@pytest.fixture
def info_vacancies_salary_none() -> Vacancy:
    """Пример вакансии с зарплатой None"""
    return Vacancy(
        "Фронтенд-разработчик",
        None,
        "Протвино (Московская область)",
        "Профильное высшее образование. Знание фундаментальных....",
        "https://hh.ru/vacancy/125063056"
    )


@pytest.fixture
def info_vacancies_salary_zero() -> Vacancy:
    """Пример вакансии с зарплатой None"""
    return Vacancy(
        "Фронтенд-разработчик",
        "",
        "Протвино (Московская область)",
        "Профильное высшее образование. Знание фундаментальных....",
        "https://hh.ru/vacancy/125063056"
    )


@pytest.fixture
def info_vacancies_salary_from() -> Vacancy:
    """
    Фикстура предоставляет тестовый объект Vacancy с указанием зарплаты 'from'.
    """
    return Vacancy(
        "Оператор ПК, Бухгалтер на первичную документацию",
        {"from": 1800},
        "Гатово",
        "Уверенный пользователь ПК. Аналитический склад ума и умение...",
        "https://hh.ru/vacancy/124760695"
    )


@pytest.fixture
def info_vacancies_salary_to() -> Vacancy:
    """
    Фикстура предоставляет тестовый объект Vacancy с указанием зарплаты 'to'.
    """
    return Vacancy(
        "Оператор ПК, Бухгалтер на первичную документацию",
        {"to": 15000},
        "Гатово",
        "Уверенный пользователь ПК. Аналитический склад ума и умение...",
        "https://hh.ru/vacancy/124760695"
    )


@pytest.fixture
def info_vacancies_salary_from_to() -> Vacancy:
    """
    Фикстура предоставляет тестовый объект Vacancy с указанием зарплаты 'from' и 'to'.
    """
    return Vacancy(
        "Младший специалист (Канада)",
        {"from": None, "to": None},
        "Канада",
        "Коммуникабельных людей.  Опыт работы не менее 2 лет....",
        "https://hh.ru/vacancy/124824193"
    )


@pytest.fixture
def vacancies_requirements_and_clean() -> Vacancy:
    """Пример вакансии для тестов"""
    return Vacancy(
        "Специалист по прогулкам",
        80111,
        "Ставрополь",
        "",
        "https://hh.ru/vacancy/123486611")


@pytest.fixture
def vacancies_to_dict() -> dict:
    """Пример вакансии для тестов - словарь для создания объекта класса Vacancy"""
    return {
        "name": "Офис-менеджер",
        "salary": 250000,
        "city": "Алматы",
        "requirements": "Желательно высшее образование. Опыт работы на...",
        "url": "https://hh.ru/vacancy/123923267"
    }


@pytest.fixture
def vacancies_magical_method() -> list[dict[str, Any]]:
    """Фикстура представляет тестовые данные вакансий для тестирования магических методов"""
    return [
        {
            "name": "Офис-менеджер",
            "salary": 250000,
            "city": "Алматы",
            "requirements": "Желательно высшее образование. Опыт работы на позиции...",
            "url": "https://hh.ru/vacancy/123923267"
        },
        {
            "name": "Специалист по прогулкам",
            "salary": 80111,
            "city": "Ставрополь",
            "requirements": "Быстрый старт карьеры без опыта!",
            "url": "https://hh.ru/vacancy/123486611"
        },
        {
            "name": "Администратор на ресепшен",
            "salary": 250000,
            "city": "Астана",
            "requirements": "Коммуникабельность. Пунктуальность. Обучаемость...",
            "url": "https://hh.ru/vacancy/124970937"
        }
    ]


@pytest.fixture
def vacancies_for_filter() -> list[Vacancy]:
    """Фикстура представляет тестовые данные вакансий для фильтрации"""
    return [
        Vacancy(
            "Водитель легкового автомобиля для руководителя",
            80000,
            "Тюмень",
            "Не менее 3-х лет работы водителем руководителя. Открытая категория В. Без фото резюме НЕ...",
            "https://hh.ru/vacancy/124985030"
        ),
        Vacancy(
            "Специалист по кадрам",
            3000,
            "Минск",
            "Личные качества: Стрессоустойчивость, коммуникабельность, ответственность.",
            "https://hh.ru/vacancy/125033362"
        ),
        Vacancy(
            "Администратор",
            280000,
            "Алматы",
            "Навыки управления коллективом. Ответственность, коммуникабельность, стрессоустойчивость...",
            "https://hh.ru/vacancy/124464875"
        )
    ]


@pytest.fixture
def json_file_worker_init() -> list[dict[str, Any]]:
    """Фикстура представляет тестовые данные вакансий для JsonFileWorker"""
    return [
        {
            "name": "Финансовый директор (CFO)",
            "salary": 400000,
            "city": "Москва",
            "requirements": "Команда проекта имеет успешный практический опыт реализации масштабных...",
            "url": "https://hh.ru/vacancy/125038694"
        },
        {
            "name": "Стюард-официант на скоростной поезд Сапсан",
            "salary": 86000,
            "city": "Россия",
            "requirements": "Рассматриваем кандидатов без опыта работы, если вы готовы обучаться...",
            "url": "https://hh.ru/vacancy/124874334"
        },
        {
            "name": "Водитель (В,С)",
            "salary": 150000,
            "city": "Уфа",
            "requirements": "Хорошее знание ПДД. Наличие удостоверения категории В,С.",
            "url": "https://hh.ru/vacancy/124990352"
        }
    ]
