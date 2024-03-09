from ._anvil_designer import LogoutTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Logout(LogoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
   # self.label_1.visible = True
    sleep(3)
    anvil.users.logout()
    anvil.users.login_with_form()
    ## Return to Main Screen if the User logs in again
    open_form("MainForm")
    pass