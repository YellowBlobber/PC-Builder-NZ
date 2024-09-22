
    ### This is the last guides page. ###

from ..Guides_Home import Guides_Home
from ._anvil_designer import Guides_Page3Template
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


class Guides_Page3(Guides_Page3Template): # same as the other pages/forms with just buttons
  def __init__(self, **properties):
    self.init_components(**properties)
    user = anvil.users.get_user()
    if user:
        self.login_button.visible = False
        self.my_account_button.visible = True
        self.my_account_button.text = (f"{user['email']}")

  def return_button_click(self, **event_args):
    form = Guides_Home()
    open_form(form)

  def sign_out_button_click(self, **event_args):
    anvil.users.logout()
    alert("You have been signed out.")
    self.my_account_button.visible = False
    self.login_button.visible = True

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