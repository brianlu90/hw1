# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061120.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
target_data = []
stations = [{'name': 'C0A880', 'sum': 0.0, 'count': 0},
            {'name': 'C0F9A0', 'sum': 0.0, 'count': 0},
            {'name': 'C0G640', 'sum': 0.0, 'count': 0},
            {'name': 'C0R190', 'sum': 0.0, 'count': 0},
            {'name': 'C0X260', 'sum': 0.0, 'count': 0}]

# Retrive ten data points from the beginning.
#target_data = data[:10]
for row in data:
    for station in stations:
        if row['station_id'] == station['name']:
            if (row['PRES'] != '-99.000') and (row['PRES'] != '-999.000'):
                station['sum'] = station['sum'] + float(row['PRES'])
                station['count'] = station['count'] + 1
for station in stations:
    if station['count'] != 0:
        target_data.append([station['name'], float("{:.3f}".format(station['sum'] / station['count']))])
    else:
        target_data.append([station['name'], 'None'])
#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================