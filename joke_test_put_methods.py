import requests
from requests import Response


class ApiMethods:
    # Общий класс для работы с API

    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"

    post_resource = "/maps/api/place/add/json"
    get_resource = "/maps/api/place/get/json"
    put_resource = "/maps/api/place/update/json"

    new_address = "55, glass tower, jenson 11"

    def create_place(self) -> Response:
        # Создание нового place

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

        return requests.post(url, json=json_data)

    def get_place(self, place_id: str) -> Response:
        # Получение place по place_id

        url = f"{self.base_url}{self.get_resource}{self.key}&place_id={place_id}"
        return requests.get(url)

    def put_place(self, place_id: str) -> Response:
        # Обновление адреса place

        url = self.base_url + self.put_resource + self.key

        json_data = {
            "place_id": place_id,
            "address": self.new_address,
            "key": "qaclick123"
        }

        return requests.put(url, json=json_data)


class TestPlaceAPI:
    # Тест PUT запроса и проверки обновления данных

    def test_put_request(self) -> None:
        api = ApiMethods()

        # CREATE PLACE
        create_response = api.create_place()

        assert create_response.status_code == 200, "Create request failed"
        assert create_response.json()["status"] == "OK", "Create status not OK"

        place_id = create_response.json()["place_id"]

        # PUT REQUEST
        put_response = api.put_place(place_id)

        assert put_response.status_code == 200, "PUT request failed"
        assert put_response.json()["msg"] == "Address successfully updated"

        # GET REQUEST
        get_response = api.get_place(place_id)

        assert get_response.status_code == 200, "GET request failed"
        assert get_response.json()["address"] == api.new_address

        print("PUT тест успешно пройден")


# Запуск
if __name__ == "__main__":
    TestPlaceAPI().test_put_request()
    print("Все тесты успешно пройдены!")
