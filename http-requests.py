import requests
def get_character_id(Super_hero_list):
    url = ' https://superheroapi.com/api/2619421814940190/search/'
    timeout = 5
    heroes_dict={}
    for hero in Super_hero_list:
        response = requests.get(url= url+hero, timeout=timeout)
        data = response.json()
        for el in data['results']:
            if el['name'] == hero:
                heroes_dict[hero] = el['id']
    return heroes_dict

def character_intelligence_compare(Super_hero_list):
    hero_dict=get_character_id(Super_hero_list)
    new_hero_dict= {}
    url = ' https://superheroapi.com/api/2619421814940190/'
    timeout = 5
    for k in hero_dict.keys():
        response = requests.get(url = url+hero_dict[k]+'/powerstats', timeout=timeout)
        data = response.json()
        new_hero_dict[data['intelligence']]= data['name']
    final_dict = dict([max(new_hero_dict.items(), key=lambda k_v: k_v[1])])
    for k,v in final_dict.items():
        print(f"Самым умным супергероем оказался {v} его интеллект составил {k}")
character_intelligence_compare(['Captain America', 'Thanos', 'Hulk'])