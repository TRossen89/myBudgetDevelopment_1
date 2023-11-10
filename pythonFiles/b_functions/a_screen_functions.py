
import json



def save_screen_as_previous_screen(screen_name):

    filename = "jsonFiles/previous_screen.json"

    with open(filename, "w") as fileobject:
        json.dump(screen_name, fileobject)



def get_previous_screen():

    filename = "jsonFiles/previous_screen.json"

    with open(filename, "r") as fileobject:
        screen_name = json.load(fileobject)

        print(screen_name)

    return screen_name