#External imports
import os
#Internal imports
import Menu
import Request

#Program Flow
class Main:
    request = Request.Request()
    menu = Menu.Menu()
    menu.display_menu()
    request.set_station(menu.selectStation())
    os.system('cls' if os.name == 'nt' else 'clear')

    print("**INITIAL DATE SELECTION**")
    request.set_initial_date(menu.selectDate())
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("**FINAL DATE SELECTION**")
    request.set_final_date(menu.selectDate())
    os.system('cls' if os.name == 'nt' else 'clear')
    
    request.set_aggregation(menu.selectAggregate())
    os.system('cls' if os.name == 'nt' else 'clear')
    
    request.set_data(menu.selectData())
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("**REQUEST SUMMARY**")
    
    
