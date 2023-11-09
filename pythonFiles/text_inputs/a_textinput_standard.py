from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

class RoundedTextInput(TextInput):
    def __init__(self, password, placeholder):
        super(RoundedTextInput, self).__init__()
        self.password = password
        self.hint_text = placeholder

    pass

class TextInput_Standard(RelativeLayout):

    def __init__(self, pos_x, pos_y, password, placeholder, width = .8, height = .06):
        super().__init__()

        self.pos_hint = {"center_x": pos_x, "top": pos_y}
        self.size_hint = (width, height)

        self.text_input = RoundedTextInput(password, placeholder)
        self.add_widget(self.text_input)

        #self.ids.text_input.pos_hint = {"center_x": .5, "center_y": .5}
        #self.ids.text_input.size_hint = (.8, .8)

        #self.opacity = .1


    def get_text(self):

        text = self.text_input.text

        return text