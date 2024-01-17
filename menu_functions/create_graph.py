import csv
import matplotlib.pyplot as plt

def create_graph(filename):

    dates = []
    totals = []
    count = 0

    # Read the CSV file
    with open(filename, 'r') as infile:
        reader = csv.reader(infile)

        # Iterate through row and save one in every five entries
        for row in reader:

            count+=1

            if count % 5 == 0:
                # Grab dates -- first cell in the row
                date = row[0]
                dates.append(date)

                # Grab the total balance -- last cell in the row
                total = float(row[-1])
                totals.append(total)
            

    # Create a basic line plot, format labels to look nice
    plt.plot(dates, totals)
    plt.gcf().autofmt_xdate()

    # Add labels and title
    plt.xlabel('Dates')
    plt.ylabel('Total Balance')
    plt.title('Total Balances Over All Time')

    # Show the plot
    plt.show()
