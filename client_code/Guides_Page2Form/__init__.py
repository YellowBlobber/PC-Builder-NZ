from ._anvil_designer import Guides_Page2FormTemplate
from ..Guides_Home import Guides_Home
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


class Guides_Page2Form(Guides_Page2FormTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)


  def budget_build_button_click(self, **event_args):
    build_url = "https://7gmqage3den4gxx7.anvil.app/debug/SE6YHK4YGYOJFH54KK5F2AOTSHAKSBZQ%3DDFKTOQJTRQ4TOEYBFZU6NXIY/#?build_id=246986e4-193c-463a-b9be-fce46a039b30"
    # Open the external website in a new tab
    anvil.js.window.open(build_url, "_blank")
    pass

  def mid_build_button_click(self, **event_args):
    build_url = "https://7gmqage3den4gxx7.anvil.app/debug/SE6YHK4YGYOJFH54KK5F2AOTSHAKSBZQ%3DDFKTOQJTRQ4TOEYBFZU6NXIY/#?build_id=2a637e99-c898-439a-8f0d-06a294fbb13b"
    # Open the external website in a new tab
    anvil.js.window.open(build_url, "_blank")
    pass

  def high_build_button_click(self, **event_args):
    build_url = "https://7gmqage3den4gxx7.anvil.app/debug/SE6YHK4YGYOJFH54KK5F2AOTSHAKSBZQ%3DDFKTOQJTRQ4TOEYBFZU6NXIY/#?build_id=840146ac-a1a5-4bff-b228-a08806c1df1e"
    # Open the external website in a new tab
    anvil.js.window.open(build_url, "_blank")
    pass

  def return_button_click(self, **event_args):
    form = Guides_Home()
    open_form(form)
