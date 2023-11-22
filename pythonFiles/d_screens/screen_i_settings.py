from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen

from pythonFiles.b_functions.a_app_language import get_app_language

from pythonFiles.e_layouts.rel_a_top_bar import *



class SettingsMB(Screen):

    def __init__(self, **kwargs):
        super(SettingsMB, self).__init__(**kwargs)

        self.main_frame_layout = SettingsMB_MainFrame()
        self.add_widget(self.main_frame_layout)


    def refresh_screen(self):

        self.clear_widgets()
        self.main_frame_layout.refresh_layout()
        self.add_widget(self.main_frame_layout)

    pass

    def save_as_previous_screen(self):

        save_screen_as_previous_screen("settings_mb")


    pass


class SettingsMB_MainFrame(RelativeLayout):

    width_of_labels = .38
    height_of_labels = .1

    x_space_between_describing_and_informing_labels = .1
    x_pos_of_all_describing_labels = .008

    x_pos_of_all_informing_labels = x_pos_of_all_describing_labels + width_of_labels + x_space_between_describing_and_informing_labels

    y_space_between_top_bar_and_first_label = .1


    def __init__(self, **kwargs):
        super(SettingsMB_MainFrame, self).__init__(**kwargs)

        self.refresh_layout()

    def refresh_layout(self):

        self.app_language = get_app_language()

        if self.app_language == "english":

            self.screen_text = "Settings"

            self.ids.language_describing_label.text = "Language"
            self.ids.language_informing_label.text = "English"
            pass


        elif self.app_language == "danish":

            self.screen_text = "Indstillinger"

            self.ids.language_describing_label.text = "Sprog"
            self.ids.language_informing_label.text = "Dansk"

            pass

        self.top_bar = Rel_TopBar(self.screen_text, True, True)
        self.add_widget(self.top_bar)




    pass