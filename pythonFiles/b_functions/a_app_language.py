
import json

def get_app_language():

    filename = "jsonFiles/app_language.json"
    with open(filename, "r") as fileobjekt:
        app_language = json.load(fileobjekt)

    return app_language



def set_app_language(language):

    filename = "jsonFiles/app_language.json"
    with open(filename, "w") as fileobjekt:
        json.dump(language, fileobjekt)