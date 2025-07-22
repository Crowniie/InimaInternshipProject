import os 
class Menu:
    def display_menu(self):
        print("Welcome to GS Inima's weather extraction system")
        
    def selectStation(self):
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
        print("**DATE SELECTION**")
        print("Please enter the year:")
        year = int(input())
        print("Please enter the month:")
        month = int(input())
        print("Please enter the day:")
        day = int(input())
        
        print("**TIME SELECTION**")
        while hour < 0 or hour > 23:
            print("Please enter the hour(Use military format):")
            hour = int(input())
            if hour <= 9:
                hour = f"0{hour}"
                
        while minute < 0 or minute > 59:
            print("Please enter the minute:")
            minute = int(input())
            if minute not in range(0, 59):
                print("Please introduce a valid minute.")

        while second < 0 or second > 59:
            print("Please enter the second:")
            second = int(input())
            if second not in range(0, 59):
                print("Please introduce a valid second.")
        return f"{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}"
            

        
        


