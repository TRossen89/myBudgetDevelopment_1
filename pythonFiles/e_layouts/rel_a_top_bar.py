from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior

from pythonFiles.c_pop_ups.pop_b_burger_menu import Pop_BurgerMenu
from pythonFiles.c_pop_ups.pop_d_language_menu import Pop_LanguageMenu
from pythonFiles.b_functions.b_screens import *
from pythonFiles.f_buttons.button_b_choose_languages import Button_ChooseLanguage
from pythonFiles.b_functions.a_app_language import get_app_language
from pythonFiles.h_lists_and_dictionaries.a_list_screens import all_screens


class Rel_TopBar(RelativeLayout):

    def __init__(self, name_of_budget = "", back_arrow = True, burger_menu = True, language_menu = False,
                 title_of_language_menu = "Language", **kwargs):
        super(Rel_TopBar, self).__init__(**kwargs)

        self.language = get_app_language()

        if self.language == "english":

            self.popup_logout_title = "Logout"
            self.popup_logout_message = "Are you sure you want to log out?"
            self.popup_logout_yes_button = "Yes"
            self.popup_logout_cancel_button = "Cancel"

            self.create_budget_button = "Create Budget"
            self.your_budgets_button = "Your Budgets"
            self.advices_button = "Advices And Financial Guidance"
            self.how_to_make_money_button = "How To Make Money"
            self.learn_the_app_button = "Learn The App"
            self.settings_button = "Settings"
            self.your_account_button = "Your Account"
            self.logout_button = "Log out"
            self.logout_title = "Log out"
            self.logout_message = "Are you sure you want to log out?"
            self.logout_yes_button = "Yes"
            self.logout_cancel_button = "Cancel"


        elif self.language == "danish":

            self.create_budget_button = "Opret budget"
            self.your_budgets_button = "Dine budgetter"
            self.advices_button = "Råd og finansiel hjælp"
            self.how_to_make_money_button = "Hvordan man kan tjene penge"
            self.learn_the_app_button = "Lær appen"
            self.settings_button = "Indstillinger"
            self.your_account_button = "Din konto"
            self.logout_button = "Log ud"

            self.popup_logout_title = "Log ud"
            self.popup_logout_message = "Er du sikker på du vil logge ud?"
            self.popup_logout_yes_button = "Ja"
            self.popup_logout_cancel_button = "Cancel"

        self.title_of_language_menu = title_of_language_menu

        if back_arrow == False:
            self.ids.back_arrow.source = ""
            self.ids.back_arrow.disabled = True

        if burger_menu == False:
            self.ids.burger_menu.source = ""
            self.ids.burger_menu.disabled = True



        if language_menu == True:
            #self.ids.language_menu.text = "Language"
            #self.ids.language_menu.disabled = False

            # Dynamic
            buttons_width = .1
            buttons_height = .8
            buttons_font_size = 18

            buttons_x_space_between = .02


            danish_button_pos_center_x = .82

            # Persistent
            english_button_pos_center_x = danish_button_pos_center_x + buttons_width + buttons_x_space_between
            buttons_pos_top = 1 - ((1 - buttons_height) / 2)

            self.danish_button = Button_ChooseLanguage("danish", danish_button_pos_center_x, buttons_pos_top, buttons_width,
                                                       buttons_height, buttons_font_size)

            self.english_button = Button_ChooseLanguage("english", english_button_pos_center_x, buttons_pos_top, buttons_width,
                                                        buttons_height, buttons_font_size)

            self.add_widget(self.danish_button)
            self.add_widget(self.english_button)


        self.ids.budget_name.text = name_of_budget


    def get_previous_screen(self):

        self.current_screen = get_current_screen()
        self.previous_screen = get_previous_screen()

        self.list_of_screens = all_screens

        #self.current_screen_id = 0
        #self.previous_screen_id = 0

        for screen in self.list_of_screens:

            if self.current_screen == screen:
                self.current_screen_id = self.list_of_screens.index(screen)

            if self.previous_screen == screen:
                self.previous_screen_id = self.list_of_screens.index(screen)


        if self.current_screen_id > self.previous_screen_id:
            pass
        elif self.current_screen_id == self.previous_screen_id:
            print(self.current_screen_id-1)
            self.previous_screen = self.list_of_screens[self.current_screen_id-1]






    def burger_menu_open(self):

        # TODO: Finish making this pop up language sensitive
        #self.language = get_app_language()

        #if self.language == "english":


        pop_burger_menu = Pop_BurgerMenu(self.create_budget_button, self.your_budgets_button, self.advices_button,
                                         self.how_to_make_money_button, self.learn_the_app_button, self.settings_button,
                                         self.your_account_button, self.logout_button, self.popup_logout_title,
                                         self.popup_logout_message, self.popup_logout_yes_button, self.popup_logout_cancel_button)

        pop_burger_menu.open()


    def language_menu_open(self):

        self.language = get_app_language()

        if self.language == "english":

            self.popup_logout_title = "Logout"
            self.popup_logout_message = "Are you sure you want to log out?"
            self.popup_logout_yes_button = "Yes"
            self.popup_logout_cancel_button = "Cancel"

            self.create_budget_button = "Create Budget"
            self.your_budgets_button = "Your Budgets"
            self.advices_button = "Advices And Financial Guidance"
            self.how_to_make_money_button = "How To Make Money"
            self.learn_the_app_button = "Learn The App"
            self.settings_button = "Settings"
            self.your_account_button = "Your Account"
            self.logout_button = "Log out"
            self.logout_title = "Log out"
            self.logout_message = "Are you sure you want to log out?"
            self.logout_yes_button = "Yes"
            self.logout_cancel_button = "Cancel"


        elif self.language == "danish":

            self.create_budget_button = "Opret budget"
            self.your_budgets_button = "Dine budgetter"
            self.advices_button = "Råd og finansiel hjælp"
            self.how_to_make_money_button = "Hvordan man kan tjene penge"
            self.learn_the_app_button = "Lær appen"
            self.settings_button = "Indstillinger"
            self.your_account_button = "Din konto"
            self.logout_button = "Log ud"

            self.popup_logout_title = "Log ud"
            self.popup_logout_message = "Er du sikker på du vil logge ud?"
            self.popup_logout_yes_button = "Ja"
            self.popup_logout_cancel_button = "Cancel"

        popup_language_menu = Pop_LanguageMenu(self.title_of_language_menu)
        popup_language_menu.open()




    pass


class ImageButton(ButtonBehavior, Image):
    pass

