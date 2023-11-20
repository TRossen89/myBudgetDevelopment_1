import json


def set_current_user(user):

    list_with_user_information = []

    for ui in user:
        list_with_user_information.append(ui)

    filename = "jsonFiles/current_user.json"

    with open(filename, "w") as fileobject:
        json.dump(list_with_user_information, fileobject)


def get_current_user():

    filename = "jsonFiles/current_user.json"

    with open(filename, "r") as fileobject:
        user = json.load(fileobject)

    return user




