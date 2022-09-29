import requests


def get_card_curs():
    r_cards_curs = requests.get('https://belarusbank.by/api/kurs_cards')
    json_cards_curs = r_cards_curs.json()[0]
    print(f'В {json_cards_curs["kurs_date_time"][:-9].replace("-", ".")} банк покупает | банк продает:')
    print(f'USD: {json_cards_curs["USDCARD_in"]} | {json_cards_curs["USDCARD_out"]}\n'
          f'EUR: {json_cards_curs["EURCARD_in"]} | {json_cards_curs["EURCARD_out"]}\n'
          f'RUB: {json_cards_curs["RUBCARD_in"]} | {json_cards_curs["RUBCARD_out"]}')
    print()


def get_cash_curs(city="Минск"):
    r_cash_curs = requests.get(f'https://belarusbank.by/api/kursExchange?city={city}')
    json_cash_curs = r_cash_curs.json()
    for item in json_cash_curs:
        print(f'В {item["filials_text"]} банк покупает | банк продает:')
        print(f'USD: {item["USD_in"]} | {item["USD_out"]}\n'
              f'EUR: {item["EUR_in"]} | {item["EUR_out"]}\n'
              f'RUB: {item["RUB_in"]} | {item["RUB_out"]}')
        print()


def get_filials_info(city="Минск"):
    r_filials = requests.get(f'https://belarusbank.by/api/filials_info?city={city}')
    filials = r_filials.json()
    important_keys = ['filial_id', 'filial_name', 'street_type', 'street', 'info_worktime']
    for i in range(0, len(filials)):
        for key in filials[i]:
            if key in important_keys:
                print(f'{key}: {filials[i][key]}')
        print('')


print("""
Выберите опцию:
1 - Курс по картам
2 - Курс наличными
3 - Инфо о филиалах
""")
choice = int(input('ожидание ввода: '))
if choice == 1:
    get_card_curs()
if choice == 2:
    cityName = input('введите город: ')
    if len(cityName) > 2:
        get_cash_curs(cityName)
    else:
        print('Неверное название города')
if choice == 3:
    cityName = input('введите город: ')
    if len(cityName) > 2:
        get_filials_info(cityName)
    else:
        print('Неверное название города')
