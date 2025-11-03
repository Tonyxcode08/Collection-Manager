#Module Imports
from tabulate import tabulate
import os

#Runime Variables
running = True


#-----------------------FILE OPERATIONS-----------------------

#Function to load from file
def load_from_file():
    data = []
    with open("games.txt") as file:
        for line in file:
            parts = line.strip().split(", ")
            game, owned = parts
            data.append({"Game" : game, "Owned" : owned})
    return data

#Function to save data to file
def save_to_file(data):
    new_content = []
    for row in data:
        line = f"{row['Game']}, {row['Owned']},\n"
        new_content.append(line)

    with open("games.txt", "w") as f:
        f.writelines(new_content)

#Function to save the table to a file
def print_to_file(table):
    with open("Table.txt", "w") as f:
        f.writelines(table)

##-----------------------TABLE SETUP-----------------------
#Display table
def display_table(data):
    print("\n")
    global table
    table = tabulate(data, headers="keys", tablefmt="grid", showindex=True)
    print(table, "\n")

#Assign Headers
data = load_from_file()
headers = list(data[0].keys())

#-----------------------MAIN LOOP-----------------------
while running:
    
    print("Welcome to my XBOX 360 game database! \n What do you want to do?")
    choice = int(input("\n Choose an option: \n 1. View Table \n 2. Edit table \n 3. Print Table to File \n 4. Quit \n "))
    
    match choice:
       #Option 1: View the table
        case 1:
            display_table(data)
        
        #Option 2: Edit the table
        case 2:
           index = int(input("Please type the index of the row you want to edit: \n "))
           selected_row = data[index]
           display_table([selected_row])
           confirm = str(input("Is this the row you want to edit? \n Y / N: "))
           match confirm:
                
                case "N":
                    continue
                
                case "Y":
                    selected_column = str(input("Please select the header of the column you want to edit: \n "))
                    new_value = input("What is your new value? \n ")
                    data[index][selected_column] = new_value 
                    display_table(data)
                    save_to_file(data)

        #Option 3: Print table to a file
        case 3:
            print("Printing to file...")
            print_to_file(table)
            print(" \n Done!")
            continue
        
        #Option 4: Quit the program
        case 4: 
            print("Bye!")
            break
            




