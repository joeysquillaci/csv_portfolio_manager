import csv
from helper_funcs.get_header import *
from helper_funcs.write_row import *
from helper_funcs.compute_total import *

def add_entry(filename):

    valid_entry = False

    # Get header
    header = get_header(filename)

    # Only accept valid entries
    while(valid_entry == False):
            
        entry = []

        date = input("What date is this entry for?\n")
        entry.append(date)

        # Prompt user for balance, ignore "Date" and "Total" columns
        for i in range(1, len(header) - 1):
            balance = input("What is the balance of " + header[i] + "?\n")
            entry.append("{:.2f}".format(float(balance)))

        # Print entry back to user to verify validity
        print(entry) # TO DO 
        answer = input("Is this entry correct?\n")

        # Valid entry, compute total and write to csv file
        if(answer.lower() == 'y'):

            valid_entry = True
            total = compute_total(entry)
            entry.append(total)
            write_row(filename, entry)

        # Invalid entry, have user re-enter values
        elif(answer.lower() == 'n'):
            print("Please re-enter the entry details.\n")

        # Invalid response to entry validity question, reprompt to re-enter values
        else:
            print("Invalid answer, please re-enter entry details.\n")



