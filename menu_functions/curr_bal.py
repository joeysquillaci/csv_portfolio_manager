import csv
from colorama import *
from helper_funcs.get_header import *

def curr_bal(filename):

    text_adjust = 16

    header = get_header(filename)

    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # Iterate over the rows, only save last (most recent) row
        for row in csv_reader:
            row = row

        # Iterate through each item in the header
        for i in range(0, len(header)):
            print('|', end='')
            print(f'{Style.BRIGHT}{header[i].ljust(text_adjust)}{Style.RESET_ALL}', end='')

        print('')

        # Iterate through each item in the row
        for i in range(0, len(row)):
            print('|', end='')

            # Chooses color based on even or odd
            if i % 2 == 0:
                print(f'{Fore.LIGHTBLACK_EX}{row[i].ljust(text_adjust)}{Style.RESET_ALL}', end='')
            else:
                print(f'{Fore.LIGHTWHITE_EX}{row[i].ljust(text_adjust)}{Style.RESET_ALL}', end='')

    print('')

                
