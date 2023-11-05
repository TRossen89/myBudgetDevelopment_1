from kivy.uix.screenmanager import Screen
#from pythonFiles.persistence.db_connection import DBConnection
from pythonFiles.persistence.user_mapper import UserMapper



class Login(Screen):


    def login(self):

        username = self.ids.username.text
        password = self.ids.password.text


        loginStatus = UserMapper.login_request(username, password)

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



