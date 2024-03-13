import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
import time
from datetime import date, datetime, timedelta, timezone
import os
import csv
import sqlite3
import pandas as pd


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

# Parameter definitions
configuration_file = 'Desktop/SPMP/Database/config_parameters.csv'
configuration = read_csv_to_dict(configuration_file)
customer_id = pick_parameter_value(configuration, 'customer_id')

current_day = date.today().strftime('%Y-%m-%d')
current_time = time.strftime('%H:%M:%S')

@anvil.server.callable
def get_config_file():
  new_directory = 'Desktop/SPMP/Database'
  os.chdir(new_directory)  
  configuration = read_csv_to_dict('config_parameters.csv')
  return configuration

@anvil.server.callable
def save_configuration(parameter_dict):
  new_directory = 'Desktop/SPMP/Database'
  os.chdir(new_directory)
  write_dict_to_csv('config_parameters.csv',parameter_dict)
  
@anvil.server.callable
def get_aggregate_file():
  new_directory = 'Desktop/SPMP/Daily_Reports/Summaries'
  os.chdir(new_directory)  
  aggregate_data = read_csv_to_dict(f'daily_aggregate_{customer_id}_{current_day}.csv')
  return aggregate_data