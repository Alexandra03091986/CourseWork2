from typing import List, Dict, Any

import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для работы с API сервисов с вакансиями"""

    @abstractmethod
    def _connecting(self) -> bool:
        """ Установка соединения с API"""
        pass

    @abstractmethod
    def load_vacancies(self, query:str, **kwargs) -> List[Dict[str, Any]]:
        """Получение списка вакансий по поисковому запросу"""
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__base_url = 'https://api.hh.ru/vacancies'
        self.connected = False
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def _connecting(self) -> bool:
        """ Установка соединения с API"""
        try:
            response = requests.get(self.__base_url, params=self.__params, timeout=5)
            self.connected = response.status_code == 200
            return self.connected
        except requests.exceptions.RequestException:
            self.connected = False
            return False

    def load_vacancies(self, query:str, **kwargs) -> list[Any] | None:
        """Получение списка вакансий по поисковому запросу"""

        # Проверяем подключение перед получением данных
        if not self._connecting():
            print("Ошибка: не получилось подключиться к API")
            return []

        self.__params['text'] = query
        self.__params['page'] = 0
        self.__vacancies = []

        try:
            while self.__params.get('page') != 20:
                response = requests.get(self.__base_url, params=self.__params, timeout=5)
                vacancies_data = response.json()
                vacancies = vacancies_data.get('items', [])

                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при загрузке: {e}")
            return []
        return self.__vacancies
