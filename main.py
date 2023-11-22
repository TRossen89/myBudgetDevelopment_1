
from kivy.app import App

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition


from pythonFiles.d_screens.screen_a_login import Login
from pythonFiles.d_screens.screen_b_create_user import CreateUser
from pythonFiles.d_screens.screen_c_frontpage import Frontpage

from pythonFiles.d_screens.screen_i_settings import SettingsMB
from pythonFiles.d_screens.screen_x_choose_language import ChooseLanguage

Window.size = (360, 600)

Builder.load_file('styling/file_loaded.kv')


class myBudgetDevelopmentApp(App):

    def build (self):

        myScreenManager = ScreenManager()

        myScreenManager.add_widget(Login(name="login"))
        myScreenManager.add_widget(CreateUser(name="create_user"))
        myScreenManager.add_widget(Frontpage(name="frontpage"))
        myScreenManager.add_widget(SettingsMB(name="settings_mb"))
        myScreenManager.add_widget(ChooseLanguage(name="choose_language"))

        myScreenManager.transition = NoTransition()

        Window.clearcolor = (.9, .8, .8, 1)


        return myScreenManager



if __name__ == '__main__':
    myBudgetDevelopmentApp().run()


