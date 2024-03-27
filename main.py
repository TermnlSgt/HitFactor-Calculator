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

# shot_count = f' A: {aPressed} C: {cPressed}'


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
        print(aPressed, a)

    def on_long_touch(self, *args):
        global aPressed
        global a
        aPressed = 0
        a = 0
        print(aPressed, a)


class Charlie(MDFlatButton, TouchBehavior):

    def on_press(self, *args):
        global cPressed
        global c
        cPressed += 1
        c += 5
        print(cPressed, c)

    def on_long_touch(self, *args):
        global cPressed
        global c
        cPressed = 0
        c = 0
        print(cPressed, c)


class Delta(MDFlatButton, TouchBehavior):

    def on_press(self, *args):
        global dPressed
        global d
        dPressed += 1
        d += 5

    def on_long_touch(self, *args):
        print("<on_long_touch> event")


class Mike(MDFlatButton, TouchBehavior):

    def on_press(self, *args):
        global mPressed
        global m
        mPressed += 1
        m += 5

    def on_long_touch(self, *args):
        print("<on_long_touch> event")


class NoShoot(MDFlatButton, TouchBehavior):

    def on_press(self, *args):
        global nsPressed
        global ns
        nsPressed += 1
        ns += 5

    def on_long_touch(self, *args):
        print("<on_long_touch> event")


class Reset(MDFlatButton, TouchBehavior):
    def on_long_touch(self, *args):
        global a, aPressed, c, cPressed, d, dPressed, m, mPressed, ns, nsPressed
        a = 0
        aPressed = 0
        c = 0
        cPressed = 0
        d = 0
        dPressed = 0
        m = 0
        mPressed = 0
        ns = 0
        nsPressed = 0


App().run()
