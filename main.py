
from kivy.app import App

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition
#from kivy.uix.tabbedpanel import TabbedPanel

from pythonFiles.screens.screen_a_login import Login
from pythonFiles.screens.screen_b_create_user import CreateUser
from pythonFiles.screens.screen_c_frontpage import Frontpage



Window.size = (360, 600)

Builder.load_file('styling/file_loaded.kv')


class myBudgetDevelopmentApp(App):

    def build (self):

        myScreenManager = ScreenManager()

        myScreenManager.add_widget(Login(name="login"))
        myScreenManager.add_widget(CreateUser(name="create_user"))
        myScreenManager.add_widget(Frontpage(name="frontpage"))

        myScreenManager.transition = NoTransition()

        Window.clearcolor = (.9, .8, .8, 1)

        return myScreenManager



if __name__ == '__main__':
    myBudgetDevelopmentApp().run()


