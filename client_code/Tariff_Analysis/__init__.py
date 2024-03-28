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

    # Days Available Data
    days_data = anvil.server.call('get_days_analysis')
    self.label_4.text = (f'{days_data}')

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
    days = 0
    if  5 < int(self.text_box_2.text) < (int(self.label_4.text) + 1):
        days = int(self.text_box_2.text)
    if int(self.text_box_2.text) > int(self.label_4.text):
        days = int(self.label_4.text)
        self.text_box_2.text = days
    if int(self.text_box_2.text) <= 5:
        days = int(self.label_4.text)
        self.text_box_2.text = days
    self.rich_text_1.content, self.rich_text_2.content = anvil.server.call('get_tariff_analysis', days)
    pass

