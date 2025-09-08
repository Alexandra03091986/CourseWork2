import pytest

from src.vacancy import Vacancy


@pytest.fixture
def info_vacancies() -> Vacancy:
    """Пример вакансии для тестов"""
    return Vacancy("Офис-менеджер", 250000, "Алматы", "Желательно высшее образование. Опыт работы на...", "https://hh.ru/vacancy/123923267")


@pytest.fixture
def info_vacancies_1() -> Vacancy:
    """Пример вакансии для тестов"""
    return Vacancy("Семейный водитель", 600000, "Алматы", "Рассматриваются только профессиональные автомобилисты...", "https://hh.ru/vacancy/124733111")


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
def info_vacancies_salary_zero():
    """Пример вакансии с зарплатой None"""
    return Vacancy(
        "Фронтенд-разработчик",
        None,
        "Протвино (Московская область)",
        "Профильное высшее образование. Знание фундаментальных....",
        "https://hh.ru/vacancy/125063056"
    )


@pytest.fixture
def info_vacancies_salary_from():
    return Vacancy(
        "Оператор ПК, Бухгалтер на первичную документацию",
        {"from": 1800},
        "Гатово",
        "Уверенный пользователь ПК. Аналитический склад ума и умение...",
        "https://hh.ru/vacancy/124760695"
    )


@pytest.fixture
def info_vacancies_salary_to():
    return Vacancy(
        "Оператор ПК, Бухгалтер на первичную документацию",
        {"to": 15000},
        "Гатово",
        "Уверенный пользователь ПК. Аналитический склад ума и умение...",
        "https://hh.ru/vacancy/124760695"
    )


@pytest.fixture
def info_vacancies_salary_from_to():
    return Vacancy(
        "Младший специалист (Канада)",
        {"from": None, "to": None},
        "Канада",
        "Коммуникабельных людей.  Опыт работы не менее 2 лет....",
        "https://hh.ru/vacancy/124824193"
    )


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
def vacancies_magical_method():
    return [
        {
            "name": "Офис-менеджер",
            "salary": 250000,
            "city": "Алматы",
            "requirements": "Желательно высшее образование. Опыт работы на позиции офис-менеджера/администратора от 6 месяцев. Уверенный пользователь ПК и офисных программ.",
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
            "requirements": "Коммуникабельность. Пунктуальность. Обучаемость.",
            "url": "https://hh.ru/vacancy/124970937"
        }
    ]
