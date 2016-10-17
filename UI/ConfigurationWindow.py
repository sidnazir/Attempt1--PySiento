from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import serial.tools.list_ports as ports
import os

'''
This Class is the LoadDialog. This allows the user to select a file
to flash the Arduino with.
'''


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


'''
This class contains all the widgets for the configuration view.
'''


class ConfigurationWidgets(Widget):
    list_of_ports = None
    selected_port = None
    port_list_dropdown = None
    port_selection_button = None
    flash_file = None
    connected = False
    load_file_button = None
    load_popup = None

    def __init__(self):
        super().__init__()

        # Get all the serial ports
        list_of_ports = ports.comports()

        # Widget Settings
        Window.size = (800, 500)
        Config.set('graphics', 'resizable', '0')

        # Setup dropdown
        self.port_list_dropdown = DropDown()
        self.port_list_dropdown.bind(on_select=lambda instance, x: self.set_port_button_text(x))

        # Create the port selection button to open the dropdown
        self.port_selection_button = Button(text="<Select Port>", size_hint=(None, None), size=(400, 50),
                                            pos_hint=(None, None), pos=(50, 350))
        self.port_selection_button.bind(on_release=self.port_list_dropdown.open)

        # Setup dropdown list
        for port in list_of_ports:
            button = Button(text="%s" % port.device, size_hint=(None, None), size=(400, 50))
            button.bind(on_release=lambda btn: self.port_selected(btn.text))
            self.port_list_dropdown.add_widget(button)

        # Add dropdown to the widget
        Widget.add_widget(self, widget=self.port_selection_button)

        # Create the button for loading file to flash from
        self.load_file_button = Button(text="<Select File>", size_hint=(None, None), size=(400, 50),
                                       pos_hint=(None, None), pos=(50, 250))
        self.load_file_button.bind(on_release=lambda btn: self.show_load_dialog())

        # Add load file button to the widget
        Widget.add_widget(self, widget=self.load_file_button)

    '''
    Store the selected port in a variable when a port is selected from the dropdown.
    '''
    def port_selected(self, text):
        self.selected_port = text
        self.port_list_dropdown.select(text)

    '''
    Set the text on the port button
    '''
    def set_port_button_text(self, text):
        setattr(self.port_selection_button, 'text', text)

    '''
    Show the dialog to load the file to flash the Arduino with.
    '''
    def show_load_dialog(self):
        content = LoadDialog(load=self.load_file, cancel=self.cancel_load)
        self.load_popup = Popup(title="Load flash file", content=content,
                                size_hint=(0.9, 0.9), auto_dismiss=False)
        self.load_popup.open()
        pass

    '''
    Load the file currently highlighted on the file dialog.
    '''
    def load_file(self, path, filename):
        self.flash_file = os.path.join(path, filename[0])
        display_text = filename[0]
        length = len(display_text)
        if length > 20:
            display_text = "..." + display_text[length - 20:length - 1]
        setattr(self.load_file_button, 'text', display_text)
        self.load_popup.dismiss()

    '''
    Abort the file loading process.
    '''
    def cancel_load(self):
        self.load_popup.dismiss()

    '''
    Connect to the selected port.
    '''
    def connect_to_arduino(self):
        no_port_selected_popup = Popup(title='Error', content=Label(text='No port selected'),
                                       size_hint=(None, None), size=(300, 150))
        connection_error_popup = Popup(title='Error', content=Label(text='Error connecting to device'),
                                       size_hint=(None, None), size=(300, 150))
        if self.selected_port is None:
            no_port_selected_popup.open()
        else:
            try:
                # Connect to the Arduino using the Arduino Connector
                # Pass the port to the arduino connector
                # If connection succeeds, set 'self.connected = True'
                pass
            except:
                connection_error_popup.open()

    '''
    Flash the Arduino with the selected file.
    '''
    def flash_arduino(self):
        no_file_selected_popup = Popup(title='Error', content=Label(text='No file selected'),
                                       size_hint=(None, None), size=(300, 150))
        flash_error_popup = Popup(title='Error', content=Label(text='Error flashing device'),
                                  size_hint=(None, None), size=(300, 150))
        no_connection_established_popup = Popup(title='Error', content=Label(text='No connection established'),
                                                size_hint=(None, None), size=(300, 150))
        if self.flash_file is None:
            no_file_selected_popup.open()
        elif not self.connected:
            no_connection_established_popup.open()
        else:
            try:
                # Try flashing the Arduino using the Arduino Uploader
                # Pass the file path to the Arduino Uploader
                pass
            except:
                flash_error_popup.open()

    '''
    Once the Arduino is selected and connected to, start showing the data received from it.
    '''
    def show_data(self):
        no_connection_established_popup = Popup(title='Error', content=Label(text='No connection established'),
                                                size_hint=(None, None), size=(300, 150))
        show_data_error_popup = Popup(title='Error', content=Label(text='Error showing data'),
                                      size_hint=(None, None), size=(300, 150))
        if not self.connected:
            no_connection_established_popup.open()
        else:
            try:
                # Try going to the next screen and showing data
                pass
            except:
                show_data_error_popup.open()

'''
This class is the Configuration app.
When it is built, it returns all the widgets in the configuration widgets.
'''


class ConfigurationApp(App):
    def build(self):
        widgets = ConfigurationWidgets()
        return widgets

'''
This runs the configuration app.
'''

if __name__ == '__main__':
    ConfigurationApp().run()
