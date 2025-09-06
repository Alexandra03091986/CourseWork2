from src.api_parser import HeadHunterAPI
from src.file_worker import JsonFileWorker
from src.vacancy import Vacancy

from src.api_parser import HeadHunterAPI
from src.vacancy import Vacancy
from src.file_worker import JsonFileWorker


def main():
    print("=== Система работы с вакансиями ===\n")

    # 1. Получаем вакансии с HH
    print("1. Получение вакансий с HeadHunter...")
    hh_api = HeadHunterAPI()
    hh_data = hh_api.load_vacancies("крановщик")

    if not hh_data:
        print("Не удалось получить данные с API")
        return

    print(f"Получено {len(hh_data)} вакансий с API")

    # 2. Преобразуем в объекты
    print("2. Преобразование в объекты Vacancy...")
    vacancies = Vacancy.cast_to_object_list(hh_data)
    print(f"Создано {len(vacancies)} объектов")

    # 3. Сохраняем в файл
    print("3. Сохранение в JSON файл...")
    storage = JsonFileWorker()

    for vacancy in vacancies:
        storage.add_vacancy(vacancy.to_dict())

    # 4. Читаем из файла и выводим
    print("4. Чтение из файла и вывод результатов...\n")
    saved_vacancies = storage.get_all_vacancies()

    print(f"Всего сохранено вакансий: {len(saved_vacancies)}")
    print("\nПервые 5 вакансий:")
    print("-" * 50)

    for i, vac in enumerate(saved_vacancies[:5], 1):
        vacancy_obj = Vacancy(
            vac['name'],
            vac['salary'],
            vac['city'],
            vac['requirements'],
            vac['url']
        )
        print(f"Вакансия #{i}:")
        print(vacancy_obj)
        print("-" * 50)

    # 5. Демонстрация поиска
    print("\n5. Поиск вакансий в Москве:")
    moscow_vacancies = storage.get_vacancies(city="Москва")
    print(f"Найдено {len(moscow_vacancies)} вакансий в Москве")

    # 6. Демонстрация сравнения вакансий
    if len(vacancies) >= 2:
        print("\n6. Сравнение вакансий по зарплате:")
        print(f"Вакансия 1: {vacancies[0].name} - {vacancies[0].salary}")
        print(f"Вакансия 2: {vacancies[1].name} - {vacancies[1].salary}")

        if vacancies[0] > vacancies[1]:
            print("Первая вакансия имеет большую зарплату")
        elif vacancies[0] < vacancies[1]:
            print("Вторая вакансия имеет большую зарплату")
        else:
            print("Зарплаты равны")


if __name__ == "__main__":
    main()
# # Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()
# 
# # Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.load_vacancies("Python")
# 
# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
# 
# # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
# 
# # Сохранение информации о вакансиях в файл
# json_saver = JsonFileWorker()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)

# def user_interaction():
#     platforms = ["HeadHunter"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
#
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()
