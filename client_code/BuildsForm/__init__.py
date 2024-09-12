from ._anvil_designer import BuildsFormTemplate
from ..Form1 import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class BuildsForm(BuildsFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
 # Loop through each build and create buttons
    for build_name in builds:
      btn = Button(text=build_name)
      btn.role = 'build-button'  # Optional: assign a role for custom styling
      btn.set_event_handler('click', self.build_selected)  # Event handler for clicking a button
      btn.build_name = build_name  # Store the build name in the button
            
            # Add the button to the column panel
      self.column_panel.add_component(btn)

    def build_selected(self, sender, **event_args):
        """Handles what happens when a build is selected"""
        selected_build = sender.build_name
        # Pass this information back to Form1 and update the dropdowns
        get_open_form().populate_form_with_build(selected_build)
        # Close the form after selection
        self.remove_from_parent()
