from kivy.lang import Builder
from kivymd.app import MDApp

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


class App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file('UI.kv')

    def a_onpress(self):
        global aPressed
        global a
        aPressed += 1
        a += 5
        self.root.shot_count.text = f'A: {aPressed} C: {cPressed} D: {dPressed} M: {mPressed} NS: {nsPressed}'

    def c_onpress(self):
        global cPressed
        global c
        cPressed += 1
        c += 3
        self.root.shot_count.text = f'A: {aPressed} C: {cPressed} D: {dPressed} M: {mPressed} NS: {nsPressed}'

    def d_onpress(self):
        global dPressed
        global d
        dPressed += 1
        d += 1
        self.root.shot_count.text = f'A: {aPressed} C: {cPressed} D: {dPressed} M: {mPressed} NS: {nsPressed}'

    def m_onpress(self):
        global mPressed
        global m
        mPressed += 1
        m += 10
        self.root.shot_count.text = f'A: {aPressed} C: {cPressed} D: {dPressed} M: {mPressed} NS: {nsPressed}'

    def ns_onpress(self):
        global nsPressed
        global ns
        nsPressed += 1
        ns += 10
        self.root.shot_count.text = f'A: {aPressed} C: {cPressed} D: {dPressed} M: {mPressed} NS: {nsPressed}'

    def clear(self):
        global a
        global aPressed
        global c
        global cPressed
        global d
        global dPressed
        global m
        global mPressed
        global ns
        global nsPressed
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
        self.root.hf_field.text = "Hit Factor"
        self.root.time_field.text = ""
        self.root.shot_count.text = "Shot Counter"

    def calculate(self):
        global a
        global c
        global d
        global m
        global ns
        time_total = str(self.root.time_field.text)
        if time_total == "":
            self.root.hf_field.text = 'Enter Time'
        elif time_total == str(0):
            self.root.hf_field.text = 'Time Can Not Be Zero'
        else:
            point_total = a + c + d - m - ns
            if point_total <= 0:
                self.root.hf_field.text = "HF: 0.00"
            else:
                hit_factor = point_total / float(time_total)
                rounded_hitfactor = "{:.5f}".format(hit_factor)
                self.root.hf_field.text = f'HF: {rounded_hitfactor}'


App().run()
