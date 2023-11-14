import json


def set_current_user(user_id):

    filename = "jsonFiles/current_user_id.json"

    with open(filename, "w") as fileobject:
        json.dump(user_id, fileobject)


def get_current_user():

    filename = "jsonFiles/current_user_id.json"

    with open(filename, "r") as fileobject:
        user_id = json.load(fileobject)

    return user_id




