import requests


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

    def delete_place(self, place_id: str):
        # DELETE запрос для удаления place_id

        delete_url = self.base_url + self.delete_resource + self.key

        # Тело DELETE запроса
        json_delete_data = {"place_id": place_id}

        # Отправляем DELETE
        response = requests.delete(delete_url, json=json_delete_data)

        return response

    def save_place_ids_to_file(self, place_ids: list):
        # Сохраняем place_id в текстовый файл

        with open(self.places_file, "w") as file:
            for place_id in place_ids:
                file.write(place_id + "\n")

    def read_place_ids_from_file(self) -> list:
        # Читаем place_id из текстового файла

        with open(self.places_file, "r") as file:
            place_ids = [line.strip() for line in file.readlines()]

        return place_ids

    def save_existing_place_ids(self, place_ids: list):
        # Сохраняем существующие place_id в новый файл

        with open(self.existing_places_file, "w") as file:
            for place_id in place_ids:
                file.write(place_id + "\n")


class TestPlaceAPI:
    # Тест

    def test_delete_and_get_places(self):
        api = ApiMethods()

        place_ids = []

        # Создаём 5 новых place_id
        for _ in range(5):
            place_id = api.create_place()
            place_ids.append(place_id)

        # Проверяем количество созданных place_id
        assert len(place_ids) == 5, "Создано неверное количество place_id"

        print("Создано 5 place_id")

        # Сохраняем place_id в текстовый файл
        api.save_place_ids_to_file(place_ids)

        print("place_id сохранены в файл")

        # Читаем place_id из файла
        saved_place_ids = api.read_place_ids_from_file()

        # Проверяем количество place_id в файле
        assert len(saved_place_ids) == 5, "В файле должно быть 5 place_id"

        print("Файл успешно прочитан")

        # Удаляем 2-й и 4-й place_id
        delete_indexes = [1, 3]

        for index in delete_indexes:
            delete_response = api.delete_place(saved_place_ids[index])

            # Проверяем статус DELETE
            assert delete_response.status_code == 200, \
                f"DELETE запрос не отработал для place_id: {saved_place_ids[index]}"

            delete_response_json = delete_response.json()

            # Проверяем статус удаления
            assert delete_response_json["status"] == "OK", \
                f"Статус удаления не OK для place_id: {saved_place_ids[index]}"

            print(f"place_id удалён: {saved_place_ids[index]}")

        existing_place_ids = []

        # Проверяем существование всех локаций через GET
        for place_id in saved_place_ids:

            get_response = api.get_place(place_id)

            # Существующая локация
            if get_response.status_code == 200:

                get_response_json = get_response.json()

                if "address" in get_response_json:
                    existing_place_ids.append(place_id)

                    print(f"Локация существует: {place_id}")

            # Несуществующая локация
            else:
                print(f"Локация не существует: {place_id}")

        # Проверяем количество существующих локаций
        assert len(existing_place_ids) == 3, \
            "После удаления должно остаться 3 существующие локации"

        print("Найдено 3 существующие локации")

        # Сохраняем существующие локации в новый файл
        api.save_existing_place_ids(existing_place_ids)

        print("3 существующие локации сохранены в новый файл")


# Запуск
if __name__ == "__main__":
    test = TestPlaceAPI()
    test.test_delete_and_get_places()

    print("Тест пройден успешно!")
