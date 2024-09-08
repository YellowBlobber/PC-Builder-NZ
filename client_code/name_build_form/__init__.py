from ._anvil_designer import name_build_formTemplate
from anvil import *

class name_build_form(name_build_formTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.build_name = None  # To store the name entered by the user

    def submit_button_click(self, **event_args):
        self.build_name = self.build_name_textbox.text
        if self.build_name:
            self.raise_event('x-close-alert')  # Close the alert when submit is clicked
        else:
            alert("Please enter a name for your build.")