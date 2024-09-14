import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
import anvil.server
import anvil.google.drive
import anvil.users
from anvil.tables import app_tables
from cryptography.fernet import Fernet
import anvil.secrets
import uuid

@anvil.server.callable
#defining a function that calls the information in the index worksheet 1, in google sheets. [1] being the cpu worksheet.
#the index [0] worksheet contains all items therefor we do not use index page 0 unless we are wanting all items.
def get_sheet_data_cpus():
  sheet_cpu = app_files.pc_builder_nz
  worksheet_cpu = sheet_cpu.worksheets[1]
  return worksheet_cpu.rows

@anvil.server.callable
#defining a function that calls the information in the index worksheet 2, in google sheets. [2] being the gpu worksheet.
def get_sheet_data_gpu():
  sheet_gpu = app_files.pc_builder_nz
  worksheet_gpu = sheet_gpu.worksheets[2]
  return worksheet_gpu.rows

@anvil.server.callable
#motherbrd stands for Motherboards,
#defining a fuction that calls the infomation in the index worksheet 3, in google sheets. [3] being the motherboard worksheet.
def get_sheet_data_motherbrd():
  sheet_motherbrd = app_files.pc_builder_nz
  worksheet_motherbrd = sheet_motherbrd.worksheets[3]
  return worksheet_motherbrd.rows
  
@anvil.server.callable
#defining a fuction that calls the infomation in the index worksheet 4, in google sheets. [4] being the case worksheet.
def get_sheet_data_case():
  sheet_case = app_files.pc_builder_nz
  worksheet_case = sheet_case.worksheets[4]
  return worksheet_case.rows

@anvil.server.callable
#defining a fuction that calls the infomation in the index worksheet 4, in google sheets. [4] being the case worksheet.
def get_sheet_data_ram():
  sheet_ram = app_files.pc_builder_nz
  worksheet_ram = sheet_ram.worksheets[5]
  return worksheet_ram.rows

@anvil.server.callable
#defining a fuction that calls the infomation in the index worksheet 4, in google sheets. [4] being the case worksheet.
def get_sheet_data_storage():
  sheet_storage = app_files.pc_builder_nz
  worksheet_storage = sheet_storage.worksheets[6]
  return worksheet_storage.rows

@anvil.server.callable
#defining a fuction that calls the infomation in the index worksheet 4, in google sheets. [4] being the case worksheet.
def get_sheet_data_fans():
  sheet_fans = app_files.pc_builder_nz
  worksheet_fans = sheet_fans.worksheets[7]
  return worksheet_fans.rows

@anvil.server.callable
#defining a fuction that calls the infomation in the index worksheet 4, in google sheets. [4] being the case worksheet.
def get_sheet_data_cpu_cooler():
  sheet_cpu_cooler = app_files.pc_builder_nz
  worksheet_cpu_cooler = sheet_cpu_cooler.worksheets[8]
  return worksheet_cpu_cooler.rows

@anvil.server.callable
#defining a fuction that calls the infomation in the index worksheet 4, in google sheets. [4] being the case worksheet.
def get_sheet_data_adapters():
  sheet_adapters = app_files.pc_builder_nz
  worksheet_adapters = sheet_adapters.worksheets[9]
  return worksheet_adapters.rows

@anvil.server.callable
#defining a fuction that calls the infomation in the index worksheet 4, in google sheets. [4] being the case worksheet.
def get_sheet_data_psu():
  sheet_psu = app_files.pc_builder_nz
  worksheet_psu = sheet_psu.worksheets[10]
  return worksheet_psu.rows

@anvil.server.callable
#defining a fuction that calls the infomation in the index worksheet 4, in google sheets. [4] being the case worksheet.
def get_sheet_data_os():
  sheet_os = app_files.pc_builder_nz
  worksheet_os = sheet_os.worksheets[11]
  return worksheet_os.rows

@anvil.server.callable
#this fuction calls the item names in the picked index for worksheet eg 3, allows us to call and use the names of items in the form code
def get_unique_categories(sheet_data):
  categories_item_name = set(row['Item Name'] for row in sheet_data)
  return sorted(list(categories_item_name))

@anvil.server.callable
#this fuction calls the item names in the picked index for worksheet eg 3, allows us to call and use the names of items in the form code
def get_unique_price(sheet_data):
  categories_price = set(row['Price'] for row in sheet_data)
  return sorted(list(categories_price))

@anvil.server.callable
#this fuction calls the item names in the picked index for worksheet eg 3, allows us to call and use the names of items in the form code
def get_unique_stock(sheet_data):
  categories_stock = set(row['Stock'] for row in sheet_data)
  return sorted(list(categories_stock))

@anvil.server.callable
def save_build(build_name, selected_items):
    if isinstance(build_name, str):
        # Get the logged-in user
        user = anvil.users.get_user()

        if user:
            # Generate a unique build ID for sharing
            build_id = str(uuid.uuid4())  # Generates a unique ID for each build

            # Save the build with reference to the user
            app_tables.builds.add_row(
                build_name=build_name, 
                selected_items=selected_items,
                user=user,
                build_id=build_id  # Save the unique build ID
            )

            # Return the shareable link (assuming you're using anvil's app URL)
            shareable_link = f"https://your-anvil-app-url.com/?build_id={build_id}"
            print(f"Build saved successfully! Shareable link: {shareable_link}")
            return shareable_link

        else:
            raise ValueError("No user is logged in.")
            anvil.users.login_with_form()
    else:
        raise ValueError("build_name must be a string.")

@anvil.server.callable
def get_user_builds(user_row):
    return app_tables.builds.search(user=user_row)

@anvil.server.callable
def get_build_by_id(build_id):
    """ Retrieve build by ID """
    build_row = app_tables.builds.get_by_id(build_id)
    if build_row:
        return build_row['build_data']
    return None

@anvil.server.callable
def save_build_and_generate_link(build_name, selected_items):
    user = anvil.users.get_user()
    if user:
        # Check if a build with this name already exists
        existing_build = app_tables.builds.get(user=user, build_name=build_name)
        
        if not existing_build:
            # Add new row
            row = app_tables.builds.add_row(
                build_name=build_name,
                selected_items=selected_items,
                user=user
            )
        else:
            # Build already exists, update it instead of adding a new row
            row = existing_build
            row['selected_items'] = selected_items

        # Generate a unique link
        build_id = row.get_id()  # Get the row's unique ID
        app_link = f"{anvil.server.get_app_origin()}/#?build_id={build_id}"
        return app_link
    else:
        raise ValueError("No user is logged in.")

