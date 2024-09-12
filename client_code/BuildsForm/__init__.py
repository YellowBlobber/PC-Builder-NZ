from ._anvil_designer import BuildsFormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BuildsForm(BuildsFormTemplate):
  def __init__(self, builds, **properties):
    self.init_components(**properties)
        
        # Debugging: Check if builds are received
    print("Received builds:", builds)
        
    if builds:
      for build in builds:
        # Create a button for each build
        btn = Button(text=build['build_name'], role='build-button')
        btn.tag.build_data = build  # Store the build data in the button’s tag
        btn.set_event_handler('click', self.build_selected)
                
        # Add the button to the column panel
        self.column_panel.add_component(btn)

        # Add "Go Back" button
      go_back_button = Button(text="Go Back", role="back-button")
      go_back_button.set_event_handler('click', self.go_back)
      self.column_panel.add_component(go_back_button)
    else:
      print("No builds received.")

  def build_selected(self, sender, **event_args):
    """Handle the build selection and populate the dropdowns on Form1"""
    selected_build = sender.tag.build_data

    ########## last working here
    
    # Call the method from Form1 to populate the form
    get_open_form('Form1').load_build(selected_build)

  def go_back(self, **event_args):
    """Close the alert without selecting a build"""
    open_form('Form1')
