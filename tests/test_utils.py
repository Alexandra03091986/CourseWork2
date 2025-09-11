from unittest.mock import patch

from src.utils import get_filtered_by_keyword, get_filtered_by_city, get_sort_vacancies, print_vacancies
from src.vacancy import Vacancy


def test_filtered_by_keyword(vacancies_for_filter):
    result = get_filtered_by_keyword(vacancies_for_filter, "Стрессоустойчивость")
    assert len(result) == 2


def test_filtered_by_city(vacancies_for_filter):
    result = get_filtered_by_city(vacancies_for_filter, "Алматы")
    assert len(result) == 1


def test_sort_vacancies_normal_input(vacancies_for_filter):
    with patch('builtins.input', return_value='3'):
        result = get_sort_vacancies(vacancies_for_filter)
        assert len(result) == 3
        assert result[0].salary == 280000
        assert result[1].salary == 80000
        assert result[2].salary == 3000


def test_sort_vacancies_positive_number():
    with patch('builtins.input', side_effect=['-2', '1']):
       test_vacancy = Vacancy("Специалист по кадрам", 3000, "Минск", "Личные качества: Стрессоустойчивость, коммуникабельность, ответственность.", "https://hh.ru/vacancy/125033362")
       result = get_sort_vacancies([test_vacancy])
       assert len(result) == 1
       assert result[0].salary == 3000


def test_sort_vacancies_normal_not_number(vacancies_for_filter):
    with patch('builtins.input', side_effect=['asf', '2']):
        result = get_sort_vacancies(vacancies_for_filter)
        assert len(result) == 2
        assert result[0].salary == 280000


def test_print_vacancies():
    print_vacancies([Vacancy("Тест", 1000, "Москва", "хороший работник", "https://hh.ru/vacancy/124412668")])
    print("Функция работает без ошибок")
