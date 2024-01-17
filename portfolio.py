import csv
import colorama
from menu_functions.read_csv import *
from helper_functions.print_menu import *
from helper_functions.choose_function import *

filename = 'csv/portfolio.csv'
choice = ''

while(choice != 'x'):
    print('\n')
    choice = print_menu()
    choose_function(choice, filename)



