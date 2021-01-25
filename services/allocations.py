import json
import requests
from lib.db import readInFile, saveInFile, deleteInFile
from services.user import login, getAccountId, baseUrl, headers


def getAllocations(weather):
    allocations = None
    leverage = 1.00
    if weather == 'Extreme markets':
        allocations = {
            'STRAT_ETH_USD_H_3_V2': 0.35,
            'STRAT_BTC_USD_H_3_V2': 0.35,
            'STRAT_BTC_ETH_USD_H_1': 0.3
        }
    elif weather == 'Mild bull markets':
        allocations = {
            'STRAT_ETH_USD_H_3_V2': 0.3,
            'STRAT_BTC_USD_H_3_V2': 0.3,
            'STRAT_BTC_ETH_USD_H_1': 0.4
        }
        leverage = 1.5
    elif weather == 'Mild bear or range markets':
        allocations = {
            'STRAT_ETH_USD_H_3_V2': 0.35,
            'STRAT_BTC_USD_H_3_V2': 0.35,
            'STRAT_BTC_ETH_USD_H_1': 0.3
        }
        leverage = 1.5
    return (allocations, leverage)


def updateAllocations(weather):
    compo, leverage = getAllocations(weather)
    accountId = getAccountId()
    url = baseUrl + '/account/{}'.format(accountId)
    payload = {
        'botOnly': True,
        'compo': {
            'compo': compo,
            'leverage': str(leverage)
        }
    }
    r = requests.patch(url=url, headers=headers, data=json.dumps(payload))
    response = r.json()
    if response['success']:
        print('Allocation updated!')
        return True
    print(response['errorMessage'])
    return False
