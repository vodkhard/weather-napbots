import requests
import json
from lib.db import readInFile, saveInFile
from lib.api import baseUrl, headers


def login(email, password):
    url = baseUrl + '/user/login'
    r = requests.post(url=url, headers=headers, data=json.dumps(
        {'email': email, 'password': password}))
    data = r.json()
    if data['success'] == False:
        return print('Error on login!')
    accessToken = data['data']['accessToken']
    headers['token'] = accessToken
    print('Your access token is : {}'.format(accessToken))
    return accessToken


def getUserId():
    userId = readInFile('userId')
    if userId == None:
        url = baseUrl + '/user/me'
        r = requests.get(url=url, headers=headers)
        userId = r.json()['data']['userId']
        saveInFile('userId', userId)
    print('Your user id is : {}'.format(userId))
    return userId


def getAccountId():
    accountId = readInFile('accountId')
    if accountId == None:
        userId = getUserId()
        url = baseUrl + '/account/for-user/{}'.format(userId)
        r = requests.get(url=url, headers=headers)
        accountId = r.json()['data'][0]['accountId']
        saveInFile('accountId', accountId)
    print('Your account id is : {}'.format(accountId))
    return accountId
