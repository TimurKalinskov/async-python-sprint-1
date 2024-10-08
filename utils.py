CITIES = {
    "MOSCOW": "https://code.s3.yandex.net/async-module/moscow-response.json",
    "PARIS": "https://code.s3.yandex.net/async-module/paris-response.json",
    "LONDON": "https://code.s3.yandex.net/async-module/london-response.json",
    "BERLIN": "https://code.s3.yandex.net/async-module/berlin-response.json",
    "BEIJING": "https://code.s3.yandex.net/async-module/beijing-response.json",
    "KAZAN": "https://code.s3.yandex.net/async-module/kazan-response.json",
    "SPETERSBURG": "https://code.s3.yandex.net/async-module/spetersburg-response.json",
    "VOLGOGRAD": "https://code.s3.yandex.net/async-module/volgograd-response.json",
    "NOVOSIBIRSK": "https://code.s3.yandex.net/async-module/novosibirsk-response.json",
    "KALININGRAD": "https://code.s3.yandex.net/async-module/kaliningrad-response.json",
    "ABUDHABI": "https://code.s3.yandex.net/async-module/abudhabi-response.json",
    "WARSZAWA": "https://code.s3.yandex.net/async-module/warszawa-response.json",
    "BUCHAREST": "https://code.s3.yandex.net/async-module/bucharest-response.json",
    "ROMA": "https://code.s3.yandex.net/async-module/roma-response.json",
    "CAIRO": "https://code.s3.yandex.net/async-module/cairo-response.json",
}

CITIES_DESCRIPTION_MAP = {
    'MOSCOW': 'Москва',
    'PARIS': 'Париж',
    'LONDON': 'Лондон',
    'BERLIN': 'Берлин',
    'BEIJING': 'Пекин',
    'KAZAN': 'Казань',
    'SPETERSBURG': 'Санкт-Петербург',
    'VOLGOGRAD': 'Волгоград',
    'NOVOSIBIRSK': 'Новосибирск',
    'KALININGRAD': 'Калининград',
    'ABUDHABI': 'Абу-Даби',
    'WARSZAWA': 'Варшава',
    'BUCHAREST': 'Бухарест',
    'ROMA': 'Рим',
    'CAIRO': 'Каир'
}

ERR_MESSAGE_TEMPLATE = "Something wrong. Please contact with mentor."

MIN_MAJOR_PYTHON_VER = 3
MIN_MINOR_PYTHON_VER = 9

HOURS_RANGE = (9, 19)
GOOD_CONDITIONS = ('clear', 'partly-cloudy', 'cloudy', 'overcast')

CSV_FILE_RELATIVE_PATH = 'result.csv'


def check_python_version():
    import sys

    if (
            sys.version_info.major < MIN_MAJOR_PYTHON_VER
            or sys.version_info.minor < MIN_MINOR_PYTHON_VER
    ):
        raise Exception(
            "Please use python version >= {}.{}".format(
                MIN_MAJOR_PYTHON_VER, MIN_MINOR_PYTHON_VER
            )
        )


def get_url_by_city_name(city_name):
    try:
        return CITIES[city_name]
    except KeyError:
        raise Exception("Please check that city {} exists".format(city_name))
