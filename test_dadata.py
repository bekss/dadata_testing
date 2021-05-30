import requests
from dadata import Dadata


global dadata
token = '9ae47b808663b190e7c3821285e5998aa1e27a6d'
url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"
dadata = Dadata(token, secret='4afa58208e737eb61d50110a3ad26566a1d20cc0')
key = {"query": "москва хабар"}


def res_200():
    """"Проверяеть на ответ сайта Response 200"""
    x = requests.post(url, data=key)
    response = x.reason
    return response


def response_time():
    """Проверяет время ответа API"""
    response = requests.post(url, data=key)
    return response.elapsed.total_seconds()


def encodig_html():
    """Проверяеть на правильность кодировки"""
    key = {"query": "москва хабар"}
    x = requests.post(url, data=key)
    encode = x.encoding
    return encode


def check_str():
    """Проверяеть возвращает ли определенная позиция тип str"""
    result = dadata.suggest("address", "Мишурина")
    str_name = type(result[0]['value'])
    return str_name


def check_geo_map():
    """Проверяеть на гелокацию. Существует ли такая геолокация. Если не возвращает то нужно проверить REST данные"""
    result = dadata.suggest("address", "Мишурина")
    return type(float(result[0]['data']['geo_lon']))


def check_integer():
    """Проверять, пост код является ли цифрой"""
    result = dadata.suggest("address", "Мишурина")
    is_integer = type(int(result[0]['data']['postal_code']))
    return is_integer


def length_data():
    """Проверка на длиу данных"""
    result = dadata.suggest("address", "Мишурина")
    return len(result[0])


def is_keys(keys):
    """Проверка на ключ. Есть ли такой ключи в REST API"""
    result = dadata.suggest("address", "Мишурина")
    new_key = result[0]['data'][keys]
    if new_key is True or not None:
        return new_key
    else:
        raise Exception('Такого ключа не существует')


def country(country_name):
    """Проверка на наличие государство"""
    result = dadata.suggest("address", "Мишурина")
    count = result[0]['data']['country']
    if country_name == count:
        return count


def ip_locate(ip):
    """Проверка на наличие определенного IP адреса """
    ip_l = dadata.iplocate(ip)
    value_ip = ip_l['value']
    if value_ip == 'г Краснодар' and not None:
        return value_ip


def english_vilage(language, query):
    """Проверка на запрос пользователя по определенным данным"""
    vil = dadata.suggest(name="address", query=query, language=language)
    if vil[0]['value'] == "Russia, gorod Samara, prospekt Metallurgov" and not None:
        return vil[0]['value']


def check_mail(mail):
    """Проверка на наличие email по заданным данным пользователя"""
    cheked_mail = dadata.suggest(name="email", query=mail)
    if mail in cheked_mail[0]['value']:
        return mail
    else:
        raise Exception('Такого mail не существует')


def test_response_200():
    assert res_200() == 200


def test_encoding():
    assert encodig_html() == "UTF-8"


def test_chek_str():
    assert check_str() == str


def test_integer_output():
    assert check_integer() == int


def test_lenght_data():
    assert length_data() == 3


def test_country_name():
    assert country('Россия') == 'Россия'


def test_geo_map():
    assert check_geo_map() == float


def test_is_key(key='tax_office'):
    keys = is_keys(key)
    assert keys == keys


def test_ip_locate(ips="46.226.227.20"):
    ip_loc = ip_locate(ips)
    assert ip_loc == 'г Краснодар'


def test_engl_vilage(lan='en', que='samara metal'):
    res_eng = english_vilage(lan, que)
    assert res_eng == 'Russia, gorod Samara, prospekt Metallurgov'


def test_check_mail(for_mail='beks@'):
    chek_mails = check_mail(for_mail)
    assert for_mail == chek_mails


def test_time_check():
    time = response_time()
    assert time < 1.5
