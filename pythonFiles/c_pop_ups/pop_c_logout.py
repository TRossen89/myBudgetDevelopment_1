
from kivy.uix.popup import Popup
from pythonFiles.b_functions.d_current_user import *



class Pop_Logout(Popup):

    def __init__(self, title, message, yes_button, cancel_button, **kwargs):
        super(Pop_Logout, self).__init__(**kwargs)

        self.title = title
        self.ids.message.text = message
        self.ids.yes_button.text = yes_button
        self.ids.cancel_button.text = cancel_button

    def logout(self):

        set_current_user(0)
    pass