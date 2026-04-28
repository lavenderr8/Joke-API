import requests


class ApiMethods:
    # Общий класс для работы с API

    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"

    post_resource = "/maps/api/place/add/json"
    get_resource = "/maps/api/place/get/json"
    put_resource = "/maps/api/place/update/json"

    new_address = "55, glass tower, jenson 11"

    def create_place(self) -> str:
        # Отправляем POST запрос и получаем place_id

        url = self.base_url + self.post_resource + self.key

        # Тело запроса
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

        # Отправляем POST
        response = requests.post(url, json=json_data)

        # Проверяем статус
        assert response.status_code == 200, "POST запрос не отработал"

        response_json = response.json()

        # Проверяем статус из ответа
        assert response_json["status"] == "OK", "Статус в ответе не OK"

        # Берём place_id
        place_id = response_json["place_id"]

        return place_id

    def get_place(self, place_id: str):
        # GET запрос по place_id

        url = f"{self.base_url}{self.get_resource}{self.key}&place_id={place_id}"

        response = requests.get(url)

        return response

    def put_place(self, place_id: str):
        # PUT запрос для изменения адреса

        put_url = self.base_url + self.put_resource + self.key

        # Тело PUT запроса
        json_put_data = {
            "place_id": place_id,
            "address": self.new_address,
            "key": "qaclick123"
        }

        # Отправляем PUT
        response = requests.put(put_url, json=json_put_data)

        return response


class TestPlaceAPI:
    # Тест

    def test_put_request(self):
        api = ApiMethods()

        # Создаём новый place
        place_id = api.create_place()

        # Отправляем PUT запрос
        put_response = api.put_place(place_id)

        # Проверяем статус
        assert put_response.status_code == 200, "PUT запрос не отработал"

        put_response_json = put_response.json()

        # Проверяем сообщение из ответа
        assert put_response_json["msg"] == "Address successfully updated"

        # Делаем GET запрос
        get_response = api.get_place(place_id)

        # Проверяем статус
        assert get_response.status_code == 200, "GET запрос не отработал"

        get_response_json = get_response.json()

        # Проверяем новый адрес
        assert get_response_json["address"] == api.new_address

        print("PUT запрос успешно отработал")


# Запуск
if __name__ == "__main__":
    test = TestPlaceAPI()
    test.test_put_request()
    print("Тест пройден успешно!")
