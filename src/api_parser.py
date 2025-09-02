import requests
from abc import ABC, abstractmethod



class Parser(ABC):
    """Абстрактный класс для работы с API сервисов с вакансиями"""
    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def connecting(self) -> bool:
        """ Установка соединения с API"""
        pass

    @abstractmethod
    def load_vacancies(self, query:str, **kwargs):
        """Получение списка вакансий по поисковому запросу"""
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    def __init__(self, file_worker):
        self.base_url = 'https://api.hh.ru/vacancies/'
        self.connected = False
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def connecting(self) -> bool:
        """ Установка соединения с API"""
        try:
            response = requests.get(f"{self.base_url}", params={"text": "test", "per_page": 100})
            if response.status_code == 200:
                self.connected = True
                return True
            else:
                self.connected = False
                return False
        except requests.exceptions.RequestException:
                self.connected = False
                return False


    def load_vacancies(self, query:str, **kwargs):
        """Получение списка вакансий по поисковому запросу"""

        self.params['text'] = query
        while self.params.get('page') != 20:
            response = requests.get(self.base_url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


hh = HeadHunterAPI()
print("Проверяем подключение...")
if hh.connecting():
    print("Успешное подключение!")

    vacancies = hh.load_vacancies("Python", per_page=3)
    print(f"Найдено вакансий: {len(vacancies)}")

    for vac in vacancies:
        print(f"- {vac.get('name')}")
else:
    print("Не удалось подключиться")
