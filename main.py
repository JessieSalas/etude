from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.logger import Logger

import os
import random
import etude_class
from chords import songs


Builder.load_string("""
#:import good etude_class 
#:import command subprocess.call 
#: import songs chords.songs

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



<SongButton@Button>: 
    #define template for what the song buttons have in common
    text_size: self.size
    text_hint: .5, .5
    halign: 'center'
    valign: 'middle'
     

<MusicScreen>
    dream: _dream
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
         
            SongButton:
                text: 'The Girl from Ipanema'
                id: _dream
                on_press: dream = songs['Girl From Ipanema'] 
                on_press: root.manager.current = 'instrument'         
                

            SongButton: 
                text: 'Giant Steps'
                on_press: root.manager.current = 'instrument'

            SongButton: 
                text: 'How High the Moon'
                on_press: root.manager.current = 'instrument'

            SongButton: 
                text: 'Blues for Alice'
                on_press: root.manager.current = 'instrument'

            SongButton: 
                text: 'Straight, No Chaser'
                on_press: root.manager.current = 'instrument'

            SongButton:
                text: 'Mr. P.C.'
                on_press: root.manager.current = 'instrument'

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

<InstrButton@Button>:
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    text_hint: .5, .5
    size_hint: .5, .15

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
            InstrButton:
                text: 'Alto Sax'
                on_press: #:set instrument sax_notes
                on_press: print(instrument)
                on_press: good.do(root.dream)
                on_press: command(["lilypond", "raw.lily"])
            InstrButton:
                text: 'Tenor Sax'
                #:set instr2 "Tenor"
            InstrButton:
                text: 'Soprano Sax'
                #:set instr3 "Soprano"
            InstrButton:
                text: 'Baritone Sax'
                #:set instr4 "Baritone"
            InstrButton:
                text: 'Trumpet'
                #:set instr5 "Trumpet"
            InstrButton:
                text: 'Clarinet'
                #:set instr6 "Clarinet"
            InstrButton:
                text: 'Flute'
                #:set instr7 "Flute"
            InstrButton:
                text: 'Guitar'
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

class Instrument(MusicScreen):
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
    def clean(self,instance, note):
        return etude_class.clean(self.note)
    def generate_scale(self, kind, instrument_notes, starting_note):
        return etude_class.generate_scale(self.kind, self.instrument_notes, self.starting_note)
    def parse(self, instance):
        etude_class.parse()
    def write(self, instance):
        etude_class.write()
    

if __name__ == '__main__':
    TestApp().run()
