from ..Guides_Home import Guides_Home
from ._anvil_designer import Guides_Page1FormTemplate
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
from anvil import alert


class Guides_Page1Form(Guides_Page1FormTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def return_button_click(self, **event_args):
    form = Guides_Home()
    open_form(form)

