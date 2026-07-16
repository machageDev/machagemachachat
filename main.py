from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from screens.splash_screen import SplashScreen
from screens.login_screen import LoginScreen
from screens.screen_manager import MachChatScreenManager

class MachChat(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        Builder.load_file("kv/splash.kv")
        Builder.load_file("kv/login.kv")

        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(LoginScreen(name="login"))

        return MachChatScreenManager()


MachChat().run()