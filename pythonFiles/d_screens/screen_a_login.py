from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
#from pythonFiles.a_persistence.db_connection import DBConnection
from pythonFiles.a_persistence.user_mapper import UserMapper

from pythonFiles.c_pop_ups.pop_a_message import Pop_Message
from pythonFiles.g_text_inputs.text_input_a_standard import *
from pythonFiles.e_layouts.rel_a_top_bar import *

from pythonFiles.b_functions.b_screens import *
from pythonFiles.b_functions.a_app_language import *
from pythonFiles.b_functions.d_current_user import *



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


    # -- LANGUAGE BUTTONS

    language_buttons_height = .03
    language_buttons_width = .1
    language_buttons_pos_top = .94
    language_buttons_move_to_the_right = .00
    language_buttons_move_to_the_left = .285

    english_button_pos_center_x = .85
    danish_button_pos_center_x = .73


    # -- BIG BUTTONS

    #all_big_buttons_height = .06

    #
    why_budget_and_trailer_buttons_height = .042
    why_budget_and_trailer_buttons_width = .55
    why_budget_and_trailer_buttons_pos_center_x = .5
    why_budget_and_trailer_buttons_y_space_between = .02
    why_budget_and_trailer_buttons_move_up = .03
    why_budget_and_trailer_buttons_move_down = .00
    why_budget_and_trailer_buttons_font_size = 30

    why_budget_button_pos_top = .85
    trailer_button_pos_top = .79


    #
    login_box_layout_width = .88
    login_box_layout_height = .66
    login_box_layout_pos_center_x = .5
    login_box_layout_pos_top = .7

    #
    login_label_pos_top = .96
    login_label_width = .6/login_box_layout_width
    login_label_height = .04/login_box_layout_height
    login_label_font_size = 40


    #
    text_input_standard_height = height_of_TextInput_Standard()
    text_input_standard_width = width_of_TextInput_Standard()

    username_password_text_inputs_height = text_input_standard_height / login_box_layout_height
    username_password_text_inputs_width = text_input_standard_width / login_box_layout_width
    username_password_text_inputs_y_space_between = .12

    username_password_text_inputs_pos_center_x = .5

    y_space_between_forgot_password_and_password_text_input = .002

    # Username text input top controls top of password text input (and labels connected to the two text inputs)
    username_text_input_pos_top = .76

    password_text_input_pos_top = username_text_input_pos_top - username_password_text_inputs_height - username_password_text_inputs_y_space_between

    #
    login_and_create_user_buttons_height = .06/login_box_layout_height
    login_and_create_user_buttons_pos_center_x = .5
    login_and_create_user_buttons_y_space_between = .04
    login_and_create_user_buttons_move_up = .2
    login_and_create_user_buttons_move_down = .14


    login_and_create_user_buttons_font_size = 38

    login_button_width = .35/login_box_layout_width
    create_user_button_width = .6/login_box_layout_width


    login_button_pos_top = .3
    create_user_button_pos_top = .18

    or_label_pos_top = .24


    def __init__(self, **kwargs):
        super(Login_MainFrame, self).__init__(**kwargs)

        # TODO: Remove this. It's there to remind me to check if you can set the id of a layout like it's done here
        #self.id = "login_main_frame"

        self.refresh_layout()



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


    def refresh_layout(self):

        self.app_language = get_app_language()

        if self.app_language == "english":

            self.popup_forgot_password_title = "Reset password"
            self.popup_forgot_password_message = "Do you want to reset your password?"

            self.top_bar = Rel_TopBar("Login", False, False)

            self.ids.why_make_a_budget_button.text = "Why Make A Budget?"
            self.ids.see_app_trailer_button.text = "See app trailer"

            self.ids.login_label.text = "Login"
            self.ids.enter_username_label.text = "Enter username:"
            self.ids.enter_password_label.text = "Enter password:"

            self.username = TextInput_Standard(Login_MainFrame.username_password_text_inputs_pos_center_x,
                                               Login_MainFrame.username_text_input_pos_top, False, "Username",
                                               Login_MainFrame.username_password_text_inputs_width,
                                               Login_MainFrame.username_password_text_inputs_height)
            self.password = TextInput_Standard(Login_MainFrame.username_password_text_inputs_pos_center_x,
                                               Login_MainFrame.password_text_input_pos_top, True, "Password",
                                               Login_MainFrame.username_password_text_inputs_width,
                                               Login_MainFrame.username_password_text_inputs_height)

            #self.ids.forgot_password_label.text = "[ref=forgot password]Forgot password[/ref]"
            self.ids.forgot_password_button.text = "Forgot password"

            self.ids.create_user_button.text = "Create User"
            self.ids.or_label.text = "or"
            self.ids.login_button.text = "Log in"


        elif self.app_language == "danish":

            self.top_bar = Rel_TopBar("Login", False, False)

            self.popup_forgot_password_title = "Nulstil kodeord"
            self.popup_forgot_password_message = "Indtast din mail, så sender vi et link," \
                                                 "\nhvor du kan nulstille dit kodeord"

            self.ids.why_make_a_budget_button.text = "Hvorfor lave et budget?"
            self.ids.see_app_trailer_button.text = "Se app trailer"

            self.ids.login_label.text = "Login"
            self.ids.enter_username_label.text = "Indtast brugernavn:"
            self.ids.enter_password_label.text = "Indtast kodeord:"

            self.username = TextInput_Standard(Login_MainFrame.username_password_text_inputs_pos_center_x,
                                               Login_MainFrame.username_text_input_pos_top, False, "Brugernavn",
                                               Login_MainFrame.username_password_text_inputs_width,
                                               Login_MainFrame.username_password_text_inputs_height)
            self.password = TextInput_Standard(Login_MainFrame.username_password_text_inputs_pos_center_x,
                                               Login_MainFrame.password_text_input_pos_top, True, "Kodeord",
                                               Login_MainFrame.username_password_text_inputs_width,
                                               Login_MainFrame.username_password_text_inputs_height)

            #self.ids.forgot_password_label.text = "[ref=glemt kodeord]Glemt kodeord[/ref]"
            self.ids.forgot_password_button.text = "Glemt kodeord"

            self.ids.create_user_button.text = "Opret bruger"
            self.ids.or_label.text = "eller"
            self.ids.login_button.text = "Log på"

        self.add_widget(self.top_bar)

        self.ids.login_box_layout.add_widget(self.username)
        self.ids.login_box_layout.add_widget(self.password)



    def login(self):

        app_language = get_app_language()

        if app_language == "english":



            title_connection_error = "Connection error"
            message_connection_error = "MyBudget couldn't connect\n" \
                      "to the database"

            title_sql_SELECT_error = "Conncetion error"
            message_sql_SELECT_error = "Something went wrong with the\n" \
                                     "connection to the database"

            title_credentials = "Credentials error"
            message_credentials = "You've entered af wrong\n username or password"



        elif app_language == "danish":



            title_connection_error = "Fejl med forbindelsen"
            message_connection_error = "MyBudget kunne ikke forbinde\n" \
                      "til databasen"

            title_sql_SELECT_error = "Fejl med forbindelsen"
            message_sql_SELECT_error = "Noget gik galt med forbindelsen\n" \
                                       "til databasen"

            title_credentials = "Login-fejl"
            message_credentials = "Du har indtastet et forkert\nbrugernavn eller kodeord"


        loginStatus = UserMapper.login_request(self.username.text, self.password.text)


        if loginStatus == "connection_failed":

            pop_up_message_1 = Pop_Message(title_connection_error, message_connection_error)
            pop_up_message_1.open()

            print("Connection failed")

        elif loginStatus == "select_command_failed":

            pop_up_message_2 = Pop_Message(title_sql_SELECT_error, message_sql_SELECT_error)
            pop_up_message_2.open()
            print("Select command failed")

        elif loginStatus == "credentials_failed":

            pop_up_message_3 = Pop_Message(title_credentials, message_credentials)
            pop_up_message_3.open()
            print("Credentials failed")

        elif loginStatus == "succes":
            App.get_running_app().root.get_screen("frontpage").refresh_screen()
            App.get_running_app().root.get_screen("login").manager.current = 'frontpage'

        else:
            print("Something went wrong")


    # ############ Is this necessary? ############################################
    # TODO: Figure out if it's necessary to save frontpage as previous screen when the user is logging in
    save_screen_as_previous_screen("frontpage")
    ##############################################################################
    pass


    def reset_password_popup(self):

        popup_reset_password = Pop_Message(self.popup_forgot_password_title, self.popup_forgot_password_message)
        popup_reset_password.open()

        self.ids.forgot_password_button.color = (0, 0, 0, 1)

    def on_press_color(self):
        self.ids.forgot_password_button.color = (.1, .1, 1, 1)
