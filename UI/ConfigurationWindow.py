from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


class ConfigurationWidgets(Widget):
    selected_port = None
    port_list_dropdown = None
    port_selection_button = None
    connected = False

    def __init__(self):
        super().__init__()

        # Widget Settings
        Window.size = (800, 500)
        Config.set('graphics', 'resizable', '0')

        # Setup dropdown
        self.port_list_dropdown = DropDown()
        self.port_list_dropdown.bind(on_select=lambda instance, x: setattr(self.port_selection_button, 'text', x))
        self.port_selection_button = Button(text="<Select Port>", size_hint=(None, None), size=(200, 50),
                                            pos_hint=(None, None), pos=(250, 350))
        self.port_selection_button.bind(on_release=self.port_list_dropdown.open)

        # Setup dropdown list
        for index in range(10):
            button = Button(text="test %d" % index, size_hint=(None, None), size=(200, 50))
            button.bind(on_release=lambda btn: self.port_list_dropdown.select(btn.text))
            self.port_list_dropdown.add_widget(button)

        # Add dropdown to the widget
        Widget.add_widget(self, widget=self.port_selection_button)

    def connect_to_arduino(self):
        pass

    def flash_arduino(self):
        pass

    def show_data(self):
        pass


class ConfigurationApp(App):
    def build(self):
        widgets = ConfigurationWidgets()
        return widgets

if __name__ == '__main__':
    ConfigurationApp().run()
