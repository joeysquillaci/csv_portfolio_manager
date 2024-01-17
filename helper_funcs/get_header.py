import csv

def get_header(filename):

    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # Iterate over the rows
        for row in csv_reader:

            header = row
            break

    return header