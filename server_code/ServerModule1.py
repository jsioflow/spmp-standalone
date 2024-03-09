import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
import os
import csv
import sqlite3


def read_csv_to_dict(file_path):
    data_dict = {}
    
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        
        # Assuming the first row contains header keys
        headers = next(reader, None)
        
        if headers:
            for row in reader:
                # Use a dictionary comprehension to create the dictionary
                data_dict = {headers[i]: row[i] for i in range(min(len(headers), len(row)))}
    
    return data_dict
    
def write_dict_to_csv(file_path, data_dict):
    # Extract keys and values from the dictionary
    keys = list(data_dict.keys())
    values = list(data_dict.values())

    # Write the dictionary to a CSV file
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(keys)  # Write header
        writer.writerow(values)  # Write values

def display_parameters(dict):
    print("\nList of Recorded Parameters:")
    for parameter, value in dict.items():
        print(f"{parameter}: {value}")
        
def pick_parameter_value(dict, parameter):
    try:
        selected_value = dict[parameter]
        print(f"Associated Value for '{parameter}': {selected_value}")
        return selected_value
    except KeyError:
        print(f"Parameter '{parameter}' not found. Please choose a valid parameter.")

def record_parameter(dict, parameter, value):
    dict[parameter] = value
    print(f"Parameter '{parameter}' with value '{value}' recorded successfully.")

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# Defined definitions

parameter_dict = {}

@anvil.server.callable
def say_hello(name):
  print("Hello, " + name + "!")
  print
  
@anvil.server.callable
def get_config_parameter(test_parameter):
  new_directory = 'Desktop/SPMP/Database'
  os.chdir(new_directory)  
  configuration = read_csv_to_dict('config_parameters.csv')
  value = pick_parameter_value(configuration, test_parameter)
  return value

@anvil.server.callable
def save_configuration(parameter_dict):
  new_directory = 'Desktop/SPMP/Database'
  os.chdir(new_directory)
  write_dict_to_csv('config_parameters.csv',parameter_dict)