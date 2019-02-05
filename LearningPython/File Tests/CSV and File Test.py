import csv
import os

# Normal file
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

print('\n')

with open('test.txt', 'r') as f:
    print(f.read())

print()

with open('test.txt', 'r') as f:
    line = f.readline()
    while line != '':
        print(line, end='')
        line = f.readline()
print('\n')

with open('test.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
print()


# CSV file
with open('test.csv', 'r') as csvFile:
    csvData = csv.reader(csvFile)
    print(csvData)
    for row in csvData:
        print(row)

with open('test.csv', 'r') as csvFile:
    csvData = csv.reader(csvFile)
    print(csvData)
    for row in csvData:
        print(', '.join(row))

with open(os.path.join('files', 'outputcsv.csv'), 'w', newline='') as outCsvFile:
    writer = csv.writer(outCsvFile)
    writer.writerline([1, 2, 3])