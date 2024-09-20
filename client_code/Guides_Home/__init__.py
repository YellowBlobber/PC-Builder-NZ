from ._anvil_designer import Guides_HomeTemplate
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



class Guides_Home(Guides_HomeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def learnmore_right_button_click(self, **event_args):
   open_form('Guides_Page1Form')

  def learnmore_parts_button_click(self, **event_args):
    open_form('Guides_Page2Form')