from kivy.app import App


def refresh_all_screens():

    App.get_running_app().root.get_screen("login").main_frame_layout.refresh_layout()
    App.get_running_app().root.get_screen("login").refresh_screen()
    App.get_running_app().root.get_screen("create_user").main_frame_layout.refresh_layout()
    App.get_running_app().root.get_screen("create_user").refresh_screen()
    App.get_running_app().root.get_screen("frontpage").refresh_screen()
    #App.get_running_app().root.get_screen("login").refresh_screen()

    pass