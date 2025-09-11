import json
import os.path

from src.file_worker import JsonFileWorker


def test_json_file_worker_init(json_file_worker_init):
    """Проверка инициализации JsonFileWorker"""
    assert len(json_file_worker_init) > 0
    assert 'name' in json_file_worker_init[0]
    assert 'salary' in json_file_worker_init[0]
    assert 'city' in json_file_worker_init[0]
    assert 'requirements' in json_file_worker_init[0]
    assert 'url' in json_file_worker_init[0]


def test_file_exists_false():
    assert os.path.exists('file.json') == False


def test_file_exists(tmp_path):
    """Тест на проверку создания файла"""
    test_file = tmp_path / "vacancies.json"
    # Проверяем, что файла нет
    assert not test_file.exists()

    file_work = JsonFileWorker(test_file)
    file_work._file_exists()
    # Проверяем создание файла
    assert test_file.exists()


def test_read_file():
    """Проверяет работу метода"""
    worker = JsonFileWorker("test_file.json")
    result = worker._read_file()
    assert isinstance(result, list)


def test_read_file_not_found_error(tmp_path):
    """Тест обработки FileNotFoundError"""
    test_file = tmp_path / "not_exists.json"
    worker = JsonFileWorker(test_file)
    result = worker._read_file()
    assert result == []


def test_read_file_json_decode_error(tmp_path):
    """Тест обработки JSONDecodeError"""
    # Создаем файл с broken JSON
    test_file = tmp_path / "test_file.json"
    # Создаем файл с broken JSON обычным способом
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("{invalid json")

    worker = JsonFileWorker(test_file)
    result = worker._read_file()
    assert result == []


def test_read_file_errors():
    """Тест ошибок чтения"""
    # Проверяем, что при ошибках возвращается пустой список
    worker = JsonFileWorker("nonexistent_file.json")
    result = worker._read_file()
    assert result == []
    # Очистка
    if os.path.exists("nonexistent_file.json"):
        os.remove("nonexistent_file.json")


def test_write_file(tmp_path):
    test_file = tmp_path / "test_file.json"
    worker = JsonFileWorker(test_file)
    test_data = [{"name": "Финансовый директор (CFO)", "salary": 400000,
    "city": "Москва"}]
    worker._write_file(test_data)
    # Проверяем что файл создался и содержит правильные данные
    assert test_file.exists()
    with open(test_file, 'r', encoding="utf-8") as file:
        content = json.load(file)
        assert content == test_data
    # Очистка
    if os.path.exists("test_file.json"):
        os.remove("test_file.json")


def test_is_duplicate_true():
    """Тест проверяет, является ли вакансия дубликатом"""
    worker = JsonFileWorker("test_file.json")
    vacancies = [{"name": "Pyton Developer", "city": "Москва", "url": "https://hh.ru/vacancy/124990352"},
                 {"name": "Java Developer", "city": "СПб", "url": "https://hh.ru/vacancy/124874334"}
                 ]
    new_vacancies = {"name": "Pyton Developer", "city": "Москва", "url": "https://hh.ru/vacancy/124990352"}
    result = worker._is_duplicate(new_vacancies, vacancies)
    assert result == True


def test_is_duplicate_false():
    """Тест проверяет, что вакансия не является дубликатом"""
    worker = JsonFileWorker("test_file.json")
    vacancies = [{"name": "Pyton Developer", "city": "Москва", "url": "https://hh.ru/vacancy/124990352"}]
    new_vacancies = {"name": "Java Developer", "city": "СПб", "url": "https://hh.ru/vacancy/124874334"}
    result = worker._is_duplicate(new_vacancies, vacancies)
    assert result == False


def test_add_vacancy():
    """Тест добавляет новые вакансии"""
    worker = JsonFileWorker("test_file.json")
    vacancy = {"name": "Pyton Developer", "city": "Москва", "url": "https://hh.ru/vacancy/124990352"}
    worker.add_vacancy(vacancy)
    # Проверяем, что вакансия добавилась
    data = worker._read_file()
    assert len(data) == 1
    assert data[0] == vacancy


