from kivy.uix.screenmanager import Screen
from kivy.clock import Clock


class SplashScreen(Screen):

    def on_enter(self):
        Clock.schedule_once(self.goto_login, 2)

    def goto_login(self, *args):
        self.manager.current = "login"