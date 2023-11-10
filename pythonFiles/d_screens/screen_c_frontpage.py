from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen
from pythonFiles.e_layouts.rel_top_bar import *



class Frontpage(Screen):

    ########################################
    # -- SPACES:

    y_space_between_all_buttons = NumericProperty(.03)


    ########################################
    # -- BOXES (LAYOUTS):

    # The layout framing all the buttons
    width_of_all_buttons_box = NumericProperty(.9)
    height_of_all_buttons_box = NumericProperty(.92)
    y_pos_of_all_buttons_box = NumericProperty(.94)


    ########################################
    # -- BUTTONS

    height_of_all_buttons = NumericProperty(.08)
    width_of_all_buttons = NumericProperty(.8)


    def __init__(self, **kwargs):
        super(Frontpage, self).__init__(**kwargs)

        self.top_bar = Rel_TopBar("myBudget", False, False)
        self.add_widget(self.top_bar)


    def save_as_previous_screen(self):

        save_screen_as_previous_screen("frontpage")

        pass

    pass