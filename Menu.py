import os 
class Menu:
    def display_menu(self):
        print("Welcome to GS Inima's weather extraction system")
        
    def selectStation(self):
        choice = -1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please select a station from the following list:")
        print("1. Meteo Station Gabriel de Castilla")
        print("2. Meteo Station Juan Carlos I")
        
        while choice not in ['1', '2']:
            choice = input("Enter the number of your choice: ")
            if choice not in ['1', '2']:
                print("Please introduce a valid option.")
        return choice
    
    def selectDate(self):
        hour = -1
        minute = -1
        second = -1
        print("**DATE SELECTION**")
        print("Please enter the year:")
        year = int(input())
        print("Please enter the month:")
        month = int(input())
        print("Please enter the day:")
        day = int(input())
        
        print("**TIME SELECTION**")
        print("Please enter the hour(Use military format):")
        while hour < 0 or hour > 23:
            hour = int(input())
            if hour <= 9:
                hour = f"0{hour}"
        print("Please enter the minute:")      
        while minute < 0 or minute > 59:
            minute = int(input())
            if minute not in range(0, 60):
                print("Please introduce a valid minute.")
        
        print("Please enter the second:")
        while second < 0 or second > 59:
            second = int(input())
            if second not in range(0, 60):
                print("Please introduce a valid second.")
        return f"{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}"
    
    def selectAggregate(self):
        choice = -1
        print("Please select an aggregate type:")
        print("1. Daily")
        print("2. Hourly")
        print("3. Monthly")
        print("4. Yearly")
        while choice not in range(1, 5):
            choice = int(input("Enter the number of your choice: "))
            if choice not in range(1, 5):
                print("Please introduce a valid option.")
        return choice
    
    def selectData(self):
        choice = -1
        speedChoice = -1
        tempChoice = -1 
        presChoice = -1
        print("Do you wish to receieve all the data from AEMET?")
        print("0. Yes")
        print("1. No")
        while choice not in ['0', '1']:
            choice = input("Enter the number of your choice: ")
            if choice not in ['0', '1']:
                print("Please introduce a valid option.")
        if choice == '0':
            return True, True, True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Do you wish to recieve speed data?")
            print("0. Yes")
            print("1. No")
            while speedChoice not in ['0', '1']:
                speedChoice = input("Enter the number of your choice: ")
                if speedChoice not in ['0', '1']:
                    print("Please introduce a valid option.")
            speed = True if speedChoice == '0' else False       
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("Do you wish to recieve temperature data?")
            print("0. Yes")
            print("1. No")
            while tempChoice not in ['0', '1']:
                tempChoice = input("Enter the number of your choice: ")
                if tempChoice not in ['0', '1']:
                    print("Please introduce a valid option.")
            temperature = True if tempChoice == '0' else False
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("Do you wish to recieve pressure data?")
            print("0. Yes")
            print("1. No")
            while presChoice not in ['0', '1']:
                presChoice = input("Enter the number of your choice: ")
                if presChoice not in ['0', '1']:
                    print("Please introduce a valid option.")
            pressure = True if presChoice == '0' else False
            return temperature, pressure, speed
            