from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.google.drive import app_files
from random import choice
import anvil.media
import anvil.server



class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.populate_categories()

    

    # Any code you write here will run before the form opens.
  def populate_categories(self):
    categories = anvil.server.call('get_categories')
    self.category_dropdown.items = categories

  def stock_display_8_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def cpu_dropdown_change(self, **event_args):
   selected_category = self.category_dropdown.selected_value
   items = anvil.server.call('get_items', selected_category)
   self.items_dropdown.items = items
  pass

  def cpu_dropdown_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
  pass
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

  pass
t