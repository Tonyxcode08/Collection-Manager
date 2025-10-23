from tabulate import tabulate
import os

running = True

#Load from file
def load_from_file():
    data = []
    with open("games.txt") as file:
        for line in file:
            parts = line.strip().split(", ")
            game, owned = parts
            data.append({"Game" : game, "Owned" : owned})
    return data

#Save to file
def save_to_file(data):
    new_content = []
    for row in data:
        line = f"{row['Game']}, {row['Owned']},\n"
        new_content.append(line)

    with open("games.txt", "w") as f:
        f.writelines(new_content)


#Display table
def display_table(data):
    print("\n")
    print(f"{tabulate(data, headers="keys", tablefmt="grid", showindex=True)} \n")


data = load_from_file()
headers = list(data[0].keys())

while running:
    print("Welcome to my XBOX 360 game database! \n What do you want to do?")
    choice = int(input("\n Choose an option: \n 1. View Table \n 2. Edit table \n 3. Quit \n "))
    match choice:
        case 1:
            display_table(data)
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
        case 3:
            break