def test_add_vacancy_duplicate():
    """Тест на не добавление дубликатов"""
    worker = JsonFileWorker("test_file_add_not_duplicate.json")
    vacancy = {"name": "Pyton Developer", "url": "https://hh.ru/vacancy/124990352", "city": "Москва"}
    # Добавляем первый раз
    worker.add_vacancy(vacancy)
    # Добавляем второй раз (дубликат)
    worker.add_vacancy(vacancy)
    # проверяем количество вакансий (должна быть одна)
    data = worker._read_file()
    assert len(data) == 1
    # Очистка
    if os.path.exists("test_file_add_not_duplicate.json"):
        os.remove("test_file_add_not_duplicate.json")

def test_get_vacancies_not_criteria():
    worker = JsonFileWorker("test_file.json")
    vacancy = [{"name": "Pyton Developer", "city": "Москва", "url": "https://hh.ru/vacancy/124990352"},
               {"name": "Java Developer", "city": "СПб", "url": "https://hh.ru/vacancy/124874334"}
               ]
    worker._write_file(vacancy)
    result = worker.get_vacancies()
    assert result == vacancy
    # Очистка
    if os.path.exists("test_file.json"):
        os.remove("test_file.json")


def test_get_vacancies_by_criteria():
    """Тест фильтрации по критериям"""
    worker = JsonFileWorker("test_file.json")
    vacancy = [{"name": "Pyton Developer", "salary": 100, "city": "Москва", "url": "https://hh.ru/vacancy/124990352"},
               {"name": "Java Developer", "salary": 200, "city": "СПб", "url": "https://hh.ru/vacancy/124874334"}
               ]
    worker._write_file(vacancy)
    result = worker.get_vacancies(city="Москва")
    assert len(result) == 1
    # Ищем по критерию, которого нет
    result = worker.get_vacancies(city="Тюмень")
    assert result == []
    # Ищу по двум критериям
    result = worker.get_vacancies(name="Pyton Developer", city="Москва")
    assert result[0]['salary'] == 100
    # Очистка
    if os.path.exists("test_file.json"):
        os.remove("test_file.json")


def test_delete_vacancy_by_id():
    """Тест удаления вакансии по ID"""
    worker = JsonFileWorker("test_file.json")
    vacancy = [{"id": "123", "name": "Pyton Developer", "salary": 100, "city": "Москва", "url": "https://hh.ru/vacancy/124990352"},
               {"id": "456", "name": "Java Developer", "salary": 200, "city": "СПб", "url": "https://hh.ru/vacancy/124874334"}
               ]
    worker._write_file(vacancy)
    # Удаляем вакансии по ID "123"
    worker.delete_vacancy("123")
    # проверяем, что осталась одна вакансия
    result = worker._read_file()
    assert len(result) == 1
    assert result[0]["id"] == "456"
    # Очистка
    if os.path.exists("test_file.json"):
        os.remove("test_file.json")


def test_delete_vacancy_by_alternate_url():
    """Тест удаления вакансии по alternate_url"""
    worker = JsonFileWorker("test_file.json")
    vacancy = [{"id": "123", "name": "Pyton Developer", "salary": 100, "city": "Москва", "alternate_url": "https://hh.ru/vacancy/124990352"},
               {"id": "456", "name": "Java Developer", "salary": 200, "city": "СПб", "alternate_url": "https://hh.ru/vacancy/124874334"}
               ]
    worker._write_file(vacancy)
    # Удаляем вакансии по alternate_url
    worker.delete_vacancy("https://hh.ru/vacancy/124990352")
    # проверяем, что осталась одна вакансия
    result = worker._read_file()
    assert len(result) == 1
    assert result[0]["alternate_url"] == "https://hh.ru/vacancy/124874334"
    # Очистка
    if os.path.exists("test_file.json"):
        os.remove("test_file.json")


def test_get_all_vacancies():
    """Тест удаления вакансии по ID"""
    worker = JsonFileWorker("test_file.json")
    vacancy = [{"id": "123", "name": "Pyton Developer", "salary": 100, "city": "Москва", "url": "https://hh.ru/vacancy/124990352"},
               {"id": "456", "name": "Java Developer", "salary": 200, "city": "СПб", "url": "https://hh.ru/vacancy/124874334"}
               ]
    worker._write_file(vacancy)
    result = worker.get_all_vacancies()
    assert len(result) == 2
    # Очистка
    if os.path.exists("test_file.json"):
        os.remove("test_file.json")
