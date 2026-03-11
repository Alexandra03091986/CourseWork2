from src.api_parser import HeadHunterAPI
from src.file_worker import JsonFileWorker
from src.utils import get_filtered_by_city, get_filtered_by_keyword, get_sort_vacancies, print_vacancies
from src.vacancy import Vacancy


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""
    platforms = ["HeadHunter"]
    print(f"=== Система поиска вакансий на {platforms} ===\n")

    # 1 Получаем вакансии с HH
    search_query = input("1. Введите профессию для поиска: ")
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.load_vacancies(search_query)

    if not hh_vacancies:
        print("Не удалось найти вакансии")
        return

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(f"Найдено {len(vacancies_list)} вакансий")

    #  Сохранение информации о вакансиях в файл
    json_saver = JsonFileWorker()
    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy.to_dict())

    # 2 Поиск по слову
    keyword = input("\n2. Введите ключевое слово для поиска в описании: ")
    filtered_by_keyword = get_filtered_by_keyword(vacancies_list, keyword)

    # 3. Фильтр по городу
    city = input("\n3. Введите город для фильтрации: ")
    filtered_by_city = get_filtered_by_city(filtered_by_keyword, city)

    # 4 Сортируем и берем top N
    top_vacancies = get_sort_vacancies(filtered_by_city)
    print(f"\n🎯 ИТОГОВЫЙ СПИСОК ({len(top_vacancies)} вакансий):")

    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
