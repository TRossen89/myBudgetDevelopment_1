from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import NumericProperty
from pythonFiles.a_persistence.user_mapper import UserMapper

from pythonFiles.c_pop_ups.pop_a_message import Pop_Message
from pythonFiles.e_layouts.rel_top_bar import *

class CreateUser(Screen):

    #######################################
    # -- ELEMENTS:

    # Top label
    y_pos_of_top_label = NumericProperty(.9)

    # Height of all text inputs in screen
    height_of_text_inputs = NumericProperty(0.06)

    # Y position of create user button relative to elements above (the higher the NumberProperty is the lower the button
    # is placed)
    y_pos_create_user_button = NumericProperty(.1)


    ########################################
    # -- SPACES:

    # Space between a label describing af text input and the text input described
    y_space_between_label_and_text_input = NumericProperty(.07)

    # Space between [password label and text input 1] and [password label and text input 2]
    y_space_between_password_1_and_2 = NumericProperty(.055)


    ########################################
    # -- BOXES (LAYOUTS):

    # The layout framing the create user elements
    width_of_create_user_box = NumericProperty(.8)
    height_of_create_user_box = NumericProperty(.8)
    y_pos_of_create_user_box = NumericProperty(.9)

    # The layout with the two password labels and text inputs
    width_of_password_box = NumericProperty(1)
    height_of_password_box = NumericProperty(.6)
    y_pos_of_password_box = NumericProperty(.68)


    def __init__(self, **kwargs):
        super(CreateUser, self).__init__(**kwargs)


        self.top_bar = Rel_TopBar("Create User", True, False)
        self.add_widget(self.top_bar)


    def save_as_previous_screen(self):

        save_screen_as_previous_screen("create_user")
        pass


    def create_user(self):

        created_username = self.ids.username.text
        created_password_1 = self.ids.password_1.text
        created_password_2 = self.ids.password_2.text


        if (created_password_1 != created_password_2):

            pop_up_title = "Passwords not identical"
            pop_up_message = "Your entered passwords \naren't identical"

            pop_up = Pop_Message(pop_up_title, pop_up_message)
            pop_up.open()


        else:
            create_user_status = UserMapper.create_user(created_username, created_password_1)

            if create_user_status == "connection_failed":

                pop_up_title_2 = "Connection failed"
                pop_up_message_2 = "You have no internet connection. You\nneed internet connection to create a user"

                pop_up_2 = Pop_Message(pop_up_title_2, pop_up_message_2)
                pop_up_2.open()


            elif create_user_status == "username_exists":
                print("Username already exists. Try again with another username")

            elif create_user_status == "insert_command_failed":
                print("Insert command failed")

            elif create_user_status == "succes":
                self.manager.current = 'login'

            else:
                print("Something went wrong")

    pass