from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.logger import Logger

Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Image:
            source: 'pi.jpg'
            y: self.parent.y + self.parent.height -475
            x: self.parent.x
            size_hint_y: .7
            pos_hint: {'x':.01, 'y':.2}
            allow_stretch: True
        Button:
            text: 'Settings'
            text_size: self.size
            halign: 'center'
            valign: 'middle'
            text_hint: (.5,.5)
            size_hint: .5,.13
            pos_hint: {'x':.5, 'y':0}
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Music Selection'
            text_size: self.size
            halign: 'center'
            valign: 'middle'
            text_hint: (.5,.5)
            size_hint: .5, .13
            pos: 0,0
            on_press: root.manager.current = 'music'

<SettingsScreen>
    BoxLayout:
        Button:
            text: 'Options'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'


<MusicScreen>
    BoxLayout:
        orientation: 'vertical'
        Label: 
            canvas.before:
                Color:
                    rgb: 250, 250, 250
                Rectangle:
                    pos: self.pos
                    size: self.size
            color: 0,0,0,1
            bold: True
            font_size: self.height/2
            text: 'Music List'
            text_hint: .5, .5
            halign: 'center'
            valign: 'middle'
            text_size: self.size
            size_hint: 1, .2

        GridLayout:
            rows: 2
            cols: 3
            Button:
                text: 'The Girl from Ipanema'
                text_size: self.size
                text_hint: .5, .5
                halign: 'center'
                valign: 'middle'
                on_press: root.manager.current = 'instrument'
            Button: 
                text: 'Giant Steps'
                text_size: self.size
                text_hint: .5, .5
                halign: 'center'
                valign: 'middle'
                on_press: root.manager.current = 'instrument'
            Button: 
                text: 'How High the Moon'
                text_size: self.size
                text_hint: .5, .5
                halign: 'center'
                valign: 'middle'
                on_press: root.manager.current = 'instrument'
            Button: 
                text: 'Blues for Alice'
                text_size: self.size
                text_hint: .5, .5
                halign: 'center'
                valign: 'middle'
                on_press: root.manager.current = 'instrument'
            Button: 
                text: 'Straight, No Chaser'
                text_size: self.size
                text_hint: .5, .5
                halign: 'center'
                valign: 'middle'
                on_press: root.manager.current = 'instrument'
            Button:
                text: 'Mr. P.C.'
                text_size: self.size
                text_hint: .5, .5
                halign: 'center'
                valign: 'middle'
                on_press: root.manager.current = "instrument"
        GridLayout:
            rows:1
            cols:5
            size_hint: 1,.15
            Button:
                text: 'Menu'
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text_hint: .5,.5
                size_hint: .2,.15
                on_press: root.manager.current = 'menu'

<Instrument>
    BoxLayout:
        orientation: 'vertical'
        Label:
            canvas.before:
                Color:
                    rgb: 250, 250, 250
                Rectangle:
                    pos: self.pos
                    size: self.size
            color: 0,0,0,1
            bold: True
            font_size: self.height/2
            text: 'Music List'
            text_hint: .5, .5
            halign: 'center'
            valign: 'middle'
            text_size: self.size
            size_hint: 1, .2
            text: 'Choose your instrument'
            text_hint: .5, .5
            halign: 'center'
            valign: 'middle'
            text_size: self.size
            size_hint: 1, .15
        GridLayout:
            rows: 4
            cols: 2
            Button:
                text: 'Alto Sax'
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text_hint: .5, .5
                size_hint: .5, .15
                #:set instr1 "Alto"
            Button:
                text: 'Tenor Sax'
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text_hint: .5, .5
                size_hint: .5, .15
                #:set instr2 "Tenor"
            Button:
                text: 'Soprano Sax'
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text_hint: .5, .5
                size_hint: .5, .15
                #:set instr3 "Soprano"
            Button:
                text: 'Baritone Sax'
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text_hint: .5, .5
                size_hint: .5, .15
                #:set instr4 "Baritone"
            Button:
                text: 'Trumpet'
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text_hint: .5, .5
                size_hint: .5, .15
                #:set instr5 "Trumpet"
            Button:
                text: 'Clarinet'
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text_hint: .5, .5
                size_hint: .5, .15
                #:set instr6 "Clarinet"
            Button:
                text: 'Flute'
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text_hint: .5, .5
                size_hint: .5, .15
                #:set instr7 "Flute"
            Button:
                text: 'Guitar'
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text_hint: .5, .5
                size_hint: .5, .15
                #:set instr8 "Guitar"
        Button:
            text: 'Back'
            text_size: self.size
            halign: 'center'
            valign: 'middle'
            text_hint: .5,.5
            size_hint: 1, .15
            on_press: root.manager.current = 'menu'


<OptionsScreen>
    GridLayout:
        rows: 1
        Button:
            text: 'options'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Calibrate'

""")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class MusicScreen(Screen):
    pass

class OptionsScreen(Screen):
    pass

class Instrument(Screen):
    pass



sm = ScreenManager(transition=SlideTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(MusicScreen(name='music'))
sm.add_widget(OptionsScreen(name='options'))

sm.add_widget(Instrument(name='instrument'))

class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
