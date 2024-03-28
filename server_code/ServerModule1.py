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
import numpy as np

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

# Get last line in data base and return as dataframe
def get_last_entry_as_dataframe(database, table_name):

    connection = sqlite3.connect(database)
    query = f"SELECT * FROM {table_name} ORDER BY ROWID DESC LIMIT 1"

    try:
        # Use pandas to read the result into a DataFrame
        last_entry_df = pd.read_sql_query(query, connection)

        return last_entry_df if not last_entry_df.empty else None

    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None

    finally:
        # Close the connection
        connection.close()
        
def read_table_into_dataframe(db_file, table_name):
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)

    # Build SQL query to select all rows from the specified table
    select_query = f"SELECT * FROM {table_name}"

    # Execute the query and fetch the results as a DataFrame
    dataframe = pd.read_sql_query(select_query, conn)

    # Close the connection
    conn.close()

    return dataframe
    
def get_after_last_space(input_string):
    # Find the index of the last space in the string
    last_space_index = input_string.rfind(' ')

    # Check if a space is found in the string
    if last_space_index != -1:
        # Extract characters after the last space
        result_string = input_string[last_space_index + 1:]
        return result_string
    else:
        # If no space is found, return an empty string
        return ""
    
def get_before_last_space(input_string):
    # Find the index of the last space in the string
    last_space_index = input_string.rfind(' ')

    # Check if a space is found in the string
    if last_space_index != -1:
        # Extract characters before the last space
        result_string = input_string[:last_space_index]
        return result_string
    else:
        # If no space is found, return the original string
        return input_string
    
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

@anvil.server.callable
def get_solar_power():
    new_directory = 'Desktop/SPMP/Database'
    os.chdir(new_directory)
    df_solar_power = get_last_entry_as_dataframe('solarplatform.db', 'myspm')
    solar_power = df_solar_power.loc[0,'SP_Watt']
    return solar_power

@anvil.server.callable
def get_battery_level():
    new_directory = 'Desktop/SPMP/Database'
    os.chdir(new_directory)
    df_battery_level = get_last_entry_as_dataframe('solarplatform.db', 'myspm')
    battery_level = df_battery_level.loc[0,'SP_Battery_Percent']
    return battery_level

@anvil.server.callable
def get_home_usage():
    new_directory = 'Desktop/SPMP/Database'
    os.chdir(new_directory)
    df_home_usage = get_last_entry_as_dataframe('solarplatform.db', 'myspm')
    home_usage = df_home_usage.loc[0,'Home_Watt']
    return home_usage
    
@anvil.server.callable
def get_tariff_analysis(days):
    new_directory = 'Desktop/SPMP/Tariffs'
    os.chdir(new_directory)
    # Read tariff information from CSV files
    df_tariffs = pd.read_csv('utility_plans.csv')
    
    os.chdir("..")
    new_directory = 'Database'
    os.chdir(new_directory)
    hourly_database = 'solarplatformhourly.db'
    hourly_table = 'mysphourly'
    hourly_table = read_table_into_dataframe_days(hourly_database, hourly_table, days)
    
    # Count the number of rows per date and filter out those with counts < 24
    filtered_dates = hourly_table.groupby('Date').filter(lambda x: len(x) >= 24)

    # Reset the index of df2
    filtered_dates = filtered_dates.reset_index(drop=True)
    dfChargeMatrix = filtered_dates
    
    #Time Label on Completion
    current_time = time.strftime('%H:%M:%S')

    list1 = []
    list2 = []

    # Read list of Tariff options form file and populate the Charge Matrix
    for column in df_tariffs.columns:
        list1.append(column)

    for x in range (0, len(dfChargeMatrix)):
        dfChargeMatrix.loc[x,'Hour'] = str(dfChargeMatrix.loc[x,'Hour'])

    # Iterate over Tariff options and update Charge Matrix based on matching rows in dfTariffs
    for tariffoption in list1[2:]:
        # Check if the tariff option exists as a column in dfTariffs
        if tariffoption in df_tariffs.columns:
            # Iterate over the rows in dfChargeMatrix
            for x in range(len(dfChargeMatrix)):
                # Find the corresponding row in dfTariffs based on 'Hours' and 'Day' columns
                matching_rows = df_tariffs[(df_tariffs['Hours'] == dfChargeMatrix.loc[x, 'Hour']) & (df_tariffs['Day'] == dfChargeMatrix.loc[x, 'Day'])]
                
                # Check if matching rows are found
                if not matching_rows.empty:
                    # Extract the tariff rate and update dfChargeMatrix
                    rate = matching_rows.iloc[0][tariffoption]
                    dfChargeMatrix.at[x, tariffoption + '_Rate'] = rate

    # Drop unnecessary columns from dfChargeMatrix
    dfChargeMatrix = dfChargeMatrix.drop(['Day'], axis=1)

    # Iterate over the remaining tariffs in the list
    for tariffoption in list1[2:]:
        # Calculate the tariff cost and update dfChargeMatrix
        dfChargeMatrix[tariffoption] = (dfChargeMatrix['Grid_Buy_kWh'] * dfChargeMatrix[tariffoption + '_Rate']) / 100

    ## Reformat the Charge Matrix ##
    df_summary = pd.DataFrame(columns=['Tariff Plan','Total Cost'])

    # Iterate over Tariff options and calculate total cost
    list1 = list1[2:]
    for l in range (len(list1)):
        tariffoption = (list1[l])
        df_summary.loc[l,'Tariff Plan'] = tariffoption
        df_summary.loc[l,'Total Cost'] = round((dfChargeMatrix[tariffoption].sum()),2)

    # Sort the summary DataFrame by total cost
    df_summary = df_summary.sort_values(['Total Cost'])

    # Format total cost as euros
    for x in range(0, len(df_summary)):
        df_summary.loc[x,'Total Cost'] = '€'+str(df_summary.loc[x,'Total Cost'])

    # Reset the index of dfSummary
    df_summary = df_summary.reset_index(inplace=False)
    del df_summary['index']
    # Resetting index starting at 1
    df_summary.reset_index(drop=True, inplace=True)
    df_summary.index += 1

    winner = df_summary.iloc[[0]].to_string(header=False, index=False)
    best_tariff = get_before_last_space(winner)
    best_cost = get_after_last_space(winner)
    
    winner = (f'The Best Tariff is the "{best_tariff}" at a Cost of {best_cost}')
    #print(winner)
    #print(df_summary)
    #print("Transaction Completed at: ",current_time)
    return winner, df_summary.to_markdown()

@anvil.server.callable
def get_days_analysis():
    new_directory = 'Desktop/SPMP/Tariffs'
    os.chdir(new_directory)
    # Read tariff information from CSV files
    df_tariffs = pd.read_csv('utility_plans.csv')
    
    os.chdir("..")
    new_directory = 'Database'
    os.chdir(new_directory)
    hourly_database = 'solarplatformhourly.db'
    hourly_table = 'mysphourly'
    hourly_table = read_table_into_dataframe(hourly_database, hourly_table)
    
    # Count the number of rows per date and filter out those with counts < 24
    filtered_dates = hourly_table.groupby('Date').filter(lambda x: len(x) >= 24)

    # Reset the index of df2
    filtered_dates = filtered_dates.reset_index(drop=True)
    dfChargeMatrix = filtered_dates
    days = (len(dfChargeMatrix)/24) - 3
    if days < 0:
        days = 0
    return days