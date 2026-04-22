import requests

class TestCreateJokeCategory:

    # Базовый URL
    url = "https://api.chucknorris.io"

    def test_get_all_categories(self):
        # Получаем список всех категорий
        url_categories = f'{self.url}/jokes/categories'
        response = requests.get(url_categories)

        # Проверяем статус-код
        assert response.status_code == 200
        print('Успешно: категории получены')

        categories = response.json()
        print(f'Список категорий: {categories}')

        # Проходим по каждой категории
        for category in categories:
            print(f'\nПроверяем категорию: {category}')

            url_random = f"{self.url}/jokes/random?category={category}"
            joke_response = requests.get(url_random)

            # Проверяем статус-код
            assert joke_response.status_code == 200
            print('Статус-код корректен')

            joke_data = joke_response.json()

            # Проверяем, что категория совпадает
            joke_categories = joke_data.get("categories")
            print(f"Категории в ответе: {joke_categories}")

            assert category in joke_categories
            print("Категория корректна")

            # Проверяем наличие текста шутки
            joke_text = joke_data.get("value")
            assert joke_text is not None
            print(f"Шутка: {joke_text}")

        print("\nВсе категории успешно протестированы!")

start = TestCreateJokeCategory()
start.test_get_all_categories()

