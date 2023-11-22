
from kivy.uix.popup import Popup
from pythonFiles.b_functions.d_current_user import *



class Pop_Logout(Popup):

    def logout(self):

        set_current_user(0)
    pass