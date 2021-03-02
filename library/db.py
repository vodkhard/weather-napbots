import json


def readInFile(key=None, file="user.json"):
    with open(file, "r") as data_file:
        try:
            data = json.load(data_file)
        except:
            data = {}

    if key != None:
        return data[key] if key in data else None
    return data


def saveInFile(key, value, file="user.json"):
    data = readInFile()
    data[key] = value
    with open(file, "w") as data_file:
        json.dump(data, data_file)


def deleteInFile(key, file="user.json"):
    data = readInFile()
    data.pop(key, None)
    with open(file, "w") as data_file:
        json.dump(data, data_file)
