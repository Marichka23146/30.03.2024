from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout


class FirstScreen(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='horizontal')
        
        btn1 = Button(text="First button!")
        btn1.bind(on_press=self.next)
        layout.add_widget(btn1)
        
        btn2 = Button(text="Second button!")
        btn2.bind(on_press=self.next2)
        layout.add_widget(btn2)

        btn3 = Button(text="Third button!")
        btn3.bind(on_press=self.next3)
        layout.add_widget(btn3)

        btn4 = Button(text="Fourth button!")
        btn4.bind(on_press=self.next4)
        layout.add_widget(btn4)
        
        btn5 = Button(text="Fifth button!")
        btn4.bind(on_press=self.next4)
        layout.add_widget(btn5)

        self.add_widget(layout)

    def next(self, instance):
        self.manager.transition.direction = "up"
        self.manager.current = "second"

    def next2(self, instance):
        self.manager.transition.direction = "up"
        self.manager.current = "third"

    def next3(self, instance):
        self.manager.transition.direction = "up"
        self.manager.current = "fourth"

    def next4(self, instance):
        self.manager.transition.direction = "up"
        self.manager.current = "fifth"

def next4(self, instance):
        self.manager.transition.direction = "up"
        self.manager.current = "firth"
        
def go_back(self, instance):
        self.manager.transition.direction = "down"
        self.manager.current = "first"


class SecondScreen(Screen):
    def __init__(self, name="second"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='horizontal')
        
        label = Label(text="Конституція України була прийнята 28 червня 1996 року")
        btn_back = Button(text="Go back to First")
        btn_back.bind(on_press=self.go_back)
        
        layout.add_widget(label)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.transition.direction = "down"
        self.manager.current = "first"


class ThirdScreen(Screen):
    def __init__(self, name="third"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='horizontal')
        
        label = Label(text="Акт проголошення незалежності України 24 серпня 1991 року")
        btn_back = Button(text="Go back to First")
        btn_back.bind(on_press=self.go_back)
        
        layout.add_widget(label)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.transition.direction = "down"
        self.manager.current = "first"



class FourthScreen(Screen):
    def __init__(self, name="fourth"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='horizontal')
        
        label = Label(text="Історія- це наука що вивчає минуле людства")
        btn_back = Button(text="Go back to First")
        btn_back.bind(on_press=self.go_back)
        
        layout.add_widget(label)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.transition.direction = "down"
        self.manager.current = "first"

        

class FifthScreen(Screen):
    def __init__(self, name="fifth"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='horizontal')
        
        label = Label(text="Початок повномасштабного вторгнення РФ в Україну 24 лютого 2022")
        btn_back = Button(text="Go back to First")
        btn_back.bind(on_press=self.go_back)
        
        layout.add_widget(label)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.transition.direction = "down"
        self.manager.current = "first"

        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(FourthScreen())
        sm.add_widget(FifthScreen())
        return sm


MyApp().run()
