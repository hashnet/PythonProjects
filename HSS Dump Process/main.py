import process
import csv
import os

filename = 'hssdata.txt'
# filename = 'sample.txt'
with open(filename, 'r') as f:
    input("Ensure that the file {} is placed in the same folder as the application and press enter.".format(filename))

    lst = process.process(f)

    print('\nTotal {} lines processed.'.format(len(lst) - 1))

    outfilename = 'output.csv'
    with open(outfilename, 'w', newline='') as out:
        w = csv.writer(out)
        for row in lst:
            w.writerow(row)

        print("\nProcessed data is stored in the following path.")
        print(os.path.abspath(outfilename))