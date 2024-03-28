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
    config_file = anvil.server.call('get_config_file')
    self.text_box_1.text = config_file.get('ip_address')
    self.text_box_2.text = config_file.get('customer_id')
    self.text_box_3.text = config_file.get('max_battery_capacity')
    self.text_box_4.text = config_file.get('location_region')
    self.text_box_5.text = config_file.get('location_name')
    self.text_box_6.text = config_file.get('timezone')
    self.text_box_7.text = config_file.get('battery_max_level')
    self.text_box_8.text = config_file.get('latitude')
    self.text_box_9.text = config_file.get('longitude')
    self.text_box_10.text = config_file.get('max_charge_w')
    self.text_box_11.text = config_file.get('forecast_source')
    self.text_box_12.text = config_file.get('sp_kWh_default')
    self.text_box_13.text = config_file.get('host')
    self.text_box_14.text = config_file.get('home_kWh_default')
    self.text_box_15.text = config_file.get('resource_id')
    self.text_box_16.text = config_file.get("api_key")
    self.text_box_17.text = config_file.get("timer")
    self.text_box_18.text = config_file.get("co2")
    pass

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    parameter_dict = {}
    record_parameter(parameter_dict, "ip_address", self.text_box_1.text)
    record_parameter(parameter_dict, "customer_id", self.text_box_2.text)
    record_parameter(parameter_dict, "max_battery_capacity", self.text_box_3.text)
    record_parameter(parameter_dict, "location_region", self.text_box_4.text)
    record_parameter(parameter_dict, "location_name", self.text_box_5.text)
    record_parameter(parameter_dict, "timezone", self.text_box_6.text)
    record_parameter(parameter_dict, "battery_max_level", self.text_box_7.text)
    record_parameter(parameter_dict, "latitude", self.text_box_8.text)
    record_parameter(parameter_dict, "longitude", self.text_box_9.text)
    record_parameter(parameter_dict, "max_charge_w", self.text_box_10.text)
    record_parameter(parameter_dict, "forecast_source", self.text_box_11.text)
    record_parameter(parameter_dict, "sp_kWh_default", self.text_box_12.text)
    record_parameter(parameter_dict, "host", self.text_box_13.text)
    record_parameter(parameter_dict, "home_kWh_default", self.text_box_14.text)
    record_parameter(parameter_dict, "resource_id", self.text_box_15.text)
    record_parameter(parameter_dict, "api_key", self.text_box_16.text)
    record_parameter(parameter_dict, "timer", self.text_box_17.text)
    record_parameter(parameter_dict, "co2", self.text_box_18.text)
    display_parameters(parameter_dict)
    anvil.server.call('save_configuration', parameter_dict)
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Tariff_Analysis")
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

   
    

