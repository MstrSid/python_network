import requests


def get_card_curs():
    r_cards_curs = requests.get('https://belarusbank.by/api/kurs_cards')
    json_cards_curs = r_cards_curs.json()[0]
    for key in json_cards_curs:
        print(f'{key}: {json_cards_curs[key]}')
    print()


def get_cash_curs(city):
    r_filials = requests.get(f'https://belarusbank.by/api/filials_info?city={city}')
    filials = r_filials.json()
    important_keys = ['filial_id', 'filial_name', 'street_type', 'street', 'info_worktime']
    for i in range(0, len(filials)):
        for key in filials[i]:
            if key in important_keys:
                print(f'{key}: {filials[i][key]}')
        print('')


print("""
Select option:
1 - Get card curs;
2 - Get cash curs
""")
choice = int(input('waiting: '))
if choice == 1:
    get_card_curs()
if choice == 2:
    cityName = input('input city name: ')
    if len(cityName) > 2:
        get_cash_curs(cityName)
    else:
        print('Invalid city name')
