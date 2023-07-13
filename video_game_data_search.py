import csv
import textwrap
def generate_list_games(filename):

    main_list = []

    file_in = open(filename, encoding='UTF-8', errors='replace')

    file_in.readline()
    file_in = csv.reader(file_in)

    for line in file_in:
        if ";" in line[5]:
            line[5] = line[5].split(";")
        else:
            line[5] = [line[5]]
        if ";" in line[6]:
            line[6] = line[6].split(";")
        else:
            line[6] = [line[6]]
        if ";" in line[7]:
            line[7] = line[7].split(";")
        else:
            line[7] = [line[7]]
        if ";" in line[8]:
            line[8] = line[8].split(";")
        else:
            line[8] = [line[8]]
        if ";" in line[10]:
            line[10] = line[10].replace(";",",")
        
        
        
        main_list.append(line)

    return main_list
def print_menu(menu_list):

    print("\n"*5)
    for i in range(0, len(menu_list)):
        print(f'{i+1}. {menu_list[i]}')
def get_menu_selection(menu_list):

    possible_choice_values = []
    for i in range(0, len(menu_list)):
        possible_choice_values.append(str(i+1))

    choice = input("Type number to choose ... ")

    while choice not in possible_choice_values:
        print("Incorrect selection")
        print("\n"*30)
        
        print_menu(menu_list)
        choice = input("Type number to choose ...")

    return int(choice)
def get_all_possible_genres(list_of_games):

    genres = []
    
    for game in list_of_games:
        for genre in game[6]:
            if genre not in genres:
                genres.append(genre)

    genres.sort()
    return genres
def get_all_possible_keywords(list_of_games):

    keywords = [] #empty list where listings relating to keyword will be stored
    
    for game in list_of_games: #iterates through the list of listings
      keywords.append([game[0],game[-1]])#for each listing, the name and description is appended to the 'keywords' list

    keywords.sort() #sorts the listings
    return keywords
def print_genres(list_genres):

    print("\n\nAll genres available are:")
    print("-"*20)

    for item in list_genres:
        print(f'{item:<30}')
    
    print("\n")
def get_valid_genre(list_genres):

    genre = input("What genre would you like to filter for?")
    while genre not in list_genres:
        genre = input("Sorry that genre name is not valid. Please try again")
    
    return genre
def get_valid_keyword(list_keyword):
    print(textwrap.fill('Please enter a word that might be related to a game. This program will return all games with your word in the name or description.', width=70)) #print a textwrapped statement describing the type of input the user should provide
    keyword = input("What game are you looking for?")
    while True: #while loop to ask for a valid input until a valid input is recieved and the function is returned
      for name in list_keyword:#iterates through every item in the list
        if keyword.lower() in name[0].lower() or keyword.lower() in name[1].lower():#checks if the keyword exists in the list
          return keyword #returns the keyword and breaks out of the function
      else:#continues to ask for input when word is invalid
        keyword = input("That word does not exist. Try again. What game are you looking for?")
def get_valid_score():
    print('\n\nPlease input the lowest metacritic score you want to see.')
    score = input("Lowest score: ")
    while score.isdigit() == False or 0 >= int(score) or int(score) >= 100: #loops until input is a number. and is not less than or equal to 0 or greater or equal to 100
      score = input("score number is invalid. Try again: ") #asks for score again
    print('\n\nPlease input the highest metacritic score you want to see.')
    score1 = input("Highest score: ")
    while score1.isdigit() == False or 0 > int(score1) or int(score1) > 100 or int(score) > int(score1): #loops until input is a number. and is not less than 0 or greater 100. and is not less than the lower number
      score1 = input("score number is invalid. Try again: ")
    return [int(score), int(score1)] #returns as a list of two elements
def filter_all_listings_genre(list_of_games, genre):

    sub_list = []

    for item in list_of_games:
        if genre in item[6]:
            sub_list.append(item)

    return sub_list
