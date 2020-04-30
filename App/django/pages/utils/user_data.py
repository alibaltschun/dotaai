from django.shortcuts import HttpResponse
import json
import os

BASE = (os.path.dirname(os.path.realpath(__file__)))


def read_user_data():
    USER_DATA_DRAFTING = open(BASE + "/../../local_data/drafting.json")
    USER_DATA_DRAFTING = USER_DATA_DRAFTING.read()
    USER_DATA_DRAFTING = json.loads(USER_DATA_DRAFTING)
    return USER_DATA_DRAFTING


def save_user_data(data):
    with open((BASE + "/../../local_data/drafting.json"), 'w') as f:
        json.dump(data, f)


def update_user_data(request, arr_key, value, data=read_user_data()):
    arr_key = arr_key.split(".")

    if len(arr_key) > 1:
        first_key = arr_key[0]
        arr_key = '.'.join(arr_key[1:])
        update_user_data(request, arr_key, value, data=data[first_key])

    else:
        print(arr_key[0].isdigit())
        if arr_key[0].isdigit():
            data[int(arr_key[0])] = value
        else:
            data[arr_key[0]] = value

    save_user_data(data)
    return HttpResponse(200)
