import requests
from requests import Response


class ApiMethods:
    # Общий класс для работы с API

    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"

    post_resource = "/maps/api/place/add/json"
    get_resource = "/maps/api/place/get/json"
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
        # GET запрос

        url = f"{self.base_url}{self.get_resource}{self.key}&place_id={place_id}"
        return requests.get(url)

    def delete_place(self, place_id: str) -> Response:
        # DELETE запрос

        url = self.base_url + self.delete_resource + self.key

        json_data = {"place_id": place_id}

        return requests.delete(url, json=json_data)

    def save_place_ids_to_file(self, place_ids: list[str]) -> None:
        # Запись в файл

        with open(self.places_file, "w") as file:
            for place_id in place_ids:
                file.write(place_id + "\n")

    def read_place_ids_from_file(self) -> list[str]:
        # Чтение из файла

        with open(self.places_file, "r") as file:
            return file.read().splitlines()

    def save_existing_place_ids(self, place_ids: list[str]) -> None:
        # Сохранение существующих

        with open(self.existing_places_file, "w") as file:
            for place_id in place_ids:
                file.write(place_id + "\n")
