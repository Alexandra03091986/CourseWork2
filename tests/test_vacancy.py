from src.vacancy import Vacancy


def test_vacancies_init(info_vacancies) -> None:
    """Проверка инициализации Vacancy"""
    assert info_vacancies.name == "Офис-менеджер"
    assert info_vacancies.salary == 250000
    assert info_vacancies.city == "Алматы"
    assert info_vacancies.requirements == "Желательно высшее образование. Опыт работы на..."
    assert info_vacancies.url == "https://hh.ru/vacancy/123923267"


def test_vacancies_to_dict(vacancies_to_dict, info_vacancies) -> None:
    """Тест преобразования в словарь"""
    result = info_vacancies.to_dict()
    assert result == vacancies_to_dict


def test_vacancies_str(info_vacancies):
    """Тестирует строковое представление вакансии"""
    assert str(info_vacancies) == ("Вакансия: Офис-менеджер\n"
                                   "Зарплата: 250000 руб.\n"
                                   "Город: Алматы\n"
                                   "Требования: Желательно высшее образование. Опыт работы на......\n"
                                   "Подробнее по ссылке: https://hh.ru/vacancy/123923267")


def test_eq_(vacancies_magical_method, info_vacancies, info_vacancies_1):
    assert vacancies_magical_method[0]['salary'] == vacancies_magical_method[2]['salary']
    assert not (vacancies_magical_method[0]['salary'] == vacancies_magical_method[1]['salary'])
    assert not (vacancies_magical_method[1]['salary'] == vacancies_magical_method[2]['salary'])
    result = info_vacancies.__eq__("не вакансия")
    assert result is NotImplemented
    assert not (info_vacancies == info_vacancies_1)


def test_lt_(info_vacancies_1, info_vacancies):
    assert info_vacancies < info_vacancies_1
    assert not (info_vacancies_1 < info_vacancies)
    result = info_vacancies.__lt__("не вакансия")
    assert result is NotImplemented


def test_gt_(info_vacancies_1, info_vacancies):
    assert info_vacancies_1 > info_vacancies
    assert not (info_vacancies > info_vacancies_1)
    result = info_vacancies.__gt__("не вакансия")
    assert result is NotImplemented


def test_repr_(info_vacancies_2):
    result = info_vacancies_2.__repr__()
    assert "Специалист по прогулкам" in result
    assert "80111 руб." in result


def test_validate_salary_none(info_vacancies_salary_none):
    assert info_vacancies_salary_none.salary == 0


def test_validate_salary_zero(info_vacancies_salary_zero):
    assert info_vacancies_salary_zero.salary == 0


def test_validate_salary_from(info_vacancies_salary_from):
    assert info_vacancies_salary_from.salary == 1800


def test_validate_salary_to(info_vacancies_salary_to):
    assert info_vacancies_salary_to.salary == 15000


def test_vacancies_salary_from_to(info_vacancies_salary_from_to):
    assert info_vacancies_salary_from_to.salary == 0


def test_vacancies_salaty(info_vacancies):
    assert info_vacancies.salary == 250000


def test_validate_salary_zero_():
    """Тест: ноль"""
    vacancy = Vacancy("Test", 0, "City", "Req", "http://test.com")
    assert vacancy.salary == 0


def test_validate_requirements_and_clean(vacancies_requirements_and_clean):
    assert vacancies_requirements_and_clean.requirements == "Требования не указаны"
    vacancy = Vacancy("Test", 0, "City", None, "http://test.com")
    assert vacancy.requirements == "Требования не указаны"


def test_cast_simple():
    """Тестирование создания из данных"""
    # Минимальные данные
    simple_data = [{
        'name': 'Тест',
        'salary': {'from': 50000},
        'area': {'name': 'Город'},
        'snippet': {'requirement': 'Требования'},
        'alternate_url': 'http://test.com'
    }]

    vacancies = Vacancy.cast_to_object_list(simple_data)

    assert vacancies[0].name == "Тест"


def test_cast_no_salary():
    """Тест: нет зарплаты"""
    test_data = [{
        'name': 'Developer',
        'salary': None,
        'area': {'name': 'СПб'},
        'snippet': {'requirement': 'Опыт'},
        'alternate_url': 'https://hh.ru/vacancy/456'
    }]

    vacancies = Vacancy.cast_to_object_list(test_data)
    assert vacancies[0].salary == 0
