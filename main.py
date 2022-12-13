# Data management project
import json

# Import game data
with open("game-data.txt", "r") as file_ref:
    game_list = json.load(file_ref)

favorite_list = []
user = 0
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
        print(game["Name"], "(" + game["Genre"] +")")

def search(list, name):
    for game in range(len(list)):
        if game_list[game]["Name"] == name:
            return game
    return -1

def search_game():
    print("Search by game name")
    selected_game = input("\nEnter a game name to search for: ").title()
    position = search(game_list, selected_game)
    if position != -1:
        print("Closest Matching Result: ")
        print("Name:", game_list[position]["Name"])
        print("Genre:", game_list[position]["Genre"])
        print("Price:", game_list[position]["Price"])
    else:
        print("Game was not found")        

def search_letter():
    counter = 0
    user_input = input("Enter a letter to find all available games that start with that letter: ").title()
    for game in game_list:
        if user_input == game["Name"][0]:
            print("\nClosest Matching Results:")
            print(game["Name"])
            counter += 1
    print("\nThere are", counter , "games found that start with the letter", user_input)

def search_genre():
    genre_counter = 0
    search_genre = input("Enter a genre to search for games: ").title()
    for game in game_list:
        if search_genre == game["Genre"]:
            print(game["Name"])
            genre_counter += 1
    print("There are", genre_counter, "games found of the", search_genre.capitalize(), "genre")
            
def sort_genre(): 
    bubbleSort(game_list, "Genre")
    for game in game_list:
        print(game["Genre"], ":", game["Name"])

def sort_ranking():
    bubbleSort(game_list, "Ranking")
    for game in game_list:
        print(str(game["Ranking"]) + ".", game["Name"])

def sort_price_below():
    for game in game_list:
      if game["Price"] <= 10:
        print(str(game["Name"]), "(" + str(game["Price"]) + " $)")

def sort_price_above():
    for game in game_list:
      if game["Price"] >= 20:
        print(str(game["Name"]), "(" + str(game["Price"]) + " $)")

def sort_name():
    bubbleSort(game_list, "Name")
    for game in game_list:
        print( "-" + str(game["Name"]))
    
def login_menu():
    print("Login Menu")
    print("1. Login")
    print("2. Register")
    login = input("What would you like to do: ")
    if login == "1":
        main()
    elif login == "2":   
        main()



def save_data(data, save):
    file = open(save, "w")
    json.dump(data, file)
    file.close()
        

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
        # Sort games by (Genre, Price, Name, and Ranking)
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
            print("hello")
        elif selection == "5":
            print(favorite_list)
        elif selection == "6":
            print("Hello")
        elif selection == "7":
            loop = False
            print("Closing my contact...")
        else: 
            print("Please use a valid function(1-6) ")

login_menu()