def filter_all_listings_keywords(list_of_games, keyword):

    sub_list = [] #empty list to store games that fit the keyword

    for item in list_of_games:
        if keyword.lower() in item[0].lower() or keyword.lower() in item[-1].lower(): #checks if the keyword is in the name or description
            sub_list.append(item) #item appended if the keyword exists in the listing description or name
    return sub_list
def filter_all_listings_score(list_of_games, rate):

    sub_list = []

    for item in list_of_games:
        if item[2] != '': #checks if a metacritic score exists or not
          if rate[0]<=int(item[2]) and int(item[2])<=rate[1]: #if the metacritic score of the item is between the lowest and highest number of the user's selected range, the item is appended to sub_list
            sub_list.append(item)

    return sub_list
def get_valid_listing(list_games):

    possible_choice_values = []
    for i in range(0, len(list_games)):
        possible_choice_values.append(str(i+1))
    
    choice = input("Which listing would you like to choose?")

    while choice not in (possible_choice_values):
        choice = input("Invalid choice. Try another number")

    choice = int(choice) - 1

    return list_games[choice]
def print_listings_table(list_games):

    for i in range(0, len(list_games)):
        game = list_games[i]
        s = f"{i+1:<3} {game[0]:<30}"
        print(s)
def print_game_details(some_game):

    s = "\n"
    s += some_game[0]+"\n"+f"Released on: {some_game[1]}\n"
    s+= f"With a metacritic score of {some_game[2]}\n"
    s+= f"Rated {some_game[3]}\n"
    s+=f"With an average of {some_game[4]} hours of playtime.\n\n"
    if len(some_game[5])>=1:
        s+= 'Playable on:\n'
        for keyword in some_game[5]:
            s+= keyword+"\n"
        
    
        
    print(s)
def main():
    main_game_list = generate_list_games("video_game_data.csv")
    
    all_genres = get_all_possible_genres(main_game_list)
    all_keywords = get_all_possible_keywords(main_game_list)

    menu_items = ['See All Listings', 'Find game by genre', 'Find game by keyword', 'Find game by score', 'TBD', 'Exit']
    
    print_menu(menu_items)
    choice = get_menu_selection(menu_items)
    
    while 0 < choice and choice < len(menu_items):

        ##See all listings
        if choice == 1:
            print_listings_table(main_game_list)

        #Find listing by Genre
        elif choice == 2:
            print_genres(all_genres)
            genre = get_valid_genre(all_genres)

            sub_list_genres = filter_all_listings_genre(main_game_list, genre)
            print_listings_table(sub_list_genres)

            current_game = get_valid_listing(sub_list_genres)
            
            print_game_details(current_game)
            
        elif choice == 3:
            keyword = get_valid_keyword(all_keywords) #gets keyword

            sub_list_keyword = filter_all_listings_keywords(main_game_list, keyword) #gets a list of all the names and descriptions that include the keyword
            print_listings_table(sub_list_keyword) #prints all the found listings
  
            current_game = get_valid_listing(sub_list_keyword) #gets a listing choice from the user
              
            print_game_details(current_game) #prints the information for that game

        elif choice == 4:
            rate = get_valid_score() #gets the range of metacritic score

            sub_list_score = filter_all_listings_score(main_game_list, rate) #finds the list of games that have scores withing the user's range
            if len(sub_list_score) == 0: #prints a message when there are no listings in the chosen range
              print('There are no games with metacritic scores in this range.')
            else: 
              print_listings_table(sub_list_score) #prints a list of listings that match the user's range
  
              current_game = get_valid_listing(sub_list_score) #gets a listing choice from user
              
              print_game_details(current_game) #prints the information for that game
            

        elif choice == 5:
            pass
            

        print_menu(menu_items)
        choice = get_menu_selection(menu_items)
        

    print("\n\nGood bye!")
    
    



main()
