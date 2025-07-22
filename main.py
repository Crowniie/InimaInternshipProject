#External imports
import requests 
import os
#Internal imports
import Menu
import Request

#Program Flow
class Main:
    request = Request()
    Menu.display_menu()
    request.set_station(Menu.selectStation())
    os.system('cls' if os.name == 'nt' else 'clear')

    print("**INITIAL DATE SELECTION**")
    request.set_initial_date(Menu.selectDate())
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("**FINAL DATE SELECTION**")
    request.set_final_date(Menu.selectDate())
    os.system('cls' if os.name == 'nt' else 'clear')
    
    request.set_aggregate(Menu.selectAggregate())
    os.system('cls' if os.name == 'nt' else 'clear')
    
    request.set_data(Menu.selectData())
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("**REQUEST SUMMARY**")
    
    
