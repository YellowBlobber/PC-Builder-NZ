from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def stock_display_8_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def cpu_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def cpu_dropdown_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
  pass