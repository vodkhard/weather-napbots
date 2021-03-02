import requests
import json
import library.api as api


def getWeather():
    r = api.get('/crypto-weather')
    data = r.json()
    return data['data']['weather']['weather']
