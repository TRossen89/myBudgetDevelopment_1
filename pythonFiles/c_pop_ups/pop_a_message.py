
from kivy.uix.popup import Popup



class Pop_Message(Popup):

    def __init__(self, popup_title, message, size_hint_y = .5, size_hint_x = .8):
        super().__init__()

        self.size_hint = (size_hint_x, size_hint_y)

        # Setting size of label and button so it is the same size no matter the chosen size of the pop_up
        self.ids.ok_button.size_hint = (.4, .1/size_hint_y)
        self.ids.message.size_hint = (1, .1/size_hint_y)

        self.title = popup_title
        self.ids.message.text = message


    pass