import csv
from datetime import datetime
import logging

DEGREE_SYMBOL = "\N{DEGREE SIGN}C"


def format_temperature(temp):

    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    iso_date = datetime.fromisoformat(iso_string)
    human_readable = iso_date.strftime('%A %d %B %Y')
    return human_readable
# result = convert_date('2021-07-05T07:00:00+08:00')
# print(result)
        
"""Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """



# pass


def convert_f_to_c(temp_in_fahrenheit):
    temp_in_celsius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    return round(temp_in_celsius, 1)
    
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    # pass


def calculate_mean(weather_data):
    return sum([float(item) for item in weather_data]) / len(weather_data)

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # pass


def load_data_from_csv(file_path):
    weather_data = []
    with open(file_path) as weather_data_csv:
        csv_dictreader = csv.DictReader(weather_data_csv)
        for row in csv_dictreader:
            if row:
                weather_data.append([row["date"], float(row["min"]), float(row["max"])])
    return weather_data

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # pass


def find_last_occurrence(search_term, search_list):
    """Find the index of an item's last occurrence in a list.

    Args:
        search_term: The number (float) to search for.
        search_list: The list of items to search for.

    Returns:
        A tuple containing the search term and the index of its last occurrence in the list.
    """
    if not search_list:
        return ()
    temps = [float(point) for point in reversed(search_list)]
    value_index = len(search_list) - 1 - temps.index(search_term)
    return search_term, value_index

def find_min(weather_data):
    if not weather_data:
        return ()

    temps =[float(point) for point in weather_data]
    return find_last_occurrence(min(temps), temps)

"""Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # pass


def find_max(weather_data):
        if not weather_data:
         return ()

        temps =[float(point) for point in weather_data]
        return find_last_occurrence(max(temps), temps)

"""Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # pass
