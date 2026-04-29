from api_methods import ApiMethods


class TestPlaceAPI:
    # Тесты

    def test_post_request(self) -> None:
        api = ApiMethods()

        post_response = api.create_place()

        assert post_response.status_code == 200, "POST request failed"
        assert post_response.json()["status"] == "OK", "POST status not OK"

        print("POST тест успешно пройден")

    def test_put_request(self) -> None:
        api = ApiMethods()

        # POST REQUEST
        post_response = api.create_place()

        assert post_response.status_code == 200, "POST request failed"

        place_id = post_response.json()["place_id"]

        # PUT REQUEST
        put_response = api.put_place(place_id)

        assert put_response.status_code == 200, "PUT request failed"
        assert put_response.json()["msg"] == "Address successfully updated"

        print("PUT тест успешно пройден")

    def test_get_request(self) -> None:
        api = ApiMethods()

        # POST REQUEST
        post_response = api.create_place()

        assert post_response.status_code == 200, "POST request failed"

        place_id = post_response.json()["place_id"]

        # GET REQUEST
        get_response = api.get_place(place_id)

        assert get_response.status_code == 200, "GET request failed"
        assert get_response.json()["name"] == "Frontline house", "Name does not match"

        print("GET тест успешно пройден")


# Запуск
if __name__ == "__main__":
    test = TestPlaceAPI()

    test.test_post_request()
    test.test_put_request()
    test.test_get_request()

    print("Все тесты успешно пройдены!")
