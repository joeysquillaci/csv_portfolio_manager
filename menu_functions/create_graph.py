import csv

def create_graph(filename):

    dates = []
    totals = []

    # Read the CSV file
    with open(filename, 'r') as infile:
        reader = csv.reader(infile)

        for row in reader:

            # Grab dates
            date = row[0]
            dates.append(date)

            # Grab the information in the last cell of the row
            total = row[-1]
            totals.append(total)
            
    for i in range(0, len(dates)):
        print(dates[i] + ' ' + totals[i])