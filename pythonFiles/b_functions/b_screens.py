from kivy.app import App
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



def refresh_all_screens():

    App.get_running_app().root.get_screen("login").main_frame_layout.refresh_layout()
    App.get_running_app().root.get_screen("login").refresh_screen()
    App.get_running_app().root.get_screen("create_user").main_frame_layout.refresh_layout()
    App.get_running_app().root.get_screen("create_user").refresh_screen()
    App.get_running_app().root.get_screen("frontpage").refresh_screen()
    App.get_running_app().root.get_screen("settings_mb").refresh_screen()
    App.get_running_app().root.get_screen("choose_language").refresh_screen()

    #App.get_running_app().root.get_screen("login").refresh_screen()

    pass