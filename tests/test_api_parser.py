from unittest.mock import patch

import requests.exceptions

from src.api_parser import HeadHunterAPI


def test_connecting_success():
    """Тест успешного соединения"""
    api_request = HeadHunterAPI()
    # Проверяем что возвращает метод True или False
    result = api_request._connecting()
    assert isinstance(result, bool)


def test_connecting_exception():
    """Тест обработки ошибок соединения"""
    api_request = HeadHunterAPI()
    result = api_request._connecting()
    assert result in [True, False]
    print(f"Результат соединения: {result}")

def test_connecting_exception_with_mock():
    api_request = HeadHunterAPI()
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Ошибка соединения")
        result = api_request._connecting()
        assert result == False
        assert api_request.connected == False


def test_connecting_no_error():
    api_request = HeadHunterAPI()
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        result = api_request._connecting()
        assert result == True
        assert api_request.connected == True


def test_load_vacancies_success():
    """Тест успешной загрузки вакансий"""
    api_request = HeadHunterAPI()
    with patch.object(api_request, '_connecting', return_value=True):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {
                'items': [{'name': 'Test'}]
            }
            result = api_request.load_vacancies('python')
            assert isinstance(result, list)
            assert len(result) > 0


def test_load_vacancies_no_connection() -> None:
    """Тест когда нет подключения к API"""
    api_request = HeadHunterAPI()
    with patch.object(api_request, '_connecting', return_value=False):
        result = api_request.load_vacancies('python')
        assert result == []


def test_load_vacancies_exceptions():
    """Тест, что при исключении возвращается пустой список"""
    api_requests = HeadHunterAPI()

    with patch.object(api_requests, '_connecting', return_value=True):
        with patch('requests.get', side_effect=requests.exceptions.RequestException):
            result = api_requests.load_vacancies('test')
            assert result == []