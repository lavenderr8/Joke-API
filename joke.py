# Импортируем библиотеку
import requests

# Выведем на печать URL,по которому отправляем запрос
url = "https://api.chucknorris.io/jokes/5o5MruPjRLiweDrpWfWJWA"
print(url)

# Отправим запрос на получение рандомной шутки
result = requests.get(url)

# Выведем на печать статус-код ответа
print("Статус код: " + str(result.status_code))

# Проведём проверку ОР и ФР ответа
assert 200 == result.status_code

# Выведем на печать сообщение о том, что ОР == ФР
if result.status_code == 200:
    print("Успешно! Статус код верный!")
else:
    print("Ошибка! Статус код неверный!")

# Команда для кодировки в нужный нам формат
result.encoding = 'utf-8'

# Выведем на печать ответ запроса в формате json
print(result.json())
