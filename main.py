from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from screens.splash_screen import SplashScreen
from screens.login_screen import LoginScreen


class MachChat(MDApp):

    def build(self):

        Builder.load_file("kv/splash.kv")
        Builder.load_file("kv/login.kv")

        sm = ScreenManager()

        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(LoginScreen(name="login"))

        return sm


if __name__ == "__main__":
    MachChat().run()