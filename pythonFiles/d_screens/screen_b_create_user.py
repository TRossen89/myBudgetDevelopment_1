from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import NumericProperty
from pythonFiles.a_persistence.user_mapper import UserMapper
from pythonFiles.b_functions.a_app_language import *
from pythonFiles.b_functions.c_refreshing_screens import *
from pythonFiles.c_pop_ups.pop_a_message import Pop_Message
from pythonFiles.e_layouts.rel_top_bar import *
from pythonFiles.g_text_inputs.a_textinput_standard import *




class CreateUser(Screen):


    def __init__(self, **kwargs):
        super(CreateUser, self).__init__(**kwargs)

        self.main_frame_layout = CreateUser_MainFrame()
        self.add_widget(self.main_frame_layout)


    def refresh_screen(self):
        self.clear_widgets()
        self.add_widget(self.main_frame_layout)


    def save_as_previous_screen(self):

        save_screen_as_previous_screen("create_user")
        pass





class CreateUser_MainFrame(RelativeLayout):

    width_TextInput_Standard = width_of_TextInput_Standard()
    height_TextInput_Standard = height_of_TextInput_Standard()


    #######################################
    # -- ELEMENTS:

    # Top label
    #y_pos_of_top_label = NumericProperty(.9)
    y_pos_of_top_label = .9

    # Height of all text inputs in screen
    #height_of_text_inputs = NumericProperty(0.06)
    height_of_text_inputs = .06

    # Y position of create user button relative to elements above (the higher the NumberProperty is the lower the button
    # is placed)
    #y_pos_create_user_button = NumericProperty(.1)
    y_pos_create_user_button = .1

    ########################################
    # -- SPACES:

    # Space between a label describing af text input and the text input described
    #y_space_between_label_and_text_input = NumericProperty(.07)
    y_space_between_label_and_text_input = .07

    # Space between [password label and text input 1] and [password label and text input 2]
    #y_space_between_password_1_and_2 = NumericProperty(.055)
    y_space_between_password_1_and_2 = .055

    ########################################
    # -- BOXES (LAYOUTS):

    # The layout framing the create user elements
    #width_of_create_user_box = NumericProperty(.8)
    width_of_create_user_box = .8

    #height_of_create_user_box = NumericProperty(.8)
    height_of_create_user_box = .8

    #y_pos_of_create_user_box = NumericProperty(.9)
    y_pos_of_create_user_box = .9

    # The layout with the two password labels and text inputs
    #width_of_password_box = NumericProperty(1)
    width_of_password_box = 1
    #height_of_password_box = NumericProperty(.6)
    height_of_password_box = .6

    #y_pos_of_password_box = NumericProperty(.68)
    y_pos_of_password_box = .68

    def __init__(self, **kwargs):
        super(CreateUser_MainFrame, self).__init__(**kwargs)

        self.refresh_layout()

    pass

    def english_as_language(self):

        language = "english"
        set_app_language(language)

        refresh_all_screens()

        pass



    def danish_as_language(self):

        language = "danish"
        set_app_language(language)

        refresh_all_screens()

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

        self.ids.create_user_box.add_widget(self.username)
        self.ids.password_box.add_widget(self.password_1)
        self.ids.password_box.add_widget(self.password_2)


        pass


    def refresh_text_at_layout(self, top_bar_title, username_label, username_placeholder, password_1_label,
                               password_1_placeholder, password_2_label, password_2_placeholder, create_user_button):

        self.top_bar = Rel_TopBar(top_bar_title, True, False)
        self.ids.enter_username_label.text = username_label

        pos_y_of_username_text_input_1 = CreateUser_MainFrame.y_pos_of_top_label \
                                         - CreateUser_MainFrame.y_space_between_label_and_text_input

        self.username = TextInput_Standard(.5, pos_y_of_username_text_input_1,
                                           False, username_placeholder,
                                           CreateUser_MainFrame.width_TextInput_Standard
                                           / CreateUser_MainFrame.width_of_create_user_box,
                                           CreateUser_MainFrame.height_TextInput_Standard
                                           / CreateUser_MainFrame.height_of_create_user_box)

        self.ids.enter_password_label_1.text = password_1_label

        pos_y_of_password_1_text_input = \
            1 - (CreateUser_MainFrame.y_space_between_label_and_text_input
                 / CreateUser_MainFrame.height_of_password_box)

        self.password_1 = TextInput_Standard(.5, pos_y_of_password_1_text_input,
                                             True, password_1_placeholder,
                                             CreateUser_MainFrame.width_TextInput_Standard
                                             / CreateUser_MainFrame.width_of_create_user_box
                                             / CreateUser_MainFrame.width_of_password_box,
                                             CreateUser_MainFrame.height_TextInput_Standard
                                             / CreateUser_MainFrame.height_of_create_user_box
                                             / CreateUser_MainFrame.height_of_password_box)

        self.ids.enter_password_label_2.text = password_2_label

        self.password_2 = TextInput_Standard(.5, 1 - (3 * (
                CreateUser_MainFrame.y_space_between_label_and_text_input
                / CreateUser_MainFrame.height_of_password_box))
                                             - CreateUser_MainFrame.y_space_between_password_1_and_2,
                                             True, password_2_placeholder,
                                             CreateUser_MainFrame.width_TextInput_Standard
                                             / CreateUser_MainFrame.width_of_create_user_box
                                             / CreateUser_MainFrame.width_of_password_box,
                                             CreateUser_MainFrame.height_TextInput_Standard
                                             / CreateUser_MainFrame.height_of_create_user_box
                                             / CreateUser_MainFrame.height_of_password_box)

        self.ids.create_user_button.text = create_user_button






    def create_user(self):

        created_username = self.username.text
        created_password_1 = self.password_1.text
        created_password_2 = self.password_2.text


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
                App.get_running_app().root.get_screen("create_user").manager.current = 'login'

            else:
                print("Something went wrong")

    pass