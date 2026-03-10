# Импортируем библиотеку
import requests


# Создадим общий класс
class TestCreateJoke:
    # Базовый URL для случайной шутки
    base_url = "https://api.chucknorris.io/jokes/random"

    # Создадим метод для теста
    def test_joke_category_and_chuck(self):
        # Категория шутки
        category = "dev"

        # Отправка GET-запроса с параметром category
        response = requests.get(self.base_url, params={"category": category})

        # Проверка статус-кода
        assert response.status_code == 200, "Ошибка! Статус-код неверный."

        # Преобразуем ответ в JSON
        data = response.json()

        # Проверка соответствия категории
        assert category in data["categories"], f"Категория '{category}' не найдена в ответе"

        # Проверка на содержание имени Chuck в тексте шутки
        assert "Chuck" in data["value"], "Имя 'Chuck' не найдено в шутке"

        # Вывод информации о шутке
        print("\nСлучайная шутка")
        print("Категория:", data["categories"])
        print("Шутка:", data["value"])


# Запуск теста
if __name__ == "__main__":
    test = TestCreateJoke()
    test.test_joke_category_and_chuck()
