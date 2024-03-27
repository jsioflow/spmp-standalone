from ._anvil_designer import Home_PageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Settings import Settings
from ..Logout import Logout

class Home_Page(Home_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
#   print(f"This user has logged in: {anvil.users.get_user()['email']}")
    aggregate_data = anvil.server.call('get_aggregate_file')
    result1 = aggregate_data.get('Savings_from_Base_Plan')
    self.label_4.text = (f'€{result1}')
    result2 = aggregate_data.get('Savings_from_Chosen_Plan_with_SPMP')
    self.label_6.text = (f'€{result2}')
    result3 = aggregate_data.get('SP_kWh')
    self.label_9.text = (f'{result3} kWh')
    result4 = aggregate_data.get('Home_kWh')
    self.label_10.text = (f'{result4} kWh')
    result5 = aggregate_data.get('Kg_CO2')
    self.label_12.text = (f'{result5} Kg CO2')
    result6 = aggregate_data.get('Start_Date')
    self.label_14.text = (f'{result6}')
    result7 = aggregate_data.get('End_Date')
    self.label_19.text = (f'{result7}')
    solar_data = anvil.server.call('get_solar_power')
    self.label_18.text = (f'{solar_data} Watts')

    # Battery Level Section
    battery_data = anvil.server.call('get_battery_level')
    self.label_16.text = (f'{battery_data} %')
    if 1 < battery_data < 25:
        self.label_15.icon = 'fa:battery-1'
    if 25 < battery_data < 50:
        self.label_15.icon = 'fa:battery-2'
    if 50 < battery_data < 75:
        self.label_15.icon = 'fa:battery-3'
    if 75 < battery_data < 100:
        self.label_15.icon = 'fa:battery-4'
    if battery_data == 0:
        self.label_15.icon = 'fa:battery-empty' 

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

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Tariff_Analysis")
    pass

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    pass
