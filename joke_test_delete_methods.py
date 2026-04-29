from api_methods_for_delete import ApiMethods


class TestPlaceAPI:
    # Тесты

    def test_post_request(self) -> None:
        api = ApiMethods()

        place_id = api.create_place()

        assert place_id != "", "place_id не создан"

        print("POST тест успешно пройден")

    def test_get_request(self) -> None:
        api = ApiMethods()

        place_id = api.create_place()

        get_response = api.get_place(place_id)

        assert get_response.status_code == 200, "GET запрос не выполнен"
        assert get_response.json()["name"] == "Frontline house", "Имя не совпадает"

        print("GET тест успешно пройден")

    def test_delete_request(self) -> None:
        api = ApiMethods()

        place_ids = []

        for _ in range(5):
            place_id = api.create_place()
            place_ids.append(place_id)

        delete_indexes = [1, 3]

        for index in delete_indexes:
            place_id = place_ids[index]

            delete_response = api.delete_place(place_id)
            delete_json = delete_response.json()

            assert delete_response.status_code == 200, f"DELETE не выполнен для {place_id}"
            assert delete_json["status"] == "OK", f"DELETE статус не OK для {place_id}"

            print(f"Удалён place_id: {place_id}")

        existing_place_ids = []

        for place_id in place_ids:
            get_response = api.get_place(place_id)

            if get_response.status_code == 200:
                get_json = get_response.json()

                if "address" in get_json:
                    existing_place_ids.append(place_id)

        assert len(existing_place_ids) == 3, "После удаления должно остаться 3 place_id"

        print("DELETE тест успешно пройден")

    def test_file_operations(self) -> None:
        api = ApiMethods()

        place_ids = []

        for _ in range(5):
            place_id = api.create_place()
            place_ids.append(place_id)

        assert len(place_ids) == 5, "Создано неверное количество place_id"

        api.save_place_ids_to_file(place_ids)

        saved_place_ids = api.read_place_ids_from_file()

        assert place_ids == saved_place_ids, "Данные в файле не совпадают"

        print("Файл запись/чтение успешно проверены")


# Запуск
if __name__ == "__main__":
    test = TestPlaceAPI()

    test.test_post_request()
    test.test_get_request()
    test.test_file_operations()
    test.test_delete_request()

    print("Все тесты успешно пройдены!")
