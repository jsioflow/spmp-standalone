from ._anvil_designer import SettingsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users

def record_parameter(dict, parameter, value):
    dict[parameter] = value
    print(f"Parameter '{parameter}' with value '{value}' recorded successfully.")

def display_parameters(dict):
    print("\nList of Recorded Parameters:")
    for parameter, value in dict.items():
        print(f"{parameter}: {value}")

class Settings(SettingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    open_form("Home_Page")
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Logout")
    pass

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    parameter1 = anvil.server.call('get_config_parameter', 'ip_address')
    self.text_box_1.text = parameter1
    parameter2 = anvil.server.call('get_config_parameter', 'customer_id')
    self.text_box_2.text = parameter2
    parameter3 = anvil.server.call('get_config_parameter', 'battery_capacity')
    self.text_box_3.text = parameter3
    parameter4 = anvil.server.call('get_config_parameter', 'location_region')
    self.text_box_4.text = parameter4
    parameter5 = anvil.server.call('get_config_parameter', 'location_name')
    self.text_box_5.text = parameter5
    parameter6 = anvil.server.call('get_config_parameter', 'timezone')
    self.text_box_6.text = parameter6
    parameter7 = anvil.server.call('get_config_parameter', 'battery_max_level')
    self.text_box_7.text = parameter7
    parameter8 = anvil.server.call('get_config_parameter', 'latitude')
    self.text_box_8.text = parameter8
    parameter9 = anvil.server.call('get_config_parameter', 'longitude')
    self.text_box_9.text = parameter9
    parameter10 = anvil.server.call('get_config_parameter', 'max_charge_w')
    self.text_box_10.text = parameter10
    pass

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    parameter_dict = {}
    record_parameter(parameter_dict, "ip_address", self.text_box_1.text)
    record_parameter(parameter_dict, "customer_id", self.text_box_2.text)
    record_parameter(parameter_dict, "battery_capacity", self.text_box_3.text)
    record_parameter(parameter_dict, "location_region", self.text_box_4.text)
    record_parameter(parameter_dict, "location_name", self.text_box_5.text)
    record_parameter(parameter_dict, "timezone", self.text_box_6.text)
    record_parameter(parameter_dict, "battery_max_level", self.text_box_7.text)
    record_parameter(parameter_dict, "latitude", self.text_box_8.text)
    record_parameter(parameter_dict, "longitude", self.text_box_9.text)
    record_parameter(parameter_dict, "max_charge_w", self.text_box_10.text)
    display_parameters(parameter_dict)
    anvil.server.call('save_configuration', parameter_dict)
    pass

   
    

