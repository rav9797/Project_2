import constants

NUMBER_OF_PLAYERS = len(constants.PLAYERS)
teams = []
players = []
names = []
guardians = []
experience = []
heights = []

        
# Imports the player names and makes a list of them
def player_names(list_of_players):
    for i in range(NUMBER_OF_PLAYERS):
        names.append(constants.PLAYERS[i]["name"])
    return names


# Makes a list of the player's guardians split into lists instead of strings
def player_guardians(list_of_players):
    guardians_unsplit = []
    for i in range(NUMBER_OF_PLAYERS):
        guardians_unsplit.append(constants.PLAYERS[i]["guardians"])
    for string in guardians_unsplit:
        guardians.append(string.split(" and "))
    return guardians


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
    return experience


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
    return heights
    

# Makes the list players which is a list of dictionaries
def list_of_dicts(list1, list2, list3, list4):
    for i in range(NUMBER_OF_PLAYERS):
        player = {"name": list1[i],
                  "guardians": list2[i],
                  "experience": list3[i],
                  "height": list4[i],
                  }
        players.append(player)
    return players


def import_teams(list_of_teams):
    for i in constants.TEAMS:
        teams.append(i)
    return teams
        

def import_and_clean_data():
    import_teams(constants.TEAMS)
    player_names(constants.PLAYERS)
    player_guardians(constants.PLAYERS)
    player_experience(constants.PLAYERS)
    player_height(constants.PLAYERS)
    list_of_dicts(names, guardians, experience, heights)







if __name__ == "__main__":
    import_and_clean_data()
