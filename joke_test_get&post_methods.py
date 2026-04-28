import requests
from requests import Response


class ApiMethods:
    # Общий класс для работы с API

    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"

    post_resource = "/maps/api/place/add/json"
    get_resource = "/maps/api/place/get/json"

    def create_place(self) -> Response:
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

        response = requests.post(url, json=json_data, timeout=10)
        return response

    def get_place(self, place_id: str) -> Response:
        url = f"{self.base_url}{self.get_resource}{self.key}&place_id={place_id}"

        response = requests.get(url, timeout=10)
        return response


class TestPlaceAPI:
    # Тесты

    file_name = "place_ids.txt"

    def test_create_place(self) -> None:
        api = ApiMethods()

        response = api.create_place()
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["status"] == "OK"

        print("POST запрос успешно выполнен")

    def test_place_flow(self) -> None:
        api = ApiMethods()

        place_ids = []

        # Создаём 5 place_id
        for _ in range(5):
            response = api.create_place()
            place_id = response.json()["place_id"]
            place_ids.append(place_id)

            print(f"Создан place_id: {place_id}")

        # Записываем в файл
        with open(self.file_name, "w") as file:
            for pid in place_ids:
                file.write(pid + "\n")

        print("\nplace_id записаны в файл.\n")

        # Читаем и проверяем GET
        with open(self.file_name, "r") as file:
            file_place_ids = file.readlines()

        for pid in file_place_ids:
            pid = pid.strip()

            response = api.get_place(pid)
            response_json = response.json()

            assert response.status_code == 200
            assert response_json != {}

            assert response_json["name"] == "Frontline house"
            assert response_json["address"] == "29, side layout, cohen 09"

            print(f"Place_id: {pid} — проверка пройдена")


if __name__ == "__main__":
    test = TestPlaceAPI()

    test.test_create_place()
    test.test_place_flow()

    print("Все тесты пройдены успешно!")
