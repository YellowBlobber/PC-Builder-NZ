import anvil.files
from anvil.files import data_files
import pandas as pd
import anvil.tables as tables
from anvil.tables import app_tables
import xlwings as xw

import anvil.server
#anvil.server.connect("server_TOW2URT6HPMIOQ4SBOBSXHXW-7GMQAGE3DEN4GXX7")  # Make sure you replace this with your own Uplink ke
   
# read by default 1st sheet of an excel file
#PC_Builder_NZ_data = pd.read_excel('PC_Builder_NZ_data_test.xlsx')
#print(PC_Builder_NZ_data)
# Specifying a sheet

ws = xw.Book("Book2.xlsx").sheets['Sheet1']

# Selecting data from
# a single cell
v1 = ws.range("A1:A7").value

print("Result:", v1)

'''def import_excel_data(file):
  with open(file, "rb") as f:
    df = pd.read_excel(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.table_5.add_row(**d)
import_excel_data("PC_Builder_NZ_data_test.xlsx")'''


