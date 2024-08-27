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
def get_items(category):
    sheet = anvil.google.drive.get("pc_builder_nz__google_data").worksheet("Computer_Lounge")
    data = sheet.get_all_records()
    items = [row['Item'] for row in data if row['Category'] == category]
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