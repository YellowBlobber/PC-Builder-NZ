from ._anvil_designer import CatalogueFormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CatalogueForm(CatalogueFormTemplate):
  def __init__(self, selected_category=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

   # Check which category is passed and display the relevant items
    self.show_cpus()  # Call the function to display only CPUs

    # Any code you write here will run before the form opens.

  def show_cpus(self, **event_args):
    """Load and display CPUs in the repeating panel"""
    cpu_data = anvil.server.call('get_sheet_data_cpus')
     # Clear any existing rows
    if cpu_data:
        self.cpus_repeating_panel.items = cpu_data
    else:
        alert("No CPU data found.")
