import constants
import random

NUMBER_OF_PLAYERS = len(constants.PLAYERS)
teams = []
players = []
names = []
guardians = []
experience = []
heights = []
experienced = []
inexperienced = []


def outline(word):
    print("-" * len(word))
    print(word)
    print("-" * len(word))


def import_teams(list_of_teams):
    for i in constants.TEAMS:
        teams.append(i)


# Imports the player names and makes a list of them
def player_names(list_of_players):
    for i in range(NUMBER_OF_PLAYERS):
        names.append(constants.PLAYERS[i]["name"])


# Makes a list of the player's guardians split into lists instead of strings
def player_guardians(list_of_players):
    guardians_unsplit = []
    for i in range(NUMBER_OF_PLAYERS):
        guardians_unsplit.append(constants.PLAYERS[i]["guardians"])
    for string in guardians_unsplit:
        guardians.append(string.split(" and "))


# Makes a list of the player's experience in boolean values
def player_experience(list_of_players):
    exp = []
    for i in range(NUMBER_OF_PLAYERS):
        exp.append(constants.PLAYERS[i]["experience"])
    for j in exp:
        if j == "YES":
            experience.append(True)
        else:
            experience.append(False)


# Makes a list of the player heights in ints
def player_height(list_of_players):
    heights_string = []
    for i in range(NUMBER_OF_PLAYERS):
        heights_string.append(constants.PLAYERS[i]["height"])
    for height in heights_string:
        heights.append(height.split())
    for i in range(NUMBER_OF_PLAYERS):
        del heights[i][1]
        heights[i] = int(heights[i][0])


# Makes the list players which is a list of dictionaries
def list_of_dicts(list1, list2, list3, list4):
    for i in range(NUMBER_OF_PLAYERS):
        player = {"name": list1[i],
                  "guardians": list2[i],
                  "experience": list3[i],
                  "height": list4[i],
                  }
        players.append(player)


def import_and_clean_data():
    import_teams(constants.TEAMS)
    player_names(constants.PLAYERS)
    player_guardians(constants.PLAYERS)
    player_experience(constants.PLAYERS)
    player_height(constants.PLAYERS)
    list_of_dicts(names, guardians, experience, heights)


def exp_inexp():
    player_list = players.copy()
    for player in player_list:
        for key, value in player.items():
            if key == "experience":
                if value is True:
                    experienced.append(player)
                elif value is False:
                    inexperienced.append(player)


# Populates teams with equal number of experienced and inexperienced players
def populate(team_name):
    players_per_team = int(NUMBER_OF_PLAYERS / len(teams))
    inexp_per_team = players_per_team / 2
    while len(team_name) < inexp_per_team:
        random_choice = random.randint(0, ((len(inexperienced) - 1)))
        player = inexperienced.pop(random_choice)
        team_name.append(player)
    while len(team_name) < players_per_team:
        random_choice = random.randint(0, ((len(experienced) - 1)))
        player = experienced.pop(random_choice)
        team_name.append(player)


def make_teams():
    team1 = []
    team2 = []
    team3 = []
    populate(team1)
    populate(team2)
    populate(team3)
    return team1, team2, team3


def display_teams():
    print("1) ", teams[0])
    print("2) ", teams[1])
    print("3) ", teams[2])


# Displays stats for a given team
def team_stats(team):
    team_players = []
    experienced_players = []
    inexperienced_players = []
    team_heights = []
    team_guardians = []
    for player in team:
        for key, value in player.items():
            if key == "name":
                team_players.append(value)
            if key == "experience":
                if value is True:
                    experienced_players.append(value)
                    exp = len(experienced_players)
                else:
                    inexperienced_players.append(value)
                    inexp = len(inexperienced_players)
            if key == "height":
                team_heights.append(value)
                avg_height = round((sum(team_heights) / len(team)), 2)
            if key == "guardians":
                team_guardians.append(value)
                guardians = sum(team_guardians, [])
    print("\nThere are {} players on this team:".format(len(team)))
    print("  ", ", ".join(player for player in team_players))
    print(f"\nThere are {exp} experienced players and {inexp} inexperienced players on this team.")
    print(f"\nThe average height is {avg_height} inches")
    print("\nThe players guardians are: ")
    print("  ", ", ".join(guardian for guardian in guardians))


def main_menu():
    while True:
        print()
        outline("MENU")
        print("Here are your choices:")
        print("  1) Display Team Stats")
        print("  2) Quit")
        print()
        main_choice = input("Please enter an option: ")
        try:
            main_choice = int(main_choice)
            if main_choice == 1 or main_choice == 2:
                print()
            else:
                raise ValueError()
        except ValueError:
            print("\nPlease enter 1 or 2. Try again.")
            continue
        if main_choice == 2:
            break
        elif main_choice == 1:
            display_teams()
            team_choice = input("\nSelect a team: ")
            try:
                team_choice = int(team_choice)
                if team_choice == 1 or team_choice == 2 or team_choice == 3:
                    print()
                else:
                    raise ValueError()
            except ValueError:
                print("\nPlease enter 1, 2, or 3. Try again.")
            if team_choice == 1:
                print(f"----{teams[0]} STATS----")
                team_stats(team1)
                print(f"\n----{teams[0]} STATS----")
            elif team_choice == 2:
                print(f"----{teams[1]} STATS----")
                team_stats(team2)
                print(f"\n----{teams[1]} STATS----")
            elif team_choice == 3:
                print(f"----{teams[2]} STATS----")
                team_stats(team3)
                print(f"\n----{teams[2]} STATS----")
    print("\n---HAVE A GREAT DAY!---")


if __name__ == "__main__":
    import_and_clean_data()
    exp_inexp()
    team1, team2, team3 = make_teams()
    print("BASKETBALL TEAM STATS TOOL")
    main_menu()
