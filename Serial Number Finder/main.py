"""
main.py

Description:
    This module provides utility functions to recursively search through a directory
    tree and find serial numbers in text files. It collects the file names and the
    corresponding serial numbers matching a specific pattern and logs the results
    with a timestamp and execution duration.

Author: Alejandro Orozco Romo
Created: 2025-07-04
Last Modified: 2025-07-04
Python Version: 3.12

Dependencies:
    - os: for file and directory traversal
    - re: for regular expression matching
    - daterime:for timestamp generation
    - time: for measuring execution time
    - pathlib: for path handling
    - math: for rounding durations

License:
    MIT License
"""

import os
import re
import time
from datetime import datetime
from pathlib import Path
import math

beginning = time.time()
directory_path = "C:\\Users\\T480\\Desktop\\CURSOS\\Python\\Introduccion\\Dia_9\\serial_number_finder\\Mi_Gran_Directorio"
number_pattern = r"N\D{3}-\d{5}"
finder_numbers = []
finder_folders = []


# ----------------------------------------
# Section 1: Utility Funcitions
# ----------------------------------------


def get_current_date():
    """

    :return:
    """
    current_day = datetime.now()
    return f"{current_day.day}/{current_day.month}/{current_day.year}"


# ----------------------------------------
# Section 2: Core Funcitions
# ----------------------------------------


def search_serial_numbers(file,pattern):
    """

    :return:
    """
    this_file = open(file,'r')
    text = this_file.read()
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''


def search_directory_tree():
    """

    :return:
    """
    for directoy, subdirectory, file in os.walk(directory_path):
        for elements in file:
            result = search_serial_numbers(Path(directoy, elements),number_pattern)
            if result != '':
                finder_numbers.append(result.group())
                finder_folders.append(elements.title())


def show_all():
    """

    :return:
    """
    index = 0
    print('-' * 50)
    print(f"Search date: {get_current_date()}")
    print('\n')
    print('FILE\t\t\tNO. SERIE')
    print('-------------\t----------')
    for elements in finder_folders:
        print(f'{elements}\t{finder_numbers[index]}')
        index += 1
    print('\n')
    print(f'Finder numbers: {len(finder_numbers)}')
    end = time.time()
    duration = end - beginning
    print(f'Search duration: {math.ceil(duration)}')
    print('-' * 50)


search_directory_tree()
show_all()

