class FileWorker:
    """Простой класс для работы с файлами"""

    def save(self, data, filename):
        """Сохранить данные в файл"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(data))
            return True
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return False

    def read(self, filename):
        """Прочитать данные из файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return None
