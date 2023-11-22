import json


def set_current_user(user):

    filename = "jsonFiles/current_user.json"

    with open(filename, "w") as fileobject:
        json.dump(user, fileobject)


def get_current_user():

    filename = "jsonFiles/current_user.json"

    with open(filename, "r") as fileobject:
        user = json.load(fileobject)

    return user




