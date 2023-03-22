geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def search_ru(geo_logs):

    """Функция возвращает отфильтрованный список geo_logs, содержащий только визиты из России."""

    for trip in geo_logs[:]:
        for visit, city in trip.items():
            if city[0 or 1] != 'Россия':
                geo_logs.remove(trip)
    return geo_logs


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def get_unique_ids(ids):

    """Функция возвращает все уникальные гео-ID из значений словаря ids."""

    result = set()
    for i in ids.values():
        result.update(i)
    return sorted(list(result))


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def get_max_value(stats):

    """Функция возвращает название канала с максимальным объемом."""

    result = max(stats, key=stats.get)
    return result
