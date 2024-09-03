from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from random import choice
import anvil.media
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    #self.populate_categories(**properties)
    pcs = app_files.pc_builder_nz
    
    self.worksheet = pcs[0]
    print(self.worksheet.fields)
    sheet_data_cpu = anvil.server.call('get_sheet_data_cpus')
    sheet_data_gpu = anvil.server.call('get_sheet_data_gpu')
    categories_cpu = anvil.server.call('get_unique_categories',sheet_data_cpu)
    categories_gpu = anvil.server.call('get_unique_categories',sheet_data_gpu)
    self.cpu_dropdown.items = categories_cpu
    self.gpu_dropdown.items = categories_gpu
   
   # Any code you write here will run before the form opens.
  

 

  def stock_display_8_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def cpu_dropdown_change(self, **event_args):
    selected_category = self.cpu_dropdown.selected_value
    items = anvil.server.call('get_items', selected_category)
    self.items_dropdown.items = items


  def cpu_dropdown_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
  pass
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

  pass

  def cpu_cooler_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def gpu_dropdown_change(self, **event_args):
    selected_category = self.gpu_dropdown.selected_value
    items = anvil.server.call('get_items', selected_category)
    self.items_dropdown.items = items

