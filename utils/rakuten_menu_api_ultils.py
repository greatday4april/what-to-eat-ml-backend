# %%
import requests
import json
import os

# API constants, you shouldn't have to change these.
# API_KEY = os.environ["RAKUTEN_API_KEY"]
API_KEY = os.environ['RAKUTEN_API_KEY']
API_HOST = "https://us-restaurant-menus.p.rapidapi.com"
SEARCH_PATH = "/restaurants/search/geo"
DEFAULT_LOCATION = [38.898689814814816, -77.03749537037038]


def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, path)
    headers = {
        'x-rapidapi-host': "us-restaurant-menus.p.rapidapi.com",
        'x-rapidapi-key': api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    data = json.loads(response.text)
    if 'error' in data:
        raise Exception(str(data))
    return data


def get_restaurants(location=DEFAULT_LOCATION, api_key=API_KEY):
    """Given location, get all nearby (whitin 0.3 mile) restaurants

    Args:
        location (list): geological location of user in the form of [lat, lon].

    Returns:
        dict: JSON response containing information of nearby resturants.
    """
    latitude, longtitude = location[0], location[1]
    url_params = {"page": "1", "lon": longtitude, "lat": latitude, "distance": "0.3"}

    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_menus(id, api_key=API_KEY):
    """Given restaurants id, get menu items of the resturant.

    Args:
        id (int): id of the resturant.

    Returns:
        dict: JSON response containing menu infos of the restaurant.
    """
    path = "/restaurant/" + str(id) + "/menuitems"

    return request(API_HOST, path, api_key, url_params=None)


# def get_ids_from_resonse(response_info_json):
#     # get 25 resturant ids from above response
#     if 'result' in response_info_json:
#         restaurants_data_list = response_info_json['result']['data']
#         ids = map(lambda x: x['restaurant_id'], restaurants_data_list)
#         return list(ids)
#     else:
#         return []


# def get_restaurant_menu_items_from_ids(ids):
#     # for each id get its menu items string
#     menu_items = []
#     for id in ids:
#         response_menu_json = get_menus(id)

#         # bonding all menu_item_name to form a description of the restaurant
#         menu_item_string = ""
#         if 'result' in response_menu_json:
#             for menu_item in response_menu_json['result']['data']:
#                 menu_item_name = menu_item['menu_item_name']
#                 menu_item_string += " " + menu_item_name
        
#         menu_items.append(menu_items_string)

#     return menu_items


def main():
    data = get_restaurants()
    rests = data['result']['data']
    result = map(lambda x: x['restaurant_name'], rests)
    print(sorted(list(result)))

if __name__ == '__main__':
    main()
