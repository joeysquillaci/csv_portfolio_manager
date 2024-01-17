import csv

def write_row(filename, entry):

    with open(filename, 'a', newline='') as outfile:

        csv_writer = csv.writer(outfile)

        # Write the modified data
        csv_writer.writerow(entry)