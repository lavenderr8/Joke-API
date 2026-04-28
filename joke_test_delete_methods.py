import requests
from requests import Response


class ApiMethods:
    # Общий класс для работы с API

    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"

    get_resource = "/maps/api/place/get/json"
    post_resource = "/maps/api/place/add/json"
    delete_resource = "/maps/api/place/delete/json"

    places_file = "place_ids.txt"
    existing_places_file = "existing_place_ids.txt"

    def create_place(self) -> str:
        # Создание place и возврат place_id

        url = self.base_url + self.post_resource + self.key

        json_data = {
            "location": {"lat": -38.383494, "lng": 33.427362},
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": ["shoe park", "shop"],
            "website": "http://google.com",
            "language": "French-IN"
        }

        response = requests.post(url, json=json_data)
        return response.json()["place_id"]

    def get_place(self, place_id: str) -> Response:
        # Получение place по place_id

        url = f"{self.base_url}{self.get_resource}{self.key}&place_id={place_id}"
        return requests.get(url)

    def delete_place(self, place_id: str) -> Response:
        # Удаление place

        url = self.base_url + self.delete_resource + self.key

        json_data = {"place_id": place_id}

        return requests.delete(url, json=json_data)

    def save_place_ids_to_file(self, place_ids: list[str]) -> None:
        # Сохранение place_id в файл

        with open(self.places_file, "w") as file:
            for place_id in place_ids:
                file.write(place_id + "\n")

    def read_place_ids_from_file(self) -> list[str]:
        # Чтение place_id из файла

        with open(self.places_file, "r") as file:
            return [line.strip() for line in file.readlines()]

    def save_existing_place_ids(self, place_ids: list[str]) -> None:
        # Сохранение существующих place_id

        with open(self.existing_places_file, "w") as file:
            for place_id in place_ids:
                file.write(place_id + "\n")


class TestPlaceAPI:
    # Тесты

    def test_delete_and_get_places(self) -> None:
        api = ApiMethods()

        # Создаём 5 place_id
        place_ids = []

        for _ in range(5):
            place_id = api.create_place()
            place_ids.append(place_id)

        assert len(place_ids) == 5

        print("Создано 5 place_id")

        # Сохраняем place_id в файл
        api.save_place_ids_to_file(place_ids)

        # Читаем place_id из файла
        saved_place_ids = api.read_place_ids_from_file()

        assert len(saved_place_ids) == 5

        print("Файл успешно прочитан")

        # Удаляем 2-й и 4-й place_id
        delete_indexes = [1, 3]

        for index in delete_indexes:
            place_id = saved_place_ids[index]

            delete_response = api.delete_place(place_id)
            delete_json = delete_response.json()

            assert delete_response.status_code == 200
            assert delete_json["status"] == "OK"

            print(f"Удалён place_id: {place_id}")

        # Проверяем, какие place_id ещё существуют
        existing_place_ids = []

        for place_id in saved_place_ids:
            get_response = api.get_place(place_id)

            if get_response.status_code == 200:
                get_json = get_response.json()

                if "address" in get_json:
                    existing_place_ids.append(place_id)
                    print(f"Существует: {place_id}")
                else:
                    print(f"Нет address: {place_id}")
            else:
                print(f"Не существует: {place_id}")

        assert len(existing_place_ids) == 3

        print("Найдено 3 существующих place_id")

        api.save_existing_place_ids(existing_place_ids)

        print("Существующие place_id сохранены")


# Запуск
if __name__ == "__main__":
    TestPlaceAPI().test_delete_and_get_places()
    print("Тест пройден успешно!")
