from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDFlatButton

aPressed = 0
cPressed = 0
dPressed = 0
mPressed = 0
nsPressed = 0

a = 0
c = 0
d = 0
m = 0
ns = 0


class App(MDApp, TouchBehavior):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file('UI.kv')


class Alpha(MDFlatButton, TouchBehavior):
    def on_press(self, *args):
        global aPressed
        global a
        aPressed += 1
        a += 5

    def on_long_touch(self, *args):
        print("fuck you")

    def on_double_tap(self, *args):
        print("<on_double_tap> event")

    def on_triple_tap(self, *args):
        print("<on_triple_tap> event")


class Charlie(MDFlatButton, TouchBehavior):
    def on_long_touch(self, *args):
        print("<on_long_touch> event")

    def on_double_tap(self, *args):
        print("<on_double_tap> event")

    def on_triple_tap(self, *args):
        print("<on_triple_tap> event")


class Delta(MDFlatButton, TouchBehavior):
    def on_long_touch(self, *args):
        print("<on_long_touch> event")

    def on_double_tap(self, *args):
        print("<on_double_tap> event")

    def on_triple_tap(self, *args):
        print("<on_triple_tap> event")


class Mike(MDFlatButton, TouchBehavior):
    def on_long_touch(self, *args):
        print("<on_long_touch> event")

    def on_double_tap(self, *args):
        print("<on_double_tap> event")

    def on_triple_tap(self, *args):
        print("<on_triple_tap> event")


class NoShoot(MDFlatButton, TouchBehavior):
    def on_long_touch(self, *args):
        print("<on_long_touch> event")

    def on_double_tap(self, *args):
        print("<on_double_tap> event")

    def on_triple_tap(self, *args):
        print("<on_triple_tap> event")


class Reset(MDFlatButton, TouchBehavior):
    def on_long_touch(self, *args):
        print("<on_long_touch> event")


App().run()
