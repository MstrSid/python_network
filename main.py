import requests

r_cards_curs = requests.get('https://belarusbank.by/api/kurs_cards')
r_filials = requests.get('https://belarusbank.by/api/filials_info?city=Бобруйск')
json_cards_curs = r_cards_curs.json()[0]
for key in json_cards_curs:
    print(f'{key}: {json_cards_curs[key]}')
print()

filials = r_filials.json()
important_keys = ['filial_id', 'filial_name', 'street_type', 'street', 'info_worktime']
for i in range(0, len(filials)):
    for key in filials[i]:
        if key in important_keys:
            print(f'{key}: {filials[i][key]}')
    print('')
