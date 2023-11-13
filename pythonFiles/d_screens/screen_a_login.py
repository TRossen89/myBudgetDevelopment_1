from kivy.app import App

from kivy.uix.screenmanager import Screen
#from pythonFiles.a_persistence.db_connection import DBConnection
from pythonFiles.a_persistence.user_mapper import UserMapper
from pythonFiles.b_functions.c_refreshing_screens import *
from pythonFiles.g_text_inputs.a_textinput_standard import *
from pythonFiles.e_layouts.rel_top_bar import *

from pythonFiles.b_functions.b_screen_managing import *
from pythonFiles.b_functions.a_app_language import *
import json



class Login(Screen):



    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)

        self.main_frame_layout = Login_MainFrame()
        self.add_widget(self.main_frame_layout)


    def refresh_screen(self):
        self.clear_widgets()
        self.add_widget(self.main_frame_layout)


    def save_as_previous_screen(self):

        save_screen_as_previous_screen("login")

        pass





class Login_MainFrame(RelativeLayout):


    def __init__(self, **kwargs):
        super(Login_MainFrame, self).__init__(**kwargs)


        self.id = "login_main_frame"

        self.refresh_layout()


    def refresh_layout(self):

        self.app_language = get_app_language()

        if self.app_language == "english":

            self.top_bar = Rel_TopBar("Login", False, False)

            self.username = TextInput_Standard(.5, .7, False, "Username")
            self.password = TextInput_Standard(.5, .5, True, "Password")

            self.ids.create_user_button.text = "Create User"
            self.ids.login_button.text = "Log in"


        elif self.app_language == "danish":

            self.top_bar = Rel_TopBar("Login", False, False)

            self.username = TextInput_Standard(.5, .7, False, "Brugernavn")
            self.password = TextInput_Standard(.5, .5, True, "Kode")

            self.ids.create_user_button.text = "Opret bruger"
            self.ids.login_button.text = "Log på"

        self.add_widget(self.top_bar)

        self.add_widget(self.username)
        self.add_widget(self.password)



    def english_as_language(self):

        language = "english"
        set_app_language(language)

        self.refresh_layout()

        refresh_all_screens()

        pass



    def danish_as_language(self):

        language = "danish"
        set_app_language(language)
        self.refresh_layout()

        refresh_all_screens()

        pass



    def login(self):


        loginStatus = UserMapper.login_request(self.username.text, self.password.text)

        if loginStatus == "connection_failed":
            print("Connection failed")

        elif loginStatus == "select_command_failed":
            print("Select command failed")

        elif loginStatus == "credentials_failed":
            print("Credentials failed")

        elif loginStatus == "succes":
            App.get_running_app().root.get_screen("login").manager.current = 'frontpage'

        else:
            print("Something went wrong")

    pass


