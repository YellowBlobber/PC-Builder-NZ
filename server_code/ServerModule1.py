import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
import anvil.server
import anvil.google.drive

'''@anvil.server.callable
def get_categories(self):
    sheet = app_files.pc_builder_nz
    self.worksheet = sheet[0]
    categories = self.worksheet.fields
    return categories


@anvil.server.callable
def get_items(category):
    sheet = anvil.google.drive.get("PC Builder NZ").worksheet("Computer Lounge")
    data = sheet.get_all_records()
    items = [row['Item Name'] for row in data if row['Category Name'] == category]
    return items'''

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