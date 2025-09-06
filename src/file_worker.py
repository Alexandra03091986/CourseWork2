import json
import os.path
from abc import ABC, abstractmethod


class FileWorker(ABC):
    """" Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy) -> None:
        """Добавить вакансию в хранилище"""
        ...

    @abstractmethod
    def get_vacancies(self, **criteria) -> list:
        """Получить вакансии по критериям"""
        ...

    @abstractmethod
    def delete_vacancy(self, vacancy_id: str) -> None:
        """Удалить вакансию по ID"""
        ...

    @abstractmethod
    def get_all_vacancies(self) -> list:
        """Получить все вакансии"""
        ...

class JsonFileWorker(FileWorker):
    """Класс для работы с файлами Json"""

    def __init__(self, filename: str = "../data/vacancies.json"):
        self.__filename = filename
        self._file_exists()

    def _file_exists(self) -> None:
        """Создать файл если его нет"""
        if not os.path.exists(self.__filename):
            with open(self.__filename, 'w', encoding='utf-8') as file:
                json.dump([], file)


    def _read_file(self) -> list:
        """Прочитать данные из файла"""
        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _write_file(self, data: list) -> None:
        """Записывает данные в файл"""
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def _is_duplicate(self, new_vacancy: dict, existing_vacancies: list) -> bool:
        """Проверяет, есть ли уже такая вакансия"""
        for vacancy in existing_vacancies:
            # Сравниваем по основным полям для избежания дублей
            if (vacancy.get('name') == new_vacancy.get('name') and
                    vacancy.get('url') == new_vacancy.get('url') and
                    vacancy.get('city') == new_vacancy.get('city')):
                return True
        return False

    def add_vacancy(self, vacancy: dict) -> None:
        """Добавить вакансию в JSON-файл (без дубликатов)"""
        data = self._read_file()

        # Проверяем на дубликаты
        if not self._is_duplicate(vacancy, data):
            data.append(vacancy)
            self._write_file(data)

    def get_vacancies(self, **criteria) -> list:
        """Получить вакансии по критериям из JSON-файла"""
        data = self._read_file()

        if not criteria:  # Если критерии не указаны, возвращаем все
            return data

        result = []
        for vacancy in data:
            match = True
            for key, value in criteria.items():
                if vacancy.get(key) != value:
                    match = False
                    break
            if match:
                result.append(vacancy)

        return result

    def delete_vacancy(self, vacancy_id: str) -> None:
        """Удалить вакансию по ID из JSON-файла"""
        data = self._read_file()
        # Ищем по разным возможным полям ID
        data = [v for v in data if v.get('id') != vacancy_id and v.get('url') != vacancy_id]
        self._write_file(data)

    def get_all_vacancies(self) -> list:
        """Получить все вакансии из JSON-файла"""
        return self._read_file()


# Пример использования
if __name__ == "__main__":
    # Создаем хранилища с разными именами файлов
    json_storage = JsonFileWorker("../data/my_vacancies.json")

    # Пример вакансии
    vacancy_data = {
        'id': 'hh_12345',
        'name': 'Python Developer',
        'salary': 100000,
        'city': 'Москва',
        'requirements': 'Опыт работы 3 года',
        'url': 'https://hh.ru/vacancy/12345'
    }

    # Добавляем в оба хранилища (дубликаты не добавятся)
    json_storage.add_vacancy(vacancy_data)

    # Пробуем добавить дубликат (не добавится)
    json_storage.add_vacancy(vacancy_data)

    # Получаем данные по критериям
    python_vacancies = json_storage.get_vacancies(name='Python Developer')
    print(f"Найдено {len(python_vacancies)} вакансий Python Developer")

    # Получаем все вакансии
    all_vacancies = json_storage.get_all_vacancies()
    print(f"Всего вакансий в JSON: {len(all_vacancies)}")

    # Удаляем вакансию
    json_storage.delete_vacancy('hh_12345')