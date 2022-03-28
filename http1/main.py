import requests


def get_json(name):
    url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
    response = requests.get(url)
    return response


def search_max_int_hero_variety(name):
    max_intelligence_id = ''
    max_intelligence = 0
    for hero in get_json(name).json()['results']:
        if name == hero['name']:
            intelligence = int(hero["powerstats"]['intelligence'])
            hero_id = hero['id']
            if intelligence > max_intelligence:
                max_intelligence = intelligence
                max_intelligence_id = hero_id
    heroes[max_intelligence_id] = max_intelligence


def comparer():
    heroes = {}
    names = ['Hulk', 'Captain America', 'Thanos']
    max_hero_int = 0
    max_hero_id = ''
    for name in names:
        search_max_int_hero_variety(name)
    for hero_id, hero_int in heroes.items():
        if hero_int > max_hero_int:
            max_hero_int = hero_int
            max_hero_id = hero_id
    return max_hero_id


if __name__ == '__main__':
    heroes = {}
    print(comparer())