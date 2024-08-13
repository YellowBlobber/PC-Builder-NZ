import anvil.files
from anvil.files import data_files
import pandas as pd
import anvil.tables as tables
from anvil.tables import app_tables

import anvil.server  # Make sure you replace this with your own Uplink key

def import_excel_data(file):
  with open(file, "rb") as f:
    df = pd.read_excel(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.table_5.add_row(**d)
import_excel_data("PC_Builder_NZ_data_test.xlsx")
