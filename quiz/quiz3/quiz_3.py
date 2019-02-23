# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly_csv.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a year or a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx -- xxxx (with any number of spaces,
#   possibly none, around --) and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the first year can be posterior to the first year.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv


filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
month = input('Enter a month: ')
average = 0
years_above_average = []

# REPLACE THIS COMMENT WITH YOUR CODE
try:
    if source != 'GCAG' and source != 'GISTEMP':
        raise ValueError
except ValueError:
    print('Wrong source input, giving up...')
    sys.exit()
#extract years from string (year_or_range_of_years) to max_year and min_year
import re
year_L = re.findall(r'\d+', year_or_range_of_years)
# year_L = re.split(r'[\s\-]+', year_or_range_of_years.strip())
try:
    if len(year_L) == 2:
        if int(year_L[1]) >= int(year_L[0]):
            max_year = int(year_L[1])
            min_year = int(year_L[0])
        if int(year_L[1]) < int(year_L[0]):
            max_year = int(year_L[0])
            min_year = int(year_L[1])
    elif len(year_L) == 1:
        max_year = min_year = int(year_L[0])
    else:
        raise ValueError
except ValueError:
    print('Wrong year input, giving up...')
    sys.exit()
# build a mapping between English month and digit month by dictionary
month_mapping = {'January': '01', 'February': '02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12', 'january': '01', 'february': '02', 'march':'03', 'april':'04', 'may':'05', 'june':'06', 'july':'07', 'august':'08', 'september':'09', 'october':'10', 'november':'11', 'december':'12', 'Jan': '01', 'Feb': '02', 'Mar':'03', 'Apr':'04', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12', 'jan': '01', 'feb': '02', 'mar':'03', 'apr':'04', 'jun':'06', 'jul':'07', 'aug':'08', 'sep':'09', 'oct':'10', 'nov':'11', 'dec':'12'}
try:
    num_month = int(month_mapping[month])
except KeyError:
    print('Wrong month input, giving up...')
    sys.exit()
# open and input data from csv file to list
data = []   # store year and mean, formula:[[year, mean], ...]
with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for item in reader:
        if reader.line_num == 1:
            continue
        if item[0] == source:
            date = item[1].split('-')
            if max_year >= int(date[0]) and min_year <= int(date[0]):
                if num_month == int(date[1]):
                    data.append([int(date[0]), float(item[2])])

sum_of_list = 0
for item in data:
    sum_of_list += item[1]
average = sum_of_list / len(data)
for item in data:
    if item[1] > average:
        years_above_average.append(item[0])
years_above_average = sorted(years_above_average)
        



print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
