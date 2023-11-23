from kivy.uix.popup import Popup

from pythonFiles.b_functions.a_app_language import get_app_language
from pythonFiles.f_buttons.button_b_choose_languages import Button_ChooseLanguage


class Pop_LanguageMenu(Popup):


    def __init__(self, title, **kwargs):
        super(Pop_LanguageMenu, self).__init__(**kwargs)

        self.title = title

        # Dynamic
        buttons_width = .96
        buttons_height = .11
        buttons_font_size = 28

        buttons_y_space_between = .28

        danish_button_pos_top = .98

        # Persistent
        english_button_pos_top = danish_button_pos_top - buttons_y_space_between


        self.danish_button = Button_ChooseLanguage("danish", .5, danish_button_pos_top, buttons_width,
                                                   buttons_height, buttons_font_size)

        self.english_button = Button_ChooseLanguage("english", .5, english_button_pos_top, buttons_width,
                                                    buttons_height, buttons_font_size)

        self.ids.main_frame.add_widget(self.danish_button)
        self.ids.main_frame.add_widget(self.english_button)








