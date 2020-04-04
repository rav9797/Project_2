import constants

number_of_players = len(constants.PLAYERS)
names = []
guardians = []
experience = []
height = []

        
def player_names(list_of_players):
    for i in range(number_of_players):
        names.append(constants.PLAYERS[i]["name"])
    return names


def player_guardians(list_of_players):
    for i in range(number_of_players):
        guardians.append(constants.PLAYERS[i]["guardians"])
    return guardians


def player_experience(list_of_players):
    exp = []
    for i in range(number_of_players):
        exp.append(constants.PLAYERS[i]["experience"])
    for j in exp:
        if j == "YES":
            experience.append(True)
        else:
            experience.append(False)
    return experience


def player_height(list_of_players):
    









if __name__ == "__main__":
    player_names(constants.PLAYERS)
    player_guardians(constants.PLAYERS)
    player_experience(constants.PLAYERS)
    player_height(constants.PLAYERS)
