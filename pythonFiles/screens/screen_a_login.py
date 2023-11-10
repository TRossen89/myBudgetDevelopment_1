from kivy.uix.screenmanager import Screen
#from pythonFiles.persistence.db_connection import DBConnection
from pythonFiles.persistence.user_mapper import UserMapper
from pythonFiles.text_inputs.a_textinput_standard import *



class Login(Screen):

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)


        self.username = TextInput_Standard(.5, .7, False, "Username")
        self.password = TextInput_Standard(.5, .5, True, "Password")

        self.add_widget(self.username)
        self.add_widget(self.password)


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

    pass



