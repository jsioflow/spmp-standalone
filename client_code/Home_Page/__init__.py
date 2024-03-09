from ._anvil_designer import Home_PageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Settings import Settings
from ..Logout import Logout
#from ..Form3 import Form3

class Home_Page(Home_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    anvil.users.login_with_form()
    print(f'This is a test to see if this is triggered when a user is attempting to get a password')
    print(f"This user has logged in: {anvil.users.get_user()['email']}")
    #anvil.server.call('say_hello', 'Anvil Developer')
    #self.text_box_3.text = 'test_text'

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Home_Page())
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Settings())
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Logout())
    pass
