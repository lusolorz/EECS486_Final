# import bracket 
import populate_dictionaries

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


def print_bracket(bracket, team_east):
    for i, round_matches in enumerate(bracket):
        print(f"Round {i + 1}:")
        for match in round_matches:
            player1 = match[0] if match[0] else 'TBD'
            player2 = match[1] if match[1] else 'TBD'
            winner = ""
            if team_east[player1] > team_east[player2]:
                winner = player1
            else:
                winner = player2
            max_length = max(len(player1), len(player2))
            print(f"    {player1:<{max_length}}\t──┐")
            print(f"    {' ':<{max_length}}\t  │-- " + winner) 
            print(f"    {player2:<{max_length}}\t──┘\n")
        print()

# Example usage:
team_east = populate_dictionaries.to_bracket_vis()['east']
temp = list(populate_dictionaries.to_bracket_vis()['east'].keys())
bracket = generate_bracket(list(populate_dictionaries.to_bracket_vis()['east'].keys()))
print_bracket(bracket, team_east)
for i in range (0,2):
    new_teams = []
    for item in bracket:
        for item2 in item:
            if team_east[item2[0]] < team_east[item2[1]]:
                new_teams.append(item2[1])
            else:
                new_teams.append(item2[0])
    print("Here")
    print_bracket(bracket, team_east)
    bracket = generate_bracket(new_teams)
    print_bracket(bracket, team_east)
