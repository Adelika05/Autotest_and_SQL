import requests
import configuration
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER, json=body)


def get_new_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_BODY, params= {"t": track}, headers=data.headers)
    response_new_order = get_new_order().text
    print(response_new_order)

