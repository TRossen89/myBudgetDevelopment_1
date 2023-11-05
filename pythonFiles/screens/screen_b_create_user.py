from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import NumericProperty
from pythonFiles.persistence.user_mapper import UserMapper
from pythonFiles.persistence.db_connection import DBConnection

class CreateUser(Screen):

    # Create user box
    width_of_create_user_box = NumericProperty(.8)
    height_of_create_user_box = NumericProperty(.8)
    y_pos_of_create_user_box = NumericProperty(.9)

    # Password box
    width_of_password_box = NumericProperty(1)
    height_of_password_box = NumericProperty(.6)
    y_pos_of_password_box = NumericProperty(.68)

    # Top label
    y_pos_of_top_label = NumericProperty(.9)

    # Space between a label describing af text input and the text input described
    y_space_between_label_and_text_input = NumericProperty(.07)

    # Space between [password label and text input 1] and [password label and text input 2]
    y_space_between_password_1_and_2 = NumericProperty(.055)

    # Height of all text inputs in screen
    height_of_text_inputs = NumericProperty(0.06)

    # Y position of create user button relative to elements above (the higher number the lower it's placed)
    y_pos_create_user_button = NumericProperty(.1)


    def create_user(self):

        created_username = self.ids.username.text
        created_password_1 = self.ids.password_1.text
        created_password_2 = self.ids.password_2.text

        if (created_password_1 != created_password_2):
            print("The two passwords entered was different from each other. They should be identical")

        else:
            create_user_status = UserMapper.create_user_request(created_username, created_password_1)

            if create_user_status == "connection_failed":
                print("Connection failed")

            elif create_user_status == "username_exists":
                print("Username already exists. Try again with another username")

            elif create_user_status == "insert_command_failed":
                print("Insert command failed")

            elif create_user_status == "succes":
                self.manager.current = 'login'

            else:
                print("Something went wrong")

    pass