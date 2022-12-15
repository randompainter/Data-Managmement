import json

# Functions

def read_file(file_name):
    file = open(file_name, 'r')
    info = json.load(file)
    file.close()
    return info

def write_data(selected_data, save_to):
    file = open(save_to, 'w')
    json.dump(selected_data, file)
    file.close()

def selection_sort(anArray, sort_param, compare_funct):
    for fill_slot in range(len(anArray)):
        min_pos = fill_slot

        for post_fill in range(fill_slot +1, len(anArray)):
            
            if compare_funct(anArray[post_fill][sort_param], anArray[min_pos][sort_param]):
                min_pos = post_fill

        anArray[min_pos], anArray[fill_slot] = anArray[fill_slot], anArray[min_pos]

def sort_inc(val_1, val_2):
    if val_1 < val_2:
        return True

def sort_dec(val_1, val_2):
    if val_1 > val_2:
        return True

def search_data(list, key, val):
  for item in list:
      if item[key] == val:
          return list.index(item)

  return -1

def login(user_list):
    print("Please login to access data...")

    login_username = input("Username: ")
    login_password = input("Password: ")

    if check_creds(user_list, login_username, login_password):
        user_info = open_user_spec_fav_list(user_list, login_username)
        return user_info

    else:
        return -1

def sign_up(user_list):
    # Sign up function
        print("Please create username and password...")

        sign_up_username = input("Username: ")
        sign_up_password = input("Password: ")

        if check_creds(user_list, sign_up_username, sign_up_password):
            print("Username/Password already in use")
        else:
            user_list.append(create_new_acc(sign_up_username, sign_up_password))
            write_data(user_list, './text-files/users.txt')

def create_new_acc(username, password):
    dict = {
        "Username": username,
        "Password": password,
        "Favorites": []
    }

    return dict

# Take in username and password along with the list of credentials
# Return True or False
def check_creds(list, username, password):
    for i in range(0, len(list)):
        if list[i]["Username"] == username and list[i]["Password"] == password:
            return True

    return False

def open_user_spec_fav_list(list, username):
    for i in range(0, len(list)):
        if list[i]["Username"] == username:
            return list[i]