from kivy.uix.screenmanager import ScreenManager

from screens.splash_screen import SplashScreen
from screens.login_screen import LoginScreen
from screens.register_screen import RegisterScreen


class MachChatScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(SplashScreen(name="splash"))
        self.add_widget(LoginScreen(name="login"))
        self.add_widget(RegisterScreen(name="register"))