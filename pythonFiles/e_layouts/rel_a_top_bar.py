from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior

from pythonFiles.c_pop_ups.pop_b_burger_menu import Pop_BurgerMenu
from pythonFiles.c_pop_ups.pop_d_language_menu import Pop_LanguageMenu
from pythonFiles.b_functions.b_screens import *
from pythonFiles.f_buttons.button_b_choose_languages import Button_ChooseLanguage


class Rel_TopBar(RelativeLayout):

    def __init__(self, name_of_budget = "", back_arrow = True, burger_menu = True, language_menu = False,
                 title_of_language_menu = "Language", **kwargs):
        super(Rel_TopBar, self).__init__(**kwargs)

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


    def update_previous_screen(self):
        self.previous_screen = get_previous_screen()


    def burger_menu_open(self):

        pop_burger_menu = Pop_BurgerMenu()
        pop_burger_menu.open()

    def language_menu_open(self):

        popup_language_menu = Pop_LanguageMenu(self.title_of_language_menu)
        popup_language_menu.open()




    pass


class ImageButton(ButtonBehavior, Image):
    pass

