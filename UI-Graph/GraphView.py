from kivy.app import App
from math import sin
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.uix.widget import Widget
from kivy.clock import Clock
from queue import Queue
from Backend.RestClient import RestClient

server_url = ""


class Widgets(Widget):
    """ widgets holder """

    def __init__(self):
        super().__init__()
        # Restful client
        self.restClient = RestClient(server_url)
        # Arduino connector
        # self.arduinoConnector = ArduinoConnector()
        self.buffer = Queue()
        self.tick = 0
        self.plotter1 = MeshLinePlot(color=[1, 0, 0, 1])
        self.plotter2 = MeshLinePlot(color=[1, 0, 0, 1])
        self.ids.g1.add_plot(self.plotter1)
        self.ids.g2.add_plot(self.plotter2)
        self.event1 = None
        self.event2 = None

    def plot(self, *args):
        """ the method to plot the data from sensors """
        self.tick += 1
        self.plotter1.points = [(x, sin((x-self.tick) / 10.)) for x in range(0, 101)]
        self.plotter2.points = [(x, sin((x+self.tick) / 10.)) for x in range(0, 101)]
        print(self.tick)

    def start_sending(self):
        """ send data to the server """
        print("start_sending")
        while self.buffer.not_empty:
            json_data = self.buffer.get()
            self.restClient.post(json_data)

    def stop_sending(self):
        """ stop sending data"""
        self.event1.cancel()
        print("stop_sending")

    def start_reading(self):
        """ read data from the sensors """
        print("start_reading")
        self.event2 = Clock.schedule_interval(self.plot, 0.5)
        # json_data = arduinoConnector.read()
        # self.buffer.put(json_data)

    def stop_reading(self):
        """ stop reading """
        print("stop_reading")
        self.event2.cancel()
        pass


class ControllerApp(App):
    """ window application holder """
    def build(self):
        print("start!")
        widgets = Widgets()
        return widgets


if __name__ == '__main__':
    ControllerApp().run()
