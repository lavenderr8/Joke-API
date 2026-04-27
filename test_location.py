import requests


class ApiMethods:
    # Общий класс для работы с API

    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"

    post_resource = "/maps/api/place/add/json"
    get_resource = "/maps/api/place/get/json"

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

        print(f"Создан place_id: {place_id}")

        return place_id

    def get_place(self, place_id: str):
        # GET запрос по place_id

        url = f"{self.base_url}{self.get_resource}{self.key}&place_id={place_id}"

        response = requests.get(url)

        return response


class TestPlaceAPI:
    # Тест

    file_name = "place_ids.txt"

    def test_place_flow(self):
        api = ApiMethods()

        # Создаём 5 place_id
        place_ids = []

        for _ in range(5):
            place_id = api.create_place()
            place_ids.append(place_id)

        # Сохраняем их в файл
        with open(self.file_name, "w") as file:
            for pid in place_ids:
                file.write(pid + "\n")

        print("\nplace_id записаны в файл.\n")

        # Читаем из файла и проверяем GET
        with open(self.file_name, "r") as file:
            file_place_ids = file.readlines()

        for pid in file_place_ids:
            pid = pid.strip()

            response = api.get_place(pid)

            # Проверяем статус
            assert response.status_code == 200, f"GET запрос упал для {pid}"

            response_json = response.json()
            print(f"Ответ GET для {pid}: {response_json}")

            # Проверяем, что ответ не пустой
            assert response_json != {}, f"Пустой ответ для {pid}"

            # Проверяем основные данные
            assert response_json["name"] == "Frontline house", "Имя не совпадает"
            assert response_json["address"] == "29, side layout, cohen 09", "Адрес не совпадает"

            print(f"place_id: {pid} - существует и данные корректны\n")


# Запуск
if __name__ == "__main__":
    test = TestPlaceAPI()
    test.test_place_flow()
    print("Тест пройден успешно!")
