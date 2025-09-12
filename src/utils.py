from typing import List

from src.vacancy import Vacancy


def get_filtered_by_keyword(vacancies_list: List[Vacancy], keyword: str) -> List[Vacancy]:
    """
    Фильтрует вакансии по ключевому слову в описании требований
    vacancies_list: Список вакансий для фильтрации
    keyword: Ключевое слово для поиска в требованиях
    return: Отфильтрованный список вакансий, содержащих ключевое слово
    """
    filtered_by_keyword = []
    for vacancy in vacancies_list:
        if vacancy.requirements and keyword.lower() in vacancy.requirements.lower():
            filtered_by_keyword.append(vacancy)

    print(f"После фильтра по слову '{keyword}': {len(filtered_by_keyword)} вакансий")
    return filtered_by_keyword


def get_filtered_by_city(filtered_by_keyword: List[Vacancy], city: str) -> List[Vacancy]:
    """
    Фильтрует вакансии по названию города
    filtered_by_keyword: Список вакансий, уже отфильтрованных по ключевому слову
    city: Название города для фильтрации
    return: Отфильтрованный список вакансий в указанном городе
    """
    filtered_by_city = []

    for vacancy in filtered_by_keyword:
        if vacancy.city and city.lower() in vacancy.city.lower():
            filtered_by_city.append(vacancy)

    print(f"После фильтра по городу '{city}': {len(filtered_by_city)} вакансий")
    return filtered_by_city


def get_sort_vacancies(filtered_by_city: List[Vacancy]) -> List[Vacancy]:
    """
    Сортирует вакансии по зарплате и возвращает топ N вакансий.
    Запрашивает у пользователя количество вакансий с проверкой ввода.
    :filtered_by_city: Список вакансий, отфильтрованных по городу
    :return: Топ N вакансий, отсортированных по зарплате (по убыванию)
    """
    while True:
        try:
            quantity_input = input("\n4. Введите количество вакансий для вывода в топ N: ")
            quantity_vacancies = int(quantity_input)

            if quantity_vacancies <= 0:
                print("❌ Число должно быть положительным!")
                continue

            sorted_by_salary = sorted(filtered_by_city, reverse=True)
            top_vacancies = sorted_by_salary[:quantity_vacancies]
            print(f"\nТоп {quantity_vacancies} по зарплате:")
            return top_vacancies

        except ValueError:
            print("❌ Нужно ввести число! Попробуйте снова.")


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """
    Выводит отформатированную информацию о вакансиях.
    :vacancies: Список объектов Vacancy для вывода
    """
    for vac in vacancies:
        print(vac)
        print("-" * 50)
