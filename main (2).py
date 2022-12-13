# Game Manager
import json

# Dictionary
# Soring ideas(Alphabet, genre, price)
games = [
{
    "name": "Call of The Goats",
    "genre": "Horror",
    "price": "40.99$"
},
{
    "name": "Forkknife",
    "genre": "Puzzle",
    "price": "53.78$"
},
{
    "name": "Lost in Woods",
    "genre": "Action",
    "price": "24.56$"
},
{
    "name": "Sleender Men",
    "genre": "Mystery",
    "price": "9.99$"
},
{
    "name": "Garbage Truck Simlator",
    "genre": "Casual",
    "price": "5.99$"
},
{
    "name": "Joe the Joker",
    "genre": "Horror",
    "price": "1.99$"
},
{
    "name": "Not Finding Bigfoot",
    "genre": "Shooter",
    "price": "1.99$"
},
{
    "name": "Valor Rant",
    "genre": "Open-World",
    "price": "99$"
},
{
    "name": "Leauge of Worthless",
    "genre": "Battle Royale",
    "price": "Free"
},
{
    "name": "Pokeman Beeps",
    "genre": "Rhythm",
    "price": "45.99$"
}
]


# Favourites (Title, Genre, Prices)
favorite_list = [ ]

# Save favorite_list using JSON
file = open("account.txt", "r")
user_from_file = file.read()
file.close()

users = json.loads(user_from_file)


# FUNCTIONS
foundUser = 0

def bubbleSort(anArray):
   
  for i in range(len(anArray) - 1):
 
    for j in range(0, len(anArray) - i - 1):
      if anArray[j] > anArray[j + 1]:
        anArray[j], anArray[j+1] = anArray[j+1], anArray[j]  
               
def search(anArray, name):
    for i in range (len(anArray)):
        if anArray[i]["name"] == name:
            return i
    return -1

# Menu Option Functions
def display_game():
    for game in games:
        print(game["name"])

def search_game():
    # Fix Capitalization issue
    search_game = input("Please enter a game you want to look up: ").title()
    index = search(games, search_game)
    if index != -1:
        print("Title:",games[index]["name"])
        print("Genre:",games[index]["genre"]) 
        print("Prices:",games[index]["price"])
    else:
        print("Movie not found")  

def sortgenre(): 
    bubbleSort(games, "genre")
    for game in games:
        print(game["genre"], ":", game["name"])

def add():
    newtitle = input("What is the name of this game? ")
    searching = search(games, newtitle)
    if searching == -1:
        newgenre = input("What is the genre for this game? ")
        newdir = input("What is the price for this game? ")
        print("Movie Added")
        newMovie = {
            "name": newtitle,
            "genre": newgenre,
            "price": newdir
        }
        games.append(newMovie)
    else: 
        print("Movie already in the list.")

def remove():
    removemov = input("What is the name of the game you would like to delete? ")
    index = search(games, removemov)
    if index != -1:
        games.pop(index)
        print("Movie deleted.")
    else:
        print("Movie not found")

def addfav():
    favMovie = input("What game would you like to add to your favorite_list? ")
    game = search(games, favMovie)
    alrMovie = search(users[foundUser]["faves"], favMovie)
    if game != -1 and alrMovie == 1:
        users[foundUser]["faves"].append(games[game])
        print("Movie added")

        users_json = json.dumps(users)
        file = open("account.txt", "w+")
        file.write(users_json)
        file.close()
    else:
        print("\nMovie can not be added to the list. Check if it is already in favorite_list or if it is not in your general games list.")

def removefav():
    remfavMovie = input("What game would you like to remove from your favorite_list? ")
    index = search(users[foundUser]["faves"], remfavMovie)
    if index != -1:
        users[foundUser]["faves"].pop(index)

        users_json = json.dumps(users)
        file = open("account.txt", "w+")
        file.write(users_json)
        file.close()

        print("Movie removed")
    else:
        print("Movie not in list.")

def displayfav():
    print("\nFAVOURITES:")
    for favourite in users[foundUser]["faves"]:
        print("\nTitle: ", favourite["name"], "\nGenre: ", favourite["genre"], "\nDirector: ", favourite["price"])

def exit():
    users_json = json.dumps(users)
    file = open("account.txt", "w+")
    file.write(users_json)
    file.close()

    print("Tip #1: Change password to keep the hackers ")
    login()


# MAIN MENU
# Menu Options 
def getMenuSelection():
    # Menu Options
    print("\nGame Platform Main Menu")
    print("\n1: Display all games")
    print("2: Search for a game")
    print("3: Sort game by genre")
    print("4: Sort game by price")
    print("5: Add to favorites")
    print("6: Remove from favorites")
    print("7: Display Favorites")
    print("8: Show friends list")
    print("9: find a friend")
    print("10: Add a friend")
    print("11: Remove friend")
    print("12: Logout")

    return input("\nChoose an option (1-12): ").lower()

# Main Menu
def mainMenu(): 
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1":
            display_game()
        elif selection == "2":
            search_game()
        elif selection == "3":
            sortgenre()
        elif selection == "4":
            addfav()
        elif selection == "5":
            removefav()
        elif selection == "6":
            displayfav()
        elif selection == "7":
            add()
        elif selection == "8":
            remove()
        elif selection == "12":
            exit()
            loop = False
        else: 
            print("Please choose an option. ")


# LOGIN/LOGOUT
def create_account():
    user_name = input("\nWhat would you like your username to be? ")
    user_password = input("What would you like your password to be? ")
    users.append(newUser(user_name, user_password))

def newUser(username, password):
    return {
        "username": username,
        "password": password,
        "faves": [ ]
    }

# Find the username or password
def findUP(usernameorpassword, item): 
    for i in range(len(users)):
        if users[i][usernameorpassword] == item:
            return i
    return -1

def login():
    print("\nLogin to your (Insert Name) account")
    user_name = input("Username: ")
    foundUser = findUP("username", user_name)
    if foundUser != -1:
        passw = input("Password: ")
        foundPass = findUP("password", passw)
        if foundPass != -1:
            mainMenu()
        else:
            print("Wrong Password!")
            login()
    else:
        print("No account found. Please register.")
        create_account()
        mainMenu()

# Login to your account
print("Main Menu")
print("1. Login to your account")
print("2. Register an account")
login_menu = input("Welcome to your game library (Login or Register?) ")
if login_menu == "login".capitalize() or login_menu == "1":
    login()
elif login_menu == "register".capitalize or login_menu == "2"():
    create_account()
    print("New account registered")
    login()

