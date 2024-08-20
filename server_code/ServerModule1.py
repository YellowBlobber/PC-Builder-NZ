import anvil.files
from anvil.files import data_files
import pandas as pd
import anvil.tables as tables
from anvil.tables import app_tables

import anvil.server  # Make sure you replace this with your own Uplink key
anvil.server.connect("YOUR-UPLINK-KEY")  # Make sure you replace this with your own Uplink key

def import_csv_data(file):
  with open(file, "r") as f:
    df = pd.read_csv(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.your_table_name_here.add_row(**d)
import_csv_data("PC Builder NZ data.csv")
      
def import_excel_data(file):
  with open(file, "rb") as f:
    df = pd.read_excel(f)
    for d in df.to_dict(orient="records"):
       #of {columnname -> value} for this row
       #We use Python's **kwargs syntax to pass the whole dict as
       #keyword arguments
      app_tables.table_5.add_row(**d)
import_excel_data("PC Builder NZ data.csv")


