from ._anvil_designer import LogoutTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
from time import sleep

class Logout(LogoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    sleep(3)
    anvil.users.logout()
    anvil.users.login_with_form()
    ## Return to Main Screen if the User logs in again
    open_form("Home_Page")
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Home_Page")
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Settings")
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Tariff_Analysis")
    pass
