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

    def save_as_previous_screen(self):

        save_screen_as_previous_screen("frontpage")

        pass


class Frontpage_MainFrame(RelativeLayout):

    ########################################
    # -- SPACES:

    y_space_between_all_buttons = NumericProperty(.04)


    ########################################
    # -- BOXES (LAYOUTS):

    # The layout framing all the buttons
    width_of_all_buttons_box = NumericProperty(.9)
    height_of_all_buttons_box = NumericProperty(.9)
    y_pos_of_all_buttons_box = NumericProperty(.925)


    ########################################
    # -- BUTTONS

    height_of_all_buttons = NumericProperty(.08)
    width_of_all_buttons = NumericProperty(.8)


    def __init__(self, **kwargs):
        super(Frontpage_MainFrame, self).__init__(**kwargs)


    def refresh_layout(self):

        user = get_current_user()
        if user == 0:
            pass
        else:
            user_name = user[1]

            self.top_bar = Rel_TopBar(user_name, False)
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



        elif self.app_language == "danish":

            self.ids.create_budget_button.text = "Opret nyt budget"
            self.ids.your_budgets_button.text = "Dine budgetter"
            self.ids.advices_and_financial_guidance_button.text = "Råd og finansiel hjælp"
            self.ids.how_to_make_money_button.text = "Hvordan man kan tjene penge"
            self.ids.learn_the_app_button.text = "Lær appen"
            self.ids.settings_button.text = "Indstillinger"
            self.ids.your_account_button.text = "Din konto"
            self.ids.logout_button.text = "Log ud"


    def logout(self):

        self.popup_logout = Pop_Logout()
        self.popup_logout.open()



    pass