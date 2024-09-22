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

  def learn_parts_button_click(self, **event_args):
   open_form('Guides_Page1')

  def learn_recomendations_button_click(self, **event_args):
    open_form('Guides_Page2')

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

  def builder_button_click(self, **event_args):
   open_form('Form1')

  def cpu_button_click(self, **event_args):
    open_form('CatalogueForm')

  def sign_out_button_click(self, **event_args):
    anvil.users.logout()
    alert("You have been signed out.")

  def learn_building_button_click(self, **event_args):
    open_form('Guides_Page3')

  def guides_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

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