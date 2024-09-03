import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
import anvil.server
import anvil.google.drive

@anvil.server.callable
def get_sheet_data_cpus():
  sheet_cpu = app_files.pc_builder_nz
  worksheet_cpu = sheet_cpu.worksheets[1]
  return worksheet_cpu.rows

@anvil.server.callable
def get_sheet_data_gpu():
  sheet_gpu = app_files.pc_builder_nz
  worksheet_gpu = sheet_gpu.worksheets[2]
  return worksheet_gpu.rows

@anvil.server.callable
def get_unique_categories(sheet_data):
  categories = set(row['Item Name'] for row in sheet_data)
  return sorted(list(categories))


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