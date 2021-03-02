import requests

headers = {
    'content-type': 'application/json'
}
baseUrl = 'https://middle.napbots.com/v1'


def addHeader(key, value):
    headers[key] = value


def get(url, payload={}):
    return requests.get(baseUrl + url, headers=headers, json=payload)
