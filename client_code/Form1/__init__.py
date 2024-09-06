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

    self.component_prices = {
    'cpu': 0.0,
    'gpu': 0.0,
    'motherboard': 0.0,
    'case': 0.0,
    'ram': 0.0,
    'psu': 0.0,
    'storage': 0.0,
    'storage_2': 0.0,
    'storage_3': 0.0,
    'os': 0.0,
    'fans': 0.0,
    'adapter': 0.0,
    'cpu_cooler': 0.0
    }
    
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
  
  #below is for price_display

  def update_total_price(self):
      total_price = sum(self.component_prices.values())
      self.total_price_display.text = f"${total_price:.2f}"
  
  def cpu_dropdown_change(self, **event_args):
    print("CPU dropdown changed")
    selected_cpu = self.cpu_dropdown.selected_value    
    sheet_data_cpu = anvil.server.call('get_sheet_data_cpus')
    
    for row in sheet_data_cpu:
        print(f"Checking row: {row['Item Name']}")
        if row['Item Name'].strip() == selected_cpu.strip():
            cpu_price_str = row['Price']
            cpu_price = float(cpu_price_str)  # Convert the price to float
            print(f"Price found: {cpu_price}")
            self.cpu_display.text = f"${cpu_price:.2f}"  # Display formatted price
            self.component_prices['cpu'] = cpu_price
            self.update_total_price()

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.cpu_stock_display.text = stock_status  

  def cpu_cooler_dropdown_change(self, **event_args):
    print("CPU Cooler dropdown changed")
    selected_cpu_cooler = self.cpu_cooler_dropdown.selected_value
    sheet_data_cpu_cooler = anvil.server.call('get_sheet_data_cpu_cooler')

    for row in sheet_data_cpu_cooler:
        if row['Item Name'].strip() == selected_cpu_cooler.strip():
            cpu_cooler_price_str = row['Price']
            cpu_cooler_price = float(cpu_cooler_price_str)
                # Update the price display for CPU cooler
            self.cooling_display.text = f"${cpu_cooler_price:.2f}"
            self.component_prices['cpu_cooler'] = cpu_cooler_price
            self.update_total_price()

  def motherboard_dropdown_change(self, **event_args):
    print("Motherboard dropdown changed")
    selected_motherbrd = self.motherboard_dropdown.selected_value
    sheet_data_motherbrd = anvil.server.call('get_sheet_data_motherbrd')

    for row in sheet_data_motherbrd:
        if row['Item Name'].strip() == selected_motherbrd.strip():
            motherbrd_price_str = row['Price']
            motherbrd_price = float(motherbrd_price_str)
                # Update the price display for CPU cooler
            print(f"Price found: {motherbrd_price}")
            self.motherboard_display.text = f"${motherbrd_price:.2f}"
            self.component_prices['motherboard'] =motherbrd_price
            self.update_total_price()

  def ram_dropdown_change(self, **event_args):
    selected_ram = self.ram_dropdown.selected_value
    print(f"Selected RAM: {selected_ram}")
    
    sheet_data_ram = anvil.server.call('get_sheet_data_ram')
    print(f"Sheet data: {sheet_data_ram}")

    for row in sheet_data_ram:
        if row['Item Name'].strip() == selected_ram.strip():
            ram_price_str = row['Price']
            ram_price = float(ram_price_str)
            print(f"Price found: {ram_price}")
            self.ram_display.text = f"${ram_price:.2f}"
            self.component_prices['ram'] = ram_price
            self.update_total_price()

  def gpu_dropdown_change(self, **event_args):
    selected_gpu = self.gpu_dropdown.selected_value
    print(f"Selected GPU: {selected_gpu}")
    
    sheet_data_gpu = anvil.server.call('get_sheet_data_gpu')
    print(f"Sheet data: {sheet_data_gpu}")

    for row in sheet_data_gpu:
        if row['Item Name'].strip() == selected_gpu.strip():
            gpu_price_str = row['Price']
            gpu_price = float(gpu_price_str)
            print(f"Price found: {gpu_price}")
            self.gpu_display.text = f"${gpu_price:.2f}"
            self.component_prices['gpu'] = gpu_price
            self.update_total_price()

  def case_dropdown_change(self, **event_args):
    selected_case = self.case_dropdown.selected_value
    print(f"Selected Case: {selected_case}")
    
    sheet_data_case = anvil.server.call('get_sheet_data_case')
    print(f"Sheet data: {sheet_data_case}")

    for row in sheet_data_case:
        if row['Item Name'].strip() == selected_case.strip():
            case_price_str = row['Price']
            case_price = float(case_price_str)
            print(f"Price found: {case_price}")
            self.case_display.text = f"${case_price:.2f}"
            self.component_prices['case'] = case_price
            self.update_total_price()

  def storage_dropdown_change(self, **event_args):
    selected_storage = self.storage_dropdown.selected_value
    print(f"Selected Storage: {selected_storage}")
    
    sheet_data_storage = anvil.server.call('get_sheet_data_storage')
    print(f"Sheet data: {sheet_data_storage}")

    for row in sheet_data_storage:
        if row['Item Name'].strip() == selected_storage.strip():
            storage_price_str = row['Price']
            storage_price = float(storage_price_str)
            print(f"Price found: {storage_price}")
            self.storage_display.text = f"${storage_price:.2f}"
            self.component_prices['storage'] = storage_price
            self.update_total_price()

  def os_dropdown_change(self, **event_args):
    selected_os = self.os_dropdown.selected_value
    print(f"Selected OS: {selected_os}")
    
    sheet_data_os = anvil.server.call('get_sheet_data_os')
    print(f"Sheet data: {sheet_data_os}")

    for row in sheet_data_os:
        if row['Item Name'].strip() == selected_os.strip():
            os_price_str = row['Price']
            os_price = float(os_price_str)
            print(f"Price found: {os_price}")
            self.os_display.text = f"${os_price:.2f}"
            self.component_prices['os'] = os_price
            self.update_total_price()

  def fans_dropdown_change(self, **event_args):
    selected_fans = self.fans_dropdown.selected_value
    print(f"Selected Fans: {selected_fans}")
    
    sheet_data_fans = anvil.server.call('get_sheet_data_fans')
    print(f"Sheet data: {sheet_data_fans}")

    for row in sheet_data_fans:
        if row['Item Name'].strip() == selected_fans.strip():
            fans_price_str = row['Price']
            fans_price = float(fans_price_str)
            print(f"Price found: {fans_price}")
            self.fans_display.text = f"${fans_price:.2f}"
            self.component_prices['fans'] = fans_price
            self.update_total_price()


  def storage_2_dropdown_change(self, **event_args):
    selected_storage_2 = self.storage_2_dropdown.selected_value
    print(f"Selected Storage 2: {selected_storage_2}")
    
    sheet_data_storage = anvil.server.call('get_sheet_data_storage')
    print(f"Sheet data: {sheet_data_storage}")

    for row in sheet_data_storage:
        if row['Item Name'].strip() == selected_storage_2.strip():
            storage_2_price_str = row['Price']
            storage_2_price = float(storage_2_price_str)
            print(f"Price found: {storage_2_price}")
            self.storage_2_display.text = f"${storage_2_price:.2f}"
            self.component_prices['storage_2'] = storage_2_price
            self.update_total_price()

  def storage_3_dropdown_change(self, **event_args):
    selected_storage_3 = self.storage_3_dropdown.selected_value
    print(f"Selected Storage 3: {selected_storage_3}")
    
    sheet_data_storage = anvil.server.call('get_sheet_data_storage')
    print(f"Sheet data: {sheet_data_storage}")

    for row in sheet_data_storage:
        if row['Item Name'].strip() == selected_storage_3.strip():
            storage_3_price_str = row['Price']
            storage_3_price = float(storage_3_price_str)
            print(f"Price found: {storage_3_price}")
            self.storage_3_display.text = f"${storage_3_price:.2f}"
            self.component_prices['storage_3'] = storage_3_price
            self.update_total_price()

  

  def adapters_dropdown_change(self, **event_args):
    selected_adapter = self.adapters_dropdown.selected_value
    print(f"Selected Adapter: {selected_adapter}")
    
    sheet_data_adapters = anvil.server.call('get_sheet_data_adapters')
    print(f"Sheet data: {sheet_data_adapters}")

    for row in sheet_data_adapters:
        if row['Item Name'].strip() == selected_adapter.strip():
            adapter_price_str = row['Price']
            adapter_price = float(adapter_price_str)
            print(f"Price found: {adapter_price}")
            self.adapter_display.text = f"${adapter_price:.2f}"
            self.component_prices['adapter'] = adapter_price
            self.update_total_price()

  
  def power_supply_dropdown_change(self, **event_args):
    selected_psu = self.power_supply_dropdown.selected_value
    print(f"Selected PSU: {selected_psu}")
    
    sheet_data_psu = anvil.server.call('get_sheet_data_psu')
    print(f"Sheet data: {sheet_data_psu}")

    for row in sheet_data_psu:
        if row['Item Name'].strip() == selected_psu.strip():
            psu_price_str = row['Price']
            psu_price = float(psu_price_str)
            print(f"Price found: {psu_price}")
            self.psu_display.text = f"${psu_price:.2f}"
            self.component_prices['psu'] = psu_price
            self.update_total_price()

#stock status display
