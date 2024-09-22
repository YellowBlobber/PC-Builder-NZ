
    ### This is the second guides page. ###

from ._anvil_designer import Guides_Page2Template
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


class Guides_Page2(Guides_Page2Template): 
  def __init__(self, **properties):
    self.init_components(**properties)
    user = anvil.users.get_user()
    if user:
        self.login_button.visible = False
        self.my_account_button.visible = True
        self.my_account_button.text = (f"{user['email']}")


  def budget_build_button_click(self, **event_args): # this just gets the links from the sharing system for the custom builds. The rest is the same as the other guide pages
    build_url = "https://rare-downright-mission.anvil.app/#?build_id=246986e4-193c-463a-b9be-fce46a039b30"
    # Open the external website in a new tab
    anvil.js.window.open(build_url, "_blank")

  def mid_build_button_click(self, **event_args):
    build_url = "https://rare-downright-mission.anvil.app/#?build_id=2a637e99-c898-439a-8f0d-06a294fbb13b"
    # Open the external website in a new tab
    anvil.js.window.open(build_url, "_blank")

  def high_build_button_click(self, **event_args):
    build_url = "https://rare-downright-mission.anvil.app/#?build_id=840146ac-a1a5-4bff-b228-a08806c1df1e"
    # Open the external website in a new tab
    anvil.js.window.open(build_url, "_blank")

  def return_button_click(self, **event_args):
    form = Guides_Home()
    open_form(form)

  def builder_button_click(self, **event_args):
    open_form('Form1')

  def login_button_click(self, **event_args):
    # Show Anvil's built-in login form
    user = anvil.users.login_with_form()
    
    if user:
        alert(f"Welcome, {user['email']}!")
        self.login_button.visible = False
        self.my_account_button.visible = True
        self.my_account_button.text = (f"{user['email']}")
    else:
        alert("Login failed or was canceled.")

  def catalogue_button_click(self, **event_args):
    if self.catalogue_panel.visible:  # If the label is currently visible
      self.catalogue_panel.visible = False  # Hide the label
      self.catalogue_button.icon = "fa:angle-right"
    else:
      self.catalogue_panel.visible = True  # Show the label
      self.catalogue_button.icon = "fa:angle-down"
      
  def nav_button_click(self, **event_args):
 # Toggles the visibility of the label on each button click
    if self.menu_panel.visible:  # If the label is currently visible
      self.menu_panel.visible = False  # Hide the label
    else:
      self.menu_panel.visible = True  # Show the label

  def guides_button_click(self, **event_args):
    form = Guides_Home()
    open_form(form)

  def guides_button_footer_click(self, **event_args):
    form = Guides_Home()
    open_form(form)

  def builder_button_footer_click(self, **event_args):
    open_form('Form1')

  def login_button_footer_click(self, **event_args):
    # Show Anvil's built-in login form
    user = anvil.users.login_with_form()
    
    if user:
        alert(f"Welcome, {user['email']}!")
        self.login_button.visible = False
        self.my_account_button.visible = True
        self.my_account_button.text = (f"{user['email']}")
    else:
        alert("Login failed or was canceled.")

  def logout_button_footer_click(self, **event_args):
    anvil.users.logout()
    alert("You have been signed out.")
    self.my_account_button.visible = False
    self.login_button.visible = True

  def sign_out_button_click(self, **event_args):
    anvil.users.logout()
    alert("You have been signed out.")
    self.my_account_button.visible = False
    self.login_button.visible = True
