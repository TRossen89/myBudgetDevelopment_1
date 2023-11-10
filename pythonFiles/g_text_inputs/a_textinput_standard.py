from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

class TextInput_Standard(TextInput):

    def __init__(self, pos_x, pos_y, password = False, placeholder ="", width = .8, height = .06):
        super(TextInput_Standard, self).__init__()

        self.password = password
        self.hint_text = placeholder
        self.pos_hint = {"center_x": pos_x, "top": pos_y}
        self.size_hint = (width, height)

    pass
