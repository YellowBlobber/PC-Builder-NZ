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
    self.image.source = self.item['Image Links']
    self.item_name_label.text = self.item['Item Name']
    self.price_label.text = f"${self.item['Price']}"
    self.stock_label.text = f"Stock: {self.item['Stock']}"

