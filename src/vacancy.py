import re
from typing import Any, Dict, List, Union


class Vacancy:
    """Класс для представления вакансии с валидацией данных."""
    # Используем __slots__ для экономии памяти
    __slots__ = ('name', 'salary', 'city', 'requirements', 'url')

    def __init__(
            self,
            name: str,
            salary: Union[int, None, Dict[str, Any], str],
            city: str,
            requirements: str | None,
            url: str
    ) -> None:
        """
        Инициализация вакансии
        name: Название вакансии
        url: Ссылка на вакансию
        salary: Зарплата (может быть None)
        city: Название города
        requirements: Требования
       """
        self.name = name
        self.salary = self._validate_salary(salary)
        self.city = city
        self.requirements = self._validate_requirements_and_clean(requirements)
        self.url = url

    def _validate_salary(
            self,
            salary: Union[int, None, Dict[str, Any], str]
    ) -> int:
        """
        Метод для валидации зарплаты.
        Если зарплата не указана (None), возвращает 0.
        """
        if salary is None:
            return 0
        elif isinstance(salary, dict):
            if salary.get("from") is not None:
                return salary["from"] or 0
            elif salary.get("to") is not None:
                return salary["to"] or 0
            else:
                return 0
        elif isinstance(salary, (int, float)):
            return salary
        return 0

    @classmethod
    def _validate_requirements_and_clean(cls, requirements: str) -> str:
        """Валидация входных данных и очищение требования от HTML"""

        if not requirements or not isinstance(requirements, str):
            return "Требования не указаны"

        # Очищаем от HTML тегов
        cleaned = re.sub(r'<[^>]+>', '', requirements)
        return cleaned.strip()

    # Методы сравнения
    def __eq__(self, other: object) -> bool:
        """Проверка на равенство по зарплате"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other: object) -> bool:
        """Проверка: меньше ли зарплата"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __gt__(self, other: object) -> bool:
        """Проверка: больше ли зарплата"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __str__(self) -> str:
        """Строковое представление вакансии"""
        salary_str = f"{self.salary} руб." if self.salary else "Зарплата не указана"
        requirements_str = f"{self.requirements}" if self.requirements else "Требования не указаны"
        return (f"Вакансия: {self.name}\n"
                f"Зарплата: {salary_str}\n"
                f"Город: {self.city}\n"
                f"Требования: {requirements_str[:100]}...\n"
                f"Подробнее по ссылке: {self.url}")

    def __repr__(self) -> str:
        """Красивое представление для вывода списка"""
        salary_info = f"{self.salary} руб." if self.salary else "не указана"
        return f"Вакансия: {self.name} Зарплата: {salary_info} Город: {self.city})"

    def to_dict(self) -> dict:
        """Преобразование вакансии в словарь"""
        return {
            'name': self.name,
            'salary': self.salary,
            'city': self.city,
            'requirements': self.requirements,
            'url': self.url
        }

    @classmethod
    def cast_to_object_list(cls, vacancies_data: List[Dict[str, Any]]) -> List:
        """Простое создание вакансий из данных HeadHunter"""
        vacancies = []

        for data in vacancies_data:
            # Название
            name = data.get('name', 'Без названия')
            name = re.sub(r'<[^>]+>', '', name)  # Очистка названия

            # Зарплата (если есть)
            salary_data = data.get('salary')
            if salary_data and isinstance(salary_data, dict):
                salary = salary_data.get('from') or salary_data.get('to') or 0
            else:
                salary = 0

            # Город
            city_data = data.get('area', {})
            city = city_data.get('name', 'Город не указан') if isinstance(city_data, dict) else 'Город не указан'

            # Требования
            requirements_data = data.get('snippet', {})
            requirements_null = ''
            if isinstance(requirements_data, dict):
                requirements_null = requirements_data.get('requirement', '')
            requirements = cls._validate_requirements_and_clean(requirements_null)
            # Ссылку
            url = data.get('alternate_url', '')

            # Создаем вакансию
            vacancy = cls(name, salary, city, requirements, url)
            vacancies.append(vacancy)

        return vacancies
