from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

from pythonFiles.a_persistence.user_mapper import UserMapper


def width_of_TextInput_Standard():

    return .8

def height_of_TextInput_Standard():

    return .06


class TextInput_Standard(TextInput):

    def __init__(self, pos_x, pos_y, password = False, placeholder ="", width = .8, height = .06, check_username = False):
        super(TextInput_Standard, self).__init__()

        self.check_username = check_username

        self.password = password
        self.hint_text = placeholder
        self.pos_hint = {"center_x": pos_x, "top": pos_y}
        self.size_hint = (width, height)
       # self.size = (590, 80)


    def on_text_username_checking_if_username_exists(self):

        if self.check_username == True:

            print("on_text function in username text input is triggered")
            username_to_check = self.text
            print(username_to_check)

            username_in_db = UserMapper.is_username_in_db(username_to_check)

            if username_in_db == "no_username":
                self.foreground_color = (0, 0, 0, 1)
            else:
                self.foreground_color = (1, .2, .2, 1)


    pass
