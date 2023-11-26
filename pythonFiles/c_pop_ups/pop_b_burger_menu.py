
from kivy.uix.popup import Popup


from pythonFiles.c_pop_ups.pop_c_logout import Pop_Logout

class Pop_BurgerMenu(Popup):

    font_size_of_title = 38

    height_of_buttons = .11
    with_of_buttons = .96

    y_space_between_buttons = .01

    y_space_from_button_top_to_button_top = height_of_buttons + y_space_between_buttons

    font_size_of_buttons = 28

    def __init__(self, create_budget, your_budgets, advices, how_to_make_money,
                 learn_the_app, settings, your_account, logout, logout_title, logout_message,
                 logout_yes_button, logout_cancel_button, **kwargs):
        super(Pop_BurgerMenu, self).__init__(**kwargs)

        self.ids.create_budget.text = create_budget
        self.ids.your_budgets.text = your_budgets
        self.ids.advices.text = advices
        self.ids.how_to_make_money.text = how_to_make_money
        self.ids.learn_the_app.text = learn_the_app
        self.ids.settings.text = settings
        self.ids.your_account.text = your_account
        self.ids.log_out.text = logout

        self.logout_title = logout_title
        self.logout_message = logout_message
        self.logout_yes_button = logout_yes_button
        self.logout_cancel_button = logout_cancel_button

    def popup_logout(self):

        popup_logout = Pop_Logout(self.logout_title, self.logout_message, self.logout_yes_button, self.logout_cancel_button)
        popup_logout.open()


    pass