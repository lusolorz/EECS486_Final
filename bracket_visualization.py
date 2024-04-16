# import bracket 
import populate_dictionaries
import subprocess

# # Define the tournament structure
# team = [
#         "Team 1",
#         "Team 2",
#         "Team 3",
#         "Team 4",
#         "Team 5",
#         "Team 6",
#         "Team 7",
#         "Team 8"
#     ]
#     # "results": [
#     #     [1, 2],
#     #     [3, 4],
#     #     [5, 6],
#     #     [7, 8]
#     # ]

# # Define participants
# participants = [
#     "Player 1", "Player 2", "Player 3", "Player 4",
#     "Player 5", "Player 6", "Player 7", "Player 8"
# ]

# Create a single-elimination tournament with the participants
# team_east = populate_dictionaries.to_bracket_vis()['east']
# brack = bracket.Bracket(team_east)

# # print the bracket
# brack.show()

def generate_bracket(participants):
    bracket = []
    num_matches_per_round = len(participants) // 2

    # Generate initial bracket structure
    round_matches = []
    for _ in range(num_matches_per_round):
        round_matches.append([None, None])  # Each match is initially empty
    bracket.append(round_matches)

    # Seed participants into the first round of the bracket
    for i in range(len(participants)):
        bracket[0][i // 2][i % 2] = participants[i]

    return bracket


def print_bracket(bracket, winners):
    #counter for winners: 
    j = 0
    for i, round_matches in enumerate(bracket):
        print(f"Round {i + 1}:")
        for match in round_matches:
            player1 = match[0] if match[0] else 'TBD'
            player2 = match[1] if match[1] else 'TBD'
            winner = ""
            if player1 == winners[j]:
                winner = player1
            else:
                winner = player2
            j = j + 1
            max_length = max(len(player1), len(player2))
            print(f"    {player1:<{max_length}}\t──┐")
            print(f"    {' ':<{max_length}}\t  │-- " + winner) 
            print(f"    {player2:<{max_length}}\t──┘\n")
        print()

# Example usage:
populate_dictionaries.run()
team_east = populate_dictionaries.rounds
size = 16
default_value = 0
my_list = [default_value] * size
j = 15
my_list[0] = team_east[0][0]
my_list[1] = team_east[0][15]
my_list[2] = team_east[0][7]
my_list[3] = team_east[0][8]
my_list[4] = team_east[0][4]
my_list[5] = team_east[0][11]
my_list[6] = team_east[0][3]
my_list[7] = team_east[0][12]
my_list[8] = team_east[0][5]
my_list[9] = team_east[0][10]
my_list[10] = team_east[0][2]
my_list[11] = team_east[0][13]
my_list[12] = team_east[0][6]
my_list[13] = team_east[0][9]
my_list[14] = team_east[0][1]
my_list[15] = team_east[0][14]
# for i in range(0, len(team_east[0])):
#     my_list[i] = team_east[i]
bracket = generate_bracket(my_list)
winners = team_east[1]
print_bracket(bracket, winners)
bracket = generate_bracket(team_east[1])
print_bracket(bracket, winners)
