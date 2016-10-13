from kivy.app import App
from math import sin
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.uix.widget import Widget
from kivy.clock import Clock


class Widgets(Widget):
    tick = 0

    def __init__(self):
        super().__init__()

        self.plotter1 = MeshLinePlot(color=[1, 0, 0, 1])
        self.plotter2 = MeshLinePlot(color=[1, 0, 0, 1])
        self.ids.g1.add_plot(self.plotter1)
        self.ids.g2.add_plot(self.plotter2)
        self.event1 = None
        self.event2 = None

    def plot(self, *args):
        self.tick += 1
        self.plotter1.points = [(x, sin((x-self.tick) / 10.)) for x in range(0, 101)]
        self.plotter2.points = [(x, sin((x+self.tick) / 10.)) for x in range(0, 101)]
        print(self.tick)

    def start_sending(self):
        self.event1 = Clock.schedule_interval(self.plot, 0.5)
        print("start_sending")
        pass

    def stop_sending(self):
        self.event1.cancel()
        print("stop_sending")
        pass

    def start_reading(self):
        #Clock.schedule_interval(self.plot, 0.5)
        print("start_reading")
        pass

    def stop_reading(self):
        #Clock.schedule_interval(self.plot, 0.5)
        print("stop_reading")
        pass


class ControllerApp(App):
    def build(self):
        print("start!")
        widgets = Widgets()
        #Clock.schedule_interval(widgets.plot, 0.5)
        return widgets


if __name__ == '__main__':
    ControllerApp().run()
