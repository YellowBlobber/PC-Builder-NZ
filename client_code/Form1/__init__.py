from ..name_build_form import name_build_formTemplate
from ..BuildsForm import BuildsFormTemplate
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
import anvil.users
from datetime import datetime



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

    self.component_wattage = {
    'cpu': 0.0,
    'gpu': 0.0,
    'motherboard': 0.0,
    'storage': 0.0,
    'storage_2': 0.0,
    'storage_3': 0.0,
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

  def style_my_acocunt_button(self, **event_args):
    self.my_account_buttonbutton.background = ''
    self.my_account_button.border = ''
    self.my_account_button.set_event_handler('show', self.style_my_account_button)
  
  #below is for price_display

  def update_total_price(self):
      total_price = sum(self.component_prices.values())
      self.total_price_display.text = f"${total_price:.2f}"

  def update_total_wattage(self):
      total_wattage = sum(self.component_wattage.values())
      self.wattage_display.text = f"{total_wattage}W"
  
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

            # location image making visable
            self.cpu_location.visible = True
    # wattage:
    for row in sheet_data_cpu:
      print(f"Checking row: {row['Item Name']}")
      if row['Item Name'].strip() == selected_cpu.strip():
          cpu_wattage_str = row['Value option']
          cpu_wattage = int(cpu_wattage_str)
          print(f"Wattage found: {cpu_wattage}")
          self.component_wattage['cpu'] = cpu_wattage
          self.update_total_wattage()
    # image change
    for row in sheet_data_cpu:
      if row['Item Name'] == selected_cpu:
          image_url = row['Image Links']
          print(f"Image URL: {image_url}")
            
            # Set the image source to the fetched URL
          self.cpu_image.source = image_url
          self.cpu_image.visible = True


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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.cooling_stock_display.text = stock_status
           # location image making visable
            self.cooling_location.visible = True

    # wattage:
    for row in sheet_data_cpu_cooler:
      print(f"Checking row: {row['Item Name']}")
      if row['Item Name'].strip() == selected_cpu_cooler.strip():
          cpu_cooler_wattage_str = row['Value option']
          cpu_cooler_wattage = int(cpu_cooler_wattage_str)
          print(f"wattage found: {cpu_cooler_wattage}")
          self.component_wattage['cpu_cooler'] = cpu_cooler_wattage
          self.update_total_wattage()

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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.motherboard_stock_display.text = stock_status
           # location image making visable
            self.motherboard_location.visible = True

    # wattage:
    for row in sheet_data_motherbrd:
      print(f"Checking row: {row['Item Name']}")
      if row['Item Name'].strip() == selected_motherbrd.strip():
          self.component_wattage['motherboard'] = 50
          self.update_total_wattage()

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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.ram_stock_display.text = stock_status
           # location image making visable
            self.ram_location.visible = True

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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.gpu_stock_display.text = stock_status
           # location image making visable
            self.gpu_location.visible = True

    for row in sheet_data_gpu:
      print(f"Checking row: {row['Item Name']}")
      if row['Item Name'].strip() == selected_gpu.strip():
          gpu_wattage_str = row['Value option']
          gpu_wattage = int(gpu_wattage_str)
          print(f"wattage found: {gpu_wattage}")
          self.component_wattage['gpu'] = gpu_wattage
          self.update_total_wattage()

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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.case_stock_display.text = stock_status
           # location image making visable
            self.case_location.visible = True

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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.storage_stock_display.text = stock_status
           # location image making visable
            self.storage_location.visible = True

    # wattage:
    for row in sheet_data_storage:
      print(f"Checking row: {row['Item Name']}")
      if row['Item Name'].strip() == selected_storage.strip():
          self.component_wattage['storage'] = 10
          self.update_total_wattage()

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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.os_stock_display.text = stock_status
           # location image making visable
            self.os_location.visible = True
  
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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.fans_stock_display.text = stock_status
           # location image making visable
            self.fans_location.visible = True


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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.storage_stock_display_2.text = stock_status
           # location image making visable
            self.storage_2_location.visible = True

    # wattage:
    for row in sheet_data_storage:
      print(f"Checking row: {row['Item Name']}")
      if row['Item Name'].strip() == selected_storage_2.strip():
          self.component_wattage['storage_2'] = 10
          self.update_total_wattage()

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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.storage_stock_display_3.text = stock_status
           # location image making visable
            self.storage_3_location.visible = True

    # wattage:
    for row in sheet_data_storage:
      print(f"Checking row: {row['Item Name']}")
      if row['Item Name'].strip() == selected_storage_3.strip():
          self.component_wattage['storage_3'] = 10
          self.update_total_wattage()

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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.adapters_stock_display.text = stock_status
           # location image making visable
            self.adapters_location.visible = True

  
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

            stock_status = row['Stock']  # Get stock status
            # Display stock status
            self.psu_stock_display.text = stock_status
           # location image making visable
            self.psu_location.visible = True

  def save_button_click(self, **event_args):
    # Create an instance of the name_build_form
    name_form = name_build_formTemplate()
    self.save_button.icon = ""
    self.save_button.text = "SAVING..."
    # Show the form as an alert to ask for build name input
    result = alert(content=name_form, title="Name Your Build", buttons=[("Save", True), ("Cancel", False)])
    
    if result:
        # Get the build name from the form's text box (assuming a TextBox exists on the form)
        build_name = name_form.build_name_textbox.text
        
        # Check if a name was entered
        if build_name:
            selected_items = {
                "cpu": self.cpu_dropdown.selected_value,
                "gpu": self.gpu_dropdown.selected_value,
                "motherboard": self.motherboard_dropdown.selected_value,
                "ram": self.ram_dropdown.selected_value,
                "cpu_cooler": self.cpu_cooler_dropdown.selected_value,
                "case": self.case_dropdown.selected_value,
                "psu": self.power_supply_dropdown.selected_value,
                "storage": self.storage_dropdown.selected_value,
                "os": self.os_dropdown.selected_value,
                "storage_2": self.storage_2_dropdown.selected_value,
                "storage_3": self.storage_3_dropdown.selected_value,
                "adapters": self.adapters_dropdown.selected_value,

                "total_price": self.total_price_display.text,
                "wattage": self.wattage_display.text,
            }
           # Call the server function to save the build
            anvil.server.call('save_build', build_name, selected_items)
            self.save_button.text = "SAVE "
            self.save_button.icon = "fa:save"
        else:
            alert("Please enter a name for your build.")
            self.save_button.text = "SAVE "

  def login_button_click(self, **event_args):
    # Show Anvil's built-in login form
    user = anvil.users.login_with_form()
    
    if user:
        alert(f"Welcome, {user['email']}!")
        self.profile_icon.visible = True
        self.login_button.visible = False
        self.my_account_button.visible = True
        self.my_account_button.text = (f"{user['email']}")
    else:
        alert("Login failed or was canceled.")

  def buy_button_click(self, **event_args):
    product_url = "https://www.computerlounge.co.nz/components#!categoryId=247&page=1&q=&scid=-1&isListMode=false&Filters%5B0%5D.Key=Sort&Filters%5B0%5D.Value=1"
    # Open the external website in a new tab
    anvil.js.window.open(product_url, "_blank")
    pass

  def catalogue_button_click(self, **event_args):
    if self.catalogue_panel.visible:  # If the label is currently visible
      self.catalogue_panel.visible = False  # Hide the label
      self.catalogue_button.icon = "fa:angle-right"
    else:
      self.catalogue_panel.visible = True  # Show the label
      self.catalogue_button.icon = "fa:angle-down"
      
  def nav_button_click(self, **event_args):
 # Toggles the visibility of the label on each button click
    if self.menu_panel.visible:  # If the label is currently visible
      self.menu_panel.visible = False  # Hide the label
    else:
      self.menu_panel.visible = True  # Show the label

# Function to display builds as buttons in an alert

  def view_builds_button_click(self, **event_args):
        user = anvil.users.get_user()

        if user:
            # Fetch saved builds from the server
            saved_builds = anvil.server.call('get_user_builds', user)

            if saved_builds:
                # Create a ColumnPanel to hold the buttons
                column_panel = ColumnPanel()

                # Loop through each saved build and create a button
                for build in saved_builds:
                    # Create a button for each build
                    btn = Button(text=build['build_name'], role="raised")
                    
                    # Store the build data in the button’s tag
                    btn.tag.build_data = build

                    # Set the click event handler for each button
                    btn.set_event_handler('click', lambda sender=btn, **event_args: self.load_build_click(sender))

                    # Add the button to the ColumnPanel
                    column_panel.add_component(btn)

                # Show the buttons inside an alert
                alert(content=column_panel, large=True, title="Select Your Build")

            else:
                alert("No builds found for this user.", title="No Builds")
        else:
            alert("Please log in to view your builds.", title="Login Required")


  def load_build_click(self, sender, **event_args):
    """ Handle the click event of the build button """
    # Retrieve the build data from the button tag
    build = sender.tag.build_data

    selected_items = build['selected_items']
  
    self.cpu_dropdown.selected_value = selected_items.get('cpu')
    self.gpu_dropdown.selected_value = selected_items.get('gpu')
    self.ram_dropdown.selected_value = selected_items.get('ram')
    self.motherboard_dropdown.selected_value = selected_items.get('motherboard')
    self.storage_dropdown.selected_value = selected_items.get('storage')
    self.power_supply_dropdown.selected_value = selected_items.get('psu')
    self.cpu_cooler_dropdown.selected_value = selected_items.get('cpu_cooler')
    self.case_dropdown.selected_value = selected_items.get('case')
    self.storage_2_dropdown.selected_value = selected_items.get('storage_2')
    self.storage_3_dropdown.selected_value = selected_items.get('storage_3')
    self.os_dropdown.selected_value = selected_items.get('os')
    self.adapters_dropdown.selected_value = selected_items.get('adapters')
    self.fans_dropdown.selected_value = selected_items.get('fans')
  
    alert.dismiss()