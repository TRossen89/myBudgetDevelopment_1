from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen

from pythonFiles.b_functions.a_app_language import get_app_language
from pythonFiles.b_functions.d_current_user import get_current_user
from pythonFiles.c_pop_ups.pop_c_logout import Pop_Logout
from pythonFiles.e_layouts.rel_a_top_bar import *




class Frontpage(Screen):

    def __init__(self, **kwargs):
        super(Frontpage, self).__init__(**kwargs)

        self.main_frame_layout = Frontpage_MainFrame()

        #self.add_widget(self.main_frame_layout)


    def refresh_screen(self):

        self.clear_widgets()
        self.main_frame_layout.refresh_layout()
        self.add_widget(self.main_frame_layout)

    pass

    def save_as_current_screen(self):
        set_current_screen("frontpage")

    def save_as_previous_screen(self):

        save_screen_as_previous_screen("frontpage")

        pass


class Frontpage_MainFrame(RelativeLayout):


    # BACKGROUND BOX layout

    # - Dynamic
    background_box_width = .9
    background_box_height = .9
    background_box_pos_center_x = .5
    background_box_pos_top = .925


    # - ALL BUTTONS

    # - Dynamic
    all_buttons_width = .86
    all_buttons_height = .08

    all_buttons_and_background_box_y_space_between = .02
    all_buttons_y_space_between = .02


    # - Persistent
    all_buttons_pos_center_x = background_box_pos_center_x

    all_buttons_reference_pos_top = background_box_pos_top - all_buttons_and_background_box_y_space_between
    all_buttons_from_top_to_top_space = all_buttons_height + all_buttons_y_space_between



    def __init__(self, **kwargs):
        super(Frontpage_MainFrame, self).__init__(**kwargs)


    def refresh_layout(self):

        user = get_current_user()
        if user == 0:
            pass
        else:
            user_name = user[1]

            self.top_bar = Rel_TopBar(user_name, False, True, False)
            self.add_widget(self.top_bar)



        self.app_language = get_app_language()

        if self.app_language == "english":

            self.ids.create_budget_button.text = "Create Budget"
            self.ids.your_budgets_button.text = "Your Budgets"
            self.ids.advices_and_financial_guidance_button.text = "Advices And Financial Guidance"
            self.ids.how_to_make_money_button.text = "How To Make Money"
            self.ids.learn_the_app_button.text = "Learn The App"
            self.ids.settings_button.text = "Settings"
            self.ids.your_account_button.text = "Your Account"
            self.ids.logout_button.text = "Log out"

            self.logout_popup_title = "Logout"
            self.logout_popup_message = "Are you sure want to log out?"
            self.logout_popup_yes_button = "Yes"
            self.logout_popup_no_button = "Cancel"




        elif self.app_language == "danish":

            self.ids.create_budget_button.text = "Opret nyt budget"
            self.ids.your_budgets_button.text = "Dine budgetter"
            self.ids.advices_and_financial_guidance_button.text = "Råd og finansiel hjælp"
            self.ids.how_to_make_money_button.text = "Hvordan man kan tjene penge"
            self.ids.learn_the_app_button.text = "Lær appen"
            self.ids.settings_button.text = "Indstillinger"
            self.ids.your_account_button.text = "Din konto"
            self.ids.logout_button.text = "Log ud"

            self.logout_popup_title = "Log ud"
            self.logout_popup_message = "Er du sikker på du vil logge ud?"
            self.logout_popup_yes_button = "Ja"
            self.logout_popup_no_button = "Cancel"


    def logout(self):

        self.popup_logout = Pop_Logout(self.logout_popup_title, self.logout_popup_message,
                                       self.logout_popup_yes_button, self.logout_popup_no_button)
        self.popup_logout.open()



    pass