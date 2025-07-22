class Menu:
    def display_menu(self):
        print("Welcome to Inima GS's weather extraction system")
        print("Please introduce the")
    
    def selectStation(self):
        print("Please select a station from the following list:")
        print("1. Station A")
        print("2. Station B")
        print("3. Station C")
        choice = input("Enter the number of your choice: ")
        return f"Station {choice}"
