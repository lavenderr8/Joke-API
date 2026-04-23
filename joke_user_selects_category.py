import requests


class JokeAPIClient:
    # Базовый URL
    BASE_URL = "https://api.chucknorris.io"

    def get_categories(self):
        # Получение списка всех категорий
        response = requests.get(f"{self.BASE_URL}/jokes/categories")
        response.raise_for_status()
        return response.json()

    def get_random_joke_by_category(self, category: str):
        # Получение случайной шутки по категории
        response = requests.get(
            f"{self.BASE_URL}/jokes/random?category={category}"
        )
        response.raise_for_status()
        return response.json()


# Логика
def get_joke_for_category(category: str):
    # Создаём клиент
    client = JokeAPIClient()

    # Нормализуем ввод пользователя
    category = category.strip().lower()

    # Получаем список категорий
    categories = client.get_categories()

    # Проверяем, что категория существует
    if category not in categories:
        raise ValueError(f"Категория '{category}' не найдена")

    # Получаем шутку по категории
    joke_response = client.get_random_joke_by_category(category)

    # Проверяем ответ
    if "value" not in joke_response or joke_response["value"] is None:
        raise ValueError("Некорректный ответ API")

    # Возвращаем текст шутки
    return joke_response["value"]


# Взаимодействие с пользователем
def main():
    # Создаём клиент
    client = JokeAPIClient()

    # Получаем список категорий
    categories = client.get_categories()

    # Выводим категории пользователю
    print("Доступные категории:")
    print(", ".join(categories))

    # Просим пользователя ввести корректную категорию
    while True:
        # Запрашиваем категорию у пользователя
        user_category = input("\nВведите категорию шутки: ").strip().lower()

        # Проверяем, что категория существует
        if user_category in categories:
            break

        print("Такой категории нет! Попробуйте снова.")

    try:
        # Получаем шутку
        joke = get_joke_for_category(user_category)

        # Выводим результат
        print("\nШутка:")
        print(joke)

    except ValueError as e:
        # Обработка ошибок
        print(f"Ошибка: {e}")


# Тесты
class TestChuckNorrisJokes:

    def test_joke_by_category(self):
        # Проверяем получение шутки по валидной категории
        joke = get_joke_for_category("animal")

        # Проверяем, что ответ — строка
        assert isinstance(joke, str)

        # Проверяем, что строка не пустая
        assert len(joke) > 0


# Запуск
if __name__ == "__main__":
    main()
