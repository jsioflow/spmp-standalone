from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# Any code you write here will run when the form opens.
    anvil.users.login_with_form()
    print(f'This is a test to see if this is triggered when a user is attempting to get a password')
    print(f"This user has logged in: {anvil.users.get_user()['email']}")
    #anvil.server.call('say_hello', 'Anvil Developer')
    self.text_box_3.text = 'test_text'
    

