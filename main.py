import csv

# Read CSV file

data_sheet = csv.reader(open('data.csv', 'r'))

# Convert data to list
data_sheet = list(data_sheet)

data_sheet_header = data_sheet.pop(0)

data_set = set(tuple(x) for x in data_sheet)
data_sheet_filtered = [list(x) for x in data_set]

with open('data_filtered.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data_sheet_header)
    writer.writerows(data_sheet_filtered)
