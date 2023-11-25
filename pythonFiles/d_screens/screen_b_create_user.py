
from kivy.uix.screenmanager import Screen

from pythonFiles.b_functions.a_app_language import *
from pythonFiles.b_functions.b_screens import *
from pythonFiles.c_pop_ups.pop_a_message import Pop_Message
from pythonFiles.e_layouts.rel_a_top_bar import *
from pythonFiles.g_text_inputs.text_input_a_standard import *
from pythonFiles.f_buttons.button_b_choose_languages import Button_ChooseLanguage





class CreateUser(Screen):


    def __init__(self, **kwargs):
        super(CreateUser, self).__init__(**kwargs)

        self.main_frame_layout = CreateUser_MainFrame()
        self.add_widget(self.main_frame_layout)


    def refresh_screen(self):

        self.clear_widgets()

        self.main_frame_layout.refresh_layout()
        self.add_widget(self.main_frame_layout)


    def save_as_previous_screen(self):

        save_screen_as_previous_screen("create_user")
        pass





class CreateUser_MainFrame(RelativeLayout):

    width_text_input_standard = width_of_TextInput_Standard()
    height_text_input_standard = height_of_TextInput_Standard()


    # Create user background box layout

    # - Dynamic

    create_user_box_width = .8
    create_user_box_height = .8

    create_user_box_pos_center_x = .5
    create_user_box_pos_top = .9

    create_user_box_corners_radius = 10



    # Enter username label

    # - Dynamic
    enter_username_label_width = width_text_input_standard
    enter_username_label_height = height_text_input_standard

    create_user_box_and_enter_username_label_y_space_between = .05


    # - Persistent
    enter_username_label_pos_center_x = create_user_box_pos_center_x
    enter_username_label_pos_top = create_user_box_pos_top - create_user_box_and_enter_username_label_y_space_between



    # Username text input

    # - Dynamic
    username_text_input_width = width_text_input_standard
    username_text_input_height = height_text_input_standard

    enter_username_label_and_username_text_input_y_space_between = .01


    # - Persistent
    username_text_input_pos_center_x = create_user_box_pos_center_x
    username_text_input_pos_top = enter_username_label_pos_top - enter_username_label_height \
                                  - enter_username_label_and_username_text_input_y_space_between


    # Enter password_1 label

    # - Dynamic
    enter_password_1_label_width = width_text_input_standard
    enter_password_1_label_height = height_text_input_standard

    enter_password_1_label_and_username_text_input_y_space_between = .05

    # - Persistent
    enter_password_1_label_pos_center_x = create_user_box_pos_center_x
    enter_password_1_label_pos_top = username_text_input_pos_top - username_text_input_height \
                                     - enter_password_1_label_and_username_text_input_y_space_between


    # Password_1_text_input

    # - Dynamic
    password_1_text_input_width = width_text_input_standard
    password_1_text_input_height = height_text_input_standard

    enter_password_1_label_and_password_1_text_input_y_space_between = .01

    # - Persistent
    password_1_text_input_pos_center_x = create_user_box_pos_center_x
    password_1_text_input_pos_top = enter_password_1_label_pos_top - enter_password_1_label_height \
                                  - enter_password_1_label_and_password_1_text_input_y_space_between


    # Enter password_2 label

    # - Dynamic
    enter_password_2_label_width = width_text_input_standard
    enter_password_2_label_height = height_text_input_standard

    enter_password_2_label_and_password_1_text_input_y_space_between = .05

    # - Persistent
    enter_password_2_label_pos_center_x = create_user_box_pos_center_x
    enter_password_2_label_pos_top = password_1_text_input_pos_top - password_1_text_input_height \
                                     - enter_password_2_label_and_password_1_text_input_y_space_between



    # Password_2_text_input

    # - Dynamic
    password_2_text_input_width = width_text_input_standard
    password_2_text_input_height = height_text_input_standard

    password_2_label_and_password_2_text_input_y_space_between = .01

    # - Persistent
    password_2_text_input_pos_center_x = create_user_box_pos_center_x
    password_2_text_input_pos_top = enter_password_2_label_pos_top - enter_password_2_label_height \
                                          - password_2_label_and_password_2_text_input_y_space_between



    # Create user button

    # - Dynamic
    create_user_button_width = .8
    create_user_button_height = .16

    create_user_button_and_password_2_text_input_y_space_between = .08

    # - Persistent
    create_user_button_pos_center_x = create_user_box_pos_center_x
    create_user_button_pos_top = password_2_text_input_pos_top - password_2_text_input_height - create_user_button_and_password_2_text_input_y_space_between



    def __init__(self, **kwargs):
        super(CreateUser_MainFrame, self).__init__(**kwargs)

        self.refresh_layout()

    pass



    def refresh_layout(self):

        self.app_language = get_app_language()

        if self.app_language == "english":

            self.refresh_text_at_layout("Create User", "Enter a username:", "Username", "Choose a password:",
                                        "Password", "Enter chosen password again:", "Password", "Create User")

        elif self.app_language == "danish":

            self.refresh_text_at_layout("Opret bruger", "Vælg et brugernavn:", "Brugernavn", "Vælg en kode:",
                                        "Kodeord", "Gentag kodeord:", "Kodeord", "Opret bruger")

        self.add_widget(self.top_bar)



        self.add_widget(self.username)
        self.add_widget(self.password_1)
        self.add_widget(self.password_2)


        pass


    def refresh_text_at_layout(self, top_bar_title, username_label, username_placeholder, password_1_label,
                               password_1_placeholder, password_2_label, password_2_placeholder, create_user_button):

        self.top_bar = Rel_TopBar(top_bar_title, True, False, True)
        self.ids.enter_username_label.text = username_label


        self.username = TextInput_Standard(CreateUser_MainFrame.username_text_input_pos_center_x,
                                           CreateUser_MainFrame.username_text_input_pos_top,
                                           False,
                                           username_placeholder,
                                           CreateUser_MainFrame.username_text_input_width,
                                           CreateUser_MainFrame.height_text_input_standard,
                                           True)



        self.ids.enter_password_label_1.text = password_1_label



        self.password_1 = TextInput_Standard(CreateUser_MainFrame.password_1_text_input_pos_center_x,
                                             CreateUser_MainFrame.password_1_text_input_pos_top,
                                             True, password_1_placeholder,
                                             CreateUser_MainFrame.password_1_text_input_width,
                                             CreateUser_MainFrame.password_1_text_input_height)


        self.ids.enter_password_label_2.text = password_2_label

        self.password_2 = TextInput_Standard(CreateUser_MainFrame.password_2_text_input_pos_center_x,
                                             CreateUser_MainFrame.password_2_text_input_pos_top,
                                             True, password_2_placeholder,
                                             CreateUser_MainFrame.password_2_text_input_width,
                                             CreateUser_MainFrame.password_2_text_input_height)


        self.ids.create_user_button.text = create_user_button




    def on_text_username_checking_if_username_exists(self, instance):

        print("Function is triggered")
        username_to_check = self.username.text
        username_in_db = UserMapper.is_username_in_db(username_to_check)

        if username_in_db == "no_username":
            pass
        else:
            self.username.foreground_color = (1, .2, .2, 1)



    def create_user(self):

        created_username = self.username.text
        created_password_1 = self.password_1.text
        created_password_2 = self.password_2.text

        self.app_language = get_app_language()

        if self.app_language == "english":

            pop_up_title = "Passwords not identical"
            pop_up_message = "Your entered passwords \naren't identical"

            pop_up_title_2 = "Connection failed"
            pop_up_message_2 = "You have no internet connection. You\nneed internet connection to create a user"

            pop_up_title_3 = "Username already in use"
            pop_up_message_3 = "The username you've chosen is already in use.\nPick another username"


        elif self.app_language == "danish":

            pop_up_title = "Kodeordene er ikke identiske"
            pop_up_message = "Dine indtastede kodeord \ner ikke ens"

            pop_up_title_2 = "Databaseforbindelsen fejlede"
            pop_up_message_2 = "Du har ikke internetforbindelse.\nDet kræver internetforbindelse at oprette \n" \
                               "en bruger og for at appen fungerer"

            pop_up_title_3 = "Brugernavn findes allerede"
            pop_up_message_3 = "Det valgte brugernavn er allerede i brug.\nVælg et andet brugernavn"



        if (created_password_1 != created_password_2):

            pop_up = Pop_Message(pop_up_title, pop_up_message)
            pop_up.open()


        else:
            create_user_status = UserMapper.create_user(created_username, created_password_1)

            if create_user_status == "connection_failed":

                pop_up_2 = Pop_Message(pop_up_title_2, pop_up_message_2)
                pop_up_2.open()


            elif create_user_status == "username_exists":

                pop_up_3 = Pop_Message(pop_up_title_3, pop_up_message_3)
                pop_up_3.open()
                print("Username already exists. Try again with another username")

            elif create_user_status == "insert_command_failed":
                print("Insert command failed")

            elif create_user_status == "succes":
                App.get_running_app().root.get_screen("create_user").manager.current = 'login'

            else:
                print("Something went wrong")

    pass