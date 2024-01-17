from menu_functions.read_csv import *
from menu_functions.curr_bal import *
from menu_functions.add_entry import *

def choose_function(choice, filename):

    if(choice == '1'):
        print("See current balances:\n")
        curr_bal(filename)

    elif(choice == '2'):
        print("See full history of balances:\n")
        read_csv(filename)

    elif(choice == '3'):
        print("See graphs of balances over all time\n")

    elif(choice == '4'):
        add_entry(filename)

    elif(choice == 'x'):
        print('You have exited the program\n')
        exit

    else:
        print("error")