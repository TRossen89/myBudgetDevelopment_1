
from kivy.uix.popup import Popup


from pythonFiles.c_pop_ups.pop_c_logout import Pop_Logout

class Pop_BurgerMenu(Popup):

    font_size_of_title = 38

    height_of_buttons = .11
    with_of_buttons = .96

    y_space_between_buttons = .01

    y_space_from_button_top_to_button_top = height_of_buttons + y_space_between_buttons

    font_size_of_buttons = 28

    def __init__(self, **kwargs):
        super(Pop_BurgerMenu, self).__init__(**kwargs)

    def popup_logout(self):

        popup_logout = Pop_Logout()
        popup_logout.open()


    pass