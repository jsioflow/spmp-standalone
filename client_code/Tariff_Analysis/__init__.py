from ._anvil_designer import Tariff_AnalysisTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Tariff_Analysis(Tariff_AnalysisTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Logout")
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Settings")
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Home_Page")
    pass

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_1.content = anvil.server.call('get_tariff_analysis')
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

