from kivy.uix.screenmanager import Screen
#from pythonFiles.a_persistence.db_connection import DBConnection
from pythonFiles.a_persistence.user_mapper import UserMapper
from pythonFiles.g_text_inputs.a_textinput_standard import *
from pythonFiles.e_layouts.rel_top_bar import *

from pythonFiles.b_functions.a_screen_functions import *



class Login(Screen):

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)


        self.username = TextInput_Standard(.5, .7, False, "Username")
        self.password = TextInput_Standard(.5, .5, True, "Password")
        self.add_widget(self.username)
        self.add_widget(self.password)


        self.top_bar = Rel_TopBar("Login", False, False)
        self.add_widget(self.top_bar)



    def login(self):


        loginStatus = UserMapper.login_request(self.username.text, self.password.text)

        if loginStatus == "connection_failed":
            print("Connection failed")

        elif loginStatus == "select_command_failed":
            print("Select command failed")

        elif loginStatus == "credentials_failed":
            print("Credentials failed")

        elif loginStatus == "succes":
            self.manager.current = 'frontpage'

        else:
            print("Something went wrong")



    def save_as_previous_screen(self):

        save_screen_as_previous_screen("login")

        pass





