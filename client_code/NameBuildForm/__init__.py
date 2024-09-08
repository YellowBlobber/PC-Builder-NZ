from ._anvil_designer import NameBuildFormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class NameBuildForm(NameBuildFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.build_name = None  # To store the name entered by the user

    def submit_button_click(self, **event_args):
        self.build_name = self.build_name_textbox.text
        if self.build_name:
            self.raise_event('x-close-alert')  # Close the alert when submit is clicked
        else:
            alert("Please enter a name for your build.")  # Show alert if name is empty