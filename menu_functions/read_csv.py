import csv
from colorama import *

def read_csv(filename):

    text_adjust = 16
    header_read = False
    
    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # Iterate over the remaining rows
        for row in csv_reader:

            # Iterate through each item in the row
            for i in range(0, len(row)):
                print('|', end='')

                # Logic if we haven't read the header info, bolded styling for header
                if(header_read == False):
                   print(f'{Style.BRIGHT}{row[i].ljust(text_adjust)}{Style.RESET_ALL}', end='')

                # Logic if we have read the header info, interchange between light and dark styling
                else:
                    if i % 2 == 0:
                        print(f'{Fore.LIGHTBLACK_EX}{row[i].ljust(text_adjust)}{Style.RESET_ALL}', end='')
                    else:
                        print(f'{Fore.LIGHTWHITE_EX}{row[i].ljust(text_adjust)}{Style.RESET_ALL}', end='')
            print('')
            header_read = True
