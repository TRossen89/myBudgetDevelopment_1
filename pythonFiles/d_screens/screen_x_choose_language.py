
from kivy.uix.screenmanager import Screen

from pythonFiles.b_functions.a_app_language import get_app_language

from pythonFiles.e_layouts.rel_a_top_bar import *
from pythonFiles.f_buttons.button_b_choose_languages import Button_ChooseLanguage


class ChooseLanguage(Screen):

    def __init__(self, **kwargs):
        super(ChooseLanguage, self).__init__(**kwargs)

        self.main_frame_layout = ChooseLanguage_MainFrame()
        self.add_widget(self.main_frame_layout)


    def refresh_screen(self):

        self.clear_widgets()
        self.main_frame_layout.refresh_layout()
        self.add_widget(self.main_frame_layout)

    pass

    def save_as_previous_screen(self):

        save_screen_as_previous_screen("settings")


    pass


class ChooseLanguage_MainFrame(RelativeLayout):

    width_of_language_buttons = .38
    height_of_language_buttons = .1


    x_pos_of_all_language_buttons = (width_of_language_buttons/2) + .01

    y_space_between_language_buttons = .1

    y_pos_danish_button = .88
    y_pos_english_button = y_pos_danish_button - height_of_language_buttons - y_space_between_language_buttons


    def __init__(self, **kwargs):
        super(ChooseLanguage_MainFrame, self).__init__(**kwargs)

        self.refresh_layout()

    def refresh_layout(self):

        self.app_language = get_app_language()

        if self.app_language == "english":

            self.screen_text = "Language"

            pass


        elif self.app_language == "danish":

            self.screen_text = "Sprog"


        self.danish_button = Button_ChooseLanguage("danish", ChooseLanguage_MainFrame.x_pos_of_all_language_buttons,
                                                   ChooseLanguage_MainFrame.y_pos_danish_button,
                                                   ChooseLanguage_MainFrame.width_of_language_buttons,
                                                   ChooseLanguage_MainFrame.height_of_language_buttons)

        self.english_button = Button_ChooseLanguage("english", ChooseLanguage_MainFrame.x_pos_of_all_language_buttons,
                                                    ChooseLanguage_MainFrame.y_pos_english_button,
                                                    ChooseLanguage_MainFrame.width_of_language_buttons,
                                                    ChooseLanguage_MainFrame.height_of_language_buttons)

        self.add_widget(self.danish_button)
        self.add_widget(self.english_button)

        self.top_bar = Rel_TopBar(self.screen_text, True, True)
        self.add_widget(self.top_bar)




    pass