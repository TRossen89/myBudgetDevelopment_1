
from kivy.uix.button import Button
from pythonFiles.b_functions.a_app_language import set_app_language
from pythonFiles.b_functions.b_screens import refresh_all_screens




class Button_ChooseLanguage(Button):


    def __init__(self, language, center_x = .8, top= .94, width = .1, height = .03, font_size = 16, **kwargs):
        super(Button_ChooseLanguage, self).__init__(**kwargs)


        self.language = language

        if self.language == "danish":
            self.text = "Dansk"
        elif self.language =="english":
            self.text = "English"

        self.pos_hint = {"center_x": center_x, "top": top}
        self.size_hint = (width, height)
        self.font_size = font_size


    def english_as_language(self):

        #self.language = "english"
        set_app_language(self.language)

        refresh_all_screens()



    def danish_as_language(self):

        #self.language = "danish"
        set_app_language(self.language)

        refresh_all_screens()


