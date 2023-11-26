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

    def save_as_current_screen(self):
        set_current_screen("settings_mb")


    def save_as_previous_screen(self):

        save_screen_as_previous_screen("settings_mb")


    pass


class SettingsMB_MainFrame(RelativeLayout):


    # ALL BACKGROUND BUTTONS

    # - Dynamic

    all_background_buttons_width = 1
    all_background_buttons_height = .06

    all_background_buttons_pos_center_x = .5


    # - Persistent

    # ALL DESCRIBING LABELS

    # - Dynamic
    all_describing_labels_width = .38
    all_describing_labels_height = .06

    all_describing_labels_pos_x = .06


    # ALL INFORMING LABELS

    # - Dynamic

    all_informing_labels_width = .35

    informing_labels_and_describing_labels_x_space_between = .08

    # - Persistent
    all_informing_labels_height = all_describing_labels_height

    all_informing_labels_pos_x = all_describing_labels_pos_x + all_describing_labels_width \
                                 + informing_labels_and_describing_labels_x_space_between


    # ALL LABELS

    # - Dynamic
    first_label_and_top_bar_y_space_between = .1

    all_labels_y_space_between = .02

    # - Persistent
    all_labels_reference_pos_top = 1 - first_label_and_top_bar_y_space_between
    all_labels_from_top_to_top_space = all_describing_labels_height + all_labels_y_space_between



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