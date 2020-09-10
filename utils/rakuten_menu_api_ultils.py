# %%
import requests
import json

# API constants, you shouldn't have to change these.
API_KEY = "your-key”
API_HOST = 'https://us-restaurant-menus.p.rapidapi.com'
SEARCH_PATH = '/restaurants/search'


def get_restaurants_info():
    # get resturants by location, should have parameters as location
    headers = {
        'x-rapidapi-host': API_HOST,
        'x-rapidapi-key': API_KEY,
    }
    querystring = {"page": "1"}
    url2 = API_HOST + SEARCH_PATH + "/geo?lat=40.688072&lon=-73.997385&distance=0.3"
    response_res = requests.request(
        "GET", url2, headers=headers, params=querystring)
    restaurants_info_json = json.loads(response_res.text)

    return restaurants_info_json


def get_ids_from_resonse(response_info_json):
    # get 25 resturant ids from above response
    if 'result' in response_info_json:
        restaurants_data_list = response_info_json['result']['data']
        ids = map(lambda x: x['restaurant_id'], restaurants_data_list)
        return list(ids)
    else:
        return []


def remove_numbers(string):
    # remove words that contain numbers
    output = ""
    words = string.split()
    for word in words:
        if word.isalpha():
            output += " " + word
    return output


def get_restaurant_menu_items_from_ids(ids):
    # for each id get its menu items string
    menu_items = []
    for id in ids:
        menu_items_string = get_menu_items_string(id)
        clean_menu_items_string = remove_numbers(menu_items_string)
        menu_items.append(clean_menu_items_string)

    return menu_items


def get_menu_items_string(id):
    # get menu items json by restaurant id
    headers = {
        'x-rapidapi-host': API_HOST,
        'x-rapidapi-key': API_KEY,
    }
    url = API_HOST + "/restaurant/" + str(id) + "/menuitems"
    response_menu = requests.request("GET", url, headers=headers)
    response_menu_json = json.loads(response_menu.text)

    # bonding all menu_item_name to form a description of the restaurant
    menu_item_string = ""
    if 'result' in response_menu_json:
        for menu_item in response_menu_json['result']['data']:
            menu_item_name = menu_item['menu_item_name']
            menu_item_string += " " + menu_item_name

    return menu_item_string


# %%