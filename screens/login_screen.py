from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):

    def login(self):
        print("Login button clicked")

    def register(self):
        print("Go to Register Screen")