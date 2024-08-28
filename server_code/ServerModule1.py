import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.drive

@anvil.server.callable
def get_categories():
    sheet = anvil.google.drive.get("PC Builder NZ").worksheet("Computer Lounge")
    data = sheet.get_all_records()
    categories = list(set(row['Category Name'] for row in data))
    return categories


@anvil.server.callable
def get_items(category):
    sheet = anvil.google.drive.get("pc_builder_nz__google_data").worksheet("Computer Lounge")
    data = sheet.get_all_records()
    items = [row['Item Name'] for row in data if row['Category name'] == category]
    return items

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#