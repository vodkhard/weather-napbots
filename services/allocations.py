import json
import requests
from library.db import readInFile, saveInFile, deleteInFile
from services.user import login, getAccountId, baseUrl, headers


def getAllocations(weather):
    data = readInFile(weather, "allocations.json")
    if data != None:
        allocations = data["allocations"]
        leverage = data["leverage"]
        return (allocations, leverage)
    return None


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
