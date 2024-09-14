def getNumberInput(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def getStringInput(message):
    while True:
        try:
            str = input(message)
            return str
        except ValueError:
            print("Invalid input. Please enter a valid input.")
def getBooleanInput(message):
     while True:
        try:
            user_input = input(f"{message} (Y/y/AnyKeys): ").strip()
            if user_input in ("Y", "y"):
                return True
            else:
                return False
        except ValueError:
            print("Invalid input. Please enter a valid input.")
def getOption(options=[]):
    if not options:
        print('There were no options to select')
        return None
    if not isinstance(options, list):
        print("Error: The provided options are not in a valid list format.")
        return None
    
    print('Choose Option: \n')
    for index, option in enumerate(options, start=1):
        print(f'{index}) {option}')
    while True:
        selected = getNumberInput('Enter the number of the option: ')
        
        if 1 <= selected <= len(options):
            return options[selected - 1]  
        else:
            print("Invalid selection. Please choose a number from the list.")
def pause():
    input("\nPress Enter To Continue....")
    
def printLine():
    print("____________________________________________________\n")  