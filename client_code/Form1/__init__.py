from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def stock_display_8_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

# Hello :) This is your application's concience talking, I wan't 
