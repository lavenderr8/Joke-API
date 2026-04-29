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
        # POST запрос для создания нового place

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
        # GET запрос для получения place по place_id

        url = f"{self.base_url}{self.get_resource}{self.key}&place_id={place_id}"
        return requests.get(url)

    def put_place(self, place_id: str) -> Response:
        # PUT запрос для обновления адреса

        url = self.base_url + self.put_resource + self.key

        json_data = {
            "place_id": place_id,
            "address": self.new_address,
            "key": "qaclick123"
        }

        return requests.put(url, json=json_data)
