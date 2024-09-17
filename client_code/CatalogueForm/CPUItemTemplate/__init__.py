from ._anvil_designer import CPUItemTemplateTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CPUItemTemplate(CPUItemTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def set_item(self, item):
        # Bind data to the template's components
        self.cpu_image.source = item['Image']
        self.cpu_name.text = item['Item Name']  
        self.cpu_price.text = f"${item['Price']}"
        self.cpu_stock.text = f"In Stock: {item['Stock']}"

