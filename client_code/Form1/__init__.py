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

    self.component_prices = {}
    
    self.worksheet = pcs[0]
    print(self.worksheet.fields)
    
    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for cpus, then popluates the dropdown with the called items
    sheet_data_cpu = anvil.server.call('get_sheet_data_cpus')
    categories_cpu = anvil.server.call('get_unique_categories',sheet_data_cpu)
    self.cpu_dropdown.items = categories_cpu
    
    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for gpu, then popluates the dropdown with the called items
    sheet_data_gpu = anvil.server.call('get_sheet_data_gpu')
    categories_gpu = anvil.server.call('get_unique_categories',sheet_data_gpu)
    self.gpu_dropdown.items = categories_gpu
    
    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_motherbrd = anvil.server.call('get_sheet_data_motherbrd')
    categories_motherbrd = anvil.server.call('get_unique_categories',sheet_data_motherbrd)
    self.motherboard_dropdown.items = categories_motherbrd    
    
    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_case = anvil.server.call('get_sheet_data_case')
    categories_case = anvil.server.call('get_unique_categories',sheet_data_case)
    self.case_dropdown.items = categories_case 

    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_ram = anvil.server.call('get_sheet_data_ram')
    categories_ram = anvil.server.call('get_unique_categories',sheet_data_ram)
    self.ram_dropdown.items = categories_ram 

    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_storage = anvil.server.call('get_sheet_data_storage')
    categories_storage = anvil.server.call('get_unique_categories',sheet_data_storage)
    self.storage_dropdown.items = categories_storage 
    
    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_storage_2 = anvil.server.call('get_sheet_data_storage')
    categories_storage_2 = anvil.server.call('get_unique_categories',sheet_data_storage_2)
    self.storage_2_dropdown.items = categories_storage_2 
    
    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_storage_3 = anvil.server.call('get_sheet_data_storage')
    categories_storage_3 = anvil.server.call('get_unique_categories',sheet_data_storage_3)
    self.storage_3_dropdown.items = categories_storage_3  
    
    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_fans = anvil.server.call('get_sheet_data_fans')
    categories_fans = anvil.server.call('get_unique_categories',sheet_data_fans)
    self.fans_dropdown.items = categories_fans 

    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_case = anvil.server.call('get_sheet_data_case')
    categories_case = anvil.server.call('get_unique_categories',sheet_data_case)
    self.case_dropdown.items = categories_case 

    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_cpu_cooler = anvil.server.call('get_sheet_data_cpu_cooler')
    categories_cpu_cooler = anvil.server.call('get_unique_categories',sheet_data_cpu_cooler)
    self.cpu_cooler_dropdown.items = categories_cpu_cooler 

    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_adapters = anvil.server.call('get_sheet_data_adapters')
    categories_adapters = anvil.server.call('get_unique_categories',sheet_data_adapters)
    self.adapters_dropdown.items = categories_adapters 

    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_psu = anvil.server.call('get_sheet_data_psu')
    categories_psu = anvil.server.call('get_unique_categories',sheet_data_psu)
    self.power_supply_dropdown.items = categories_psu 
    
    #this function calls from the server module and gets the sheet data for the cpus, and gets the unique categories for motherboards, then popluates the dropdown with the called items
    sheet_data_os = anvil.server.call('get_sheet_data_os')
    categories_os = anvil.server.call('get_unique_categories',sheet_data_os)
    self.os_dropdown.items = categories_os    
    
   # Any code you write here will run before the form opens.
  

 

  def storage_stock_display_pressed_enter(self, **event_args):
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

  def motherboard_dropdown_change(self, **event_args):
    selected_category = self.motherboard_dropdown.selected_value
    items = anvil.server.call('get_items', selected_category)
    self.items_dropdown.items = items

  def case_dropdown_change(self, **event_args):
    selected_category = self.case_dropdown.selected_value
    items = anvil.server.call('get_items', selected_category)
    self.items_dropdown.items = items


  #this is adding in the price of said items:
  def cpu_dropdown_change_price_text(self, **event_args):
    selected_item = self.cpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 1)  # 1 is the worksheet index for CPUs
      self.cpu_display.text = f"${price:.2f}"
      self.component_prices['cpu'] = price
      self.update_total_price()

  def gpu_dropdown_change_price_text(self, **event_args):
    selected_item = self.gpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 2)  # 2 is the worksheet index for GPUs
      self.gpu_display.text = f"${price:.2f}"
      self.component_prices['gpu'] = price
      self.update_total_price()

  def motherbrd_dropdown_change_price_text(self, **event_args):
    selected_item = self.gpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 3)
      self.gpu_display.text = f"${price:.2f}"
      self.component_prices['motherboard'] = price
      self.update_total_price()

  def case_dropdown_change_price_text(self, **event_args):
    selected_item = self.gpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 4)
      self.gpu_display.text = f"${price:.2f}"
      self.component_prices['case'] = price
      self.update_total_price()

  def ram_dropdown_change_price_text(self, **event_args):
    selected_item = self.gpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 5)
      self.gpu_display.text = f"${price:.2f}"
      self.component_prices['ram'] = price
      self.update_total_price()

  def storage_dropdown_change_price_text(self, **event_args):
    selected_item = self.gpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 6)
      self.gpu_display.text = f"${price:.2f}"
      self.component_prices['storage'] = price
      self.update_total_price()

  def fans_dropdown_change_price_text(self, **event_args):
    selected_item = self.gpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 7)
      self.gpu_display.text = f"${price:.2f}"
      self.component_prices['fans'] = price
      self.update_total_price()

  def cpu_cooler_dropdown_change_price_text(self, **event_args):
    selected_item = self.gpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 8)
      self.gpu_display.text = f"${price:.2f}"
      self.component_prices['cpu_cooler'] = price
      self.update_total_price()

  def adapters_dropdown_change_price_text(self, **event_args):
    selected_item = self.gpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 9)
      self.gpu_display.text = f"${price:.2f}"
      self.component_prices['adapters'] = price
      self.update_total_price()

  def psu_dropdown_change_price_text(self, **event_args):
    selected_item = self.gpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 10)
      self.gpu_display.text = f"${price:.2f}"
      self.component_prices['psu'] = price
      self.update_total_price()

  def os_dropdown_change_price_text(self, **event_args):
    selected_item = self.gpu_dropdown.selected_value
    if selected_item:
      price = anvil.server.call('get_item_price', selected_item, 11)
      self.gpu_display.text = f"${price:.2f}"
      self.component_prices['os'] = price
      self.update_total_price()


  #total price
  def update_total_price(self):
    total_price = sum(self.component_prices.values())
    self.total_price_display.text = f"${total_price:.2f}"