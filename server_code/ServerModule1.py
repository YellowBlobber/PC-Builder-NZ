import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

payload = { 'api_key': '9f67e09c5b0b7efd1e74ffe06d0884b1', 'url': 'https://www.computerlounge.co.nz/components#!categoryId=247&page=1&q=&scid=-1&isListMode=true&lastPage=39&Filters%5B0%5D.Key=Sort&Filters%5B0%5D.Value=1', 'session_number': '1' }
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.json())
