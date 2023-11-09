from kivy.uix.screenmanager import Screen
#from pythonFiles.persistence.db_connection import DBConnection
from pythonFiles.persistence.user_mapper import UserMapper
from pythonFiles.text_inputs.a_textinput_standard import TextInput_Standard



class Login(Screen):

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)

        self.username = TextInput_Standard(.5, .7, False, "Username")
        self.password = TextInput_Standard(.5, .5, True, "Password")

        self.add_widget(self.username)
        self.add_widget(self.password)


    def login(self):

        #TextInput:
         #   id: username
          #  pos_hint: {"center_x": .5, "center_y":.7}
           # size_hint: (.6, .07)

        #TextInput:
         #   id: password
          #  pos_hint: {"center_x": .5, "center_y":.5}
           # size_hint: (.6, .07)




        #username = self.ids.username.text
        #password = self.ids.password.text


        loginStatus = UserMapper.login_request(self.username.get_text(), self.password.get_text())

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



