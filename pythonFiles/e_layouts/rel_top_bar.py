from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior

from pythonFiles.c_pop_ups.pop_b_burger_menu import Pop_BurgerMenu
from pythonFiles.b_functions.b_screen_managing import *



class Rel_TopBar(RelativeLayout):

    def __init__(self, name_of_budget = "", back_arrow = True, burger_menu = True, **kwargs):
        super(Rel_TopBar, self).__init__(**kwargs)

        if back_arrow == False:
            self.ids.back_arrow.source = ""
            self.ids.back_arrow.disabled = True

        if burger_menu == False:
            self.ids.burger_menu.source = ""
            self.ids.burger_menu.disabled = True



        self.ids.budget_name.text = name_of_budget


    def update_previous_screen(self):
        self.previous_screen = get_previous_screen()


    def burger_menu_open(self):

        pop_burger_menu = Pop_BurgerMenu()
        pop_burger_menu.open()




    pass


class ImageButton(ButtonBehavior, Image):
    pass

