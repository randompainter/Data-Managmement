# Data management project
import json

#   with open("game-data.txt", "r") as file_ref:
#    game_list = json.load(file_ref)

# Import game data and JSON
file = open("game-data.txt")
game = file.read()
file.close()

game_list = json.loads(game)

file = open("users.txt", "r")
user = file.read()
file.close()

users = json.loads(user)

# Favourites (name, genre, price)
favourites = [ ]


# Functions
def bubbleSort(anArray, item):
    for i in range(len(anArray)):
        for nums in range(0, len(anArray) - i - 1):
            if anArray[nums][item] > anArray[nums + 1][item]:
                temp = anArray[nums]
                anArray[nums] = anArray[nums + 1]
                anArray[nums + 1] = temp 

def display_game():
    for game in game_list:
        print(game["name"], "(" + game["genre"] +")")

def search(list, name):
    for game in range(len(list)):
        if game_list[game]["name"] == name:
            return game
    return -1

def search_game():
    print("\n(Search by game name)")
    selected_game = input("\nEnter a game name to search for: ").title()
    position = search(game_list, selected_game)
    if position != -1:
        print("Closest Matching Result: ")
        print("Name:", game_list[position]["name"])
        print("Genre:", game_list[position]["genre"])
        print("Price:", game_list[position]["price"])
        print("Ranking:", game_list[position]["ranking"])
    else:
        print("Game was not found")        

def search_letter():
    counter = 0
    user_input = input("Enter a letter to find all available games that start with that letter: ").title()
    for game in game_list:
        if user_input == game["name"][0]:
            print("\nClosest Matching Results:")
            print(game["name"])
            counter += 1
    print("\nThere are", counter , "games found that start with the letter", user_input)

def search_genre():
    genre_counter = 0
    search_genre = input("Enter a genre to search for games: ").title()
    for game in game_list:
        if search_genre == game["genre"]:
            print("\n(" + str(game["name"]) + ")")
            genre_counter += 1
    print("\nThere are", genre_counter, "games found of the", search_genre.capitalize(), "genre")
            
def sort_genre(): 
    bubbleSort(game_list, "genre")
    for game in game_list:
        print(game["genre"], ":", game["name"])

def sort_ranking():
    bubbleSort(game_list, "ranking")
    for game in game_list:
        print(str(game["ranking"]) + ".", game["name"])

def sort_price_below():
    for game in game_list:
      if game["price"] <= 10:
        print(str(game["name"]), "(" + str(game["price"]) + " $)")

def sort_price_above():
    for game in game_list:
      if game["price"] >= 20:
        print(str(game["name"]), "(" + str(game["price"]) + " $)")

def sort_name():
    bubbleSort(game_list, "name")
    for game in game_list:
        print( "-" + str(game["name"]))

def newUser(username, password):
	return {
		"username": username,
		"password": password,
		"favorites": [ ]
	}
# Search for existing users
def find_account(info, item): 
    for i in range(len(users)):
        if users[i][info] == item:
            return i
    return -1

def register_account():
    # Create an account and append it to the text file
    username = input("What would you like your username to be: ")
    password = input("What would you like your password to be: ")
    users.append(new_user(username, password))
    # Save new account to user file
    add_user =  json.dumps(users)
    file = open("users.txt", "w")
    file.write(add_user)
    file.close()

find_user = 0
def login_menu():
    # Login menu
    print("|Game Library Login Menu|")
    print("1. Login")
    print("2. Register")
    # Might delete this 
    print("3. Continue as guest")
    login_input = input("What would you like to do: ")
    if login_input == "1":
        # Enter correct username and password to login else boot back to login menu
        user_name = input("\nEnter Username: ")
        find_user = find_account("username", user_name)
        if find_user != -1:
            pass_word = input("Enter Password: ")
            find_pass = find_account("password", pass_word)
            # If password and username is correct log in
            if find_pass != -1:
                print("\n(You have successfully logged in)")
                main()
            else:
                print("\nUsername or password does not match, please try again")
                login_menu()
        else:
            print("Username does not exist try registering")
            login_menu()
    elif login_input == "2":  
        # Register an account  
        register_account()
        print("Once you have sucessfully created an account try logging in")
        login_menu()
    elif login_input == "3":
        # Use menu without logging in
        main()


def new_user(username, password):
    return { 
        "username": username,
        "password": password,
        "favorites": []
    }

def exit():
    # Save all changes made when exiting
    exit = json.dumps(users)
    file = open("users.txt", "w")
    file.write(exit)
    file.close()

    # Prompt users to login again or register new account after they exit the program
    login_menu()

def add_favorite():
    # Add game to favorite list
    fav_game = input("What game would you like to add to your favourites? ").title()
    game = search(game_list, fav_game)
    if game != -1:
        users[find_user]["favorites"].append(game_list[game])
        print("Game added")

        users_file = json.dumps(users)
        file = open("users.txt", "w")
        file.write(users_file)
        file.close()
    else:
        print("\nGame cannot be added to the list, please try again or check if its already in the list")
        
def remove_favorites():
    # Remove game from favorite list
    remove_selected = input("Enter the game would you like to remove from the list: ").title()
    remove = search(users[find_user]["favorites"], remove_selected)
    if remove == -1:
        users[find_user]["favorites"].pop(remove)

        users_json = json.dumps(users)
        file = open("users.txt", "w")
        file.write(users_json)
        file.close()

        print("Game removed from favorites")
    else:
        print("Game not found in list")

def display_favorite():
    # Display favorite games
    print("Favorite List: ")
    for favourite in users[find_user]["favorites"]:
        print("\nName: ", favourite["name"], "\nGenre: ", favourite["genre"], "\nRanking: ", favourite["ranking"])       

# Main program
def main():
    loop = True
    # Main Menu
    while loop: 
        # Menu Options
        print("\n|MAIN MENU|")
        print("1. Display List")
        print("2. Search for Games")
        print("3. Sort Games")
        print("4. Add to favorite")
        print("5. Remove from favorite")
        print("6. Display favorites")
        print("7. Logout")
        selection = input("\nSelect option (1-7): ")
        # Display all avaliable games
        if selection == "1":
                print("\nAll Games: ")
                display_game()
        # Option 2 (Search games)    
        elif selection == "2":
            print("1. Search game by name")
            print("2. Search game by initial letter")
            print("3. Search game by genre")
            search_option = input("Enter the type of search available (1-3): ")
            if search_option == "1":
                search_game()
            elif search_option == "2":
                search_letter()
            elif search_option == "3":
                search_genre() 
            else:
                print("Invalid action")
        # Sort games by (genre, price, name, and ranking)
        elif selection == "3":
            print("1. Sort game by name (Alphabetical)")
            print("2. Sort game by genre (Alphabetical)")
            print("3. Sort game by prices (Below 10$)")
            print("4. sort game by price (Above 20$)")
            print("5. Sort game by ranking (Top Seller)")
            sort_option = input("\nHow do you want to sort your game? (1-3): ")
            if sort_option == "1":
                sort_name()
            elif sort_option == "2":
                sort_genre()
            elif sort_option == "3":
                sort_price_below()
            elif sort_option == "4":
                sort_price_above()
            elif sort_option == "5":
                sort_ranking()
            else: 
                print("Invalid sorting function")
        # Add game to favorite
        elif selection == "4":
            add_favorite()
        elif selection == "5":
            remove_favorites()
        elif selection == "6":
            display_favorite()
        elif selection == "7":
            loop = False
            print("(User has logged out)")
            exit()
        else: 
            print("Please use a valid function(1-6) ")

login_menu()



