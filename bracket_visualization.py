# import bracket 
import populate_dictionaries
import subprocess

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


#def print_bracket(bracket, winners_one, winners_two, winners_three):
def print_bracket(bracket, winners, f):
    #counter for winners: 
    j = 0
    max_length = 0
    #find max length of all team names for formatting 
    for i, round_matches in enumerate(bracket):
        for match in round_matches:
            player1 = match[0] if match[0] else 'TBD'
            player2 = match[1] if match[1] else 'TBD'
            if max(len(player1), len(player2)) > max_length:
                    max_length = max(len(player1), len(player2))
    #output rounds 
    for i, round_matches in enumerate(bracket):
        for match in round_matches:
            #players for game in round
            player1 = match[0] if match[0] else 'TBD'
            player2 = match[1] if match[1] else 'TBD'
            winner = ""
            if player1 == winners[j]:
                winner = player1
            else:
                winner = player2
            j = j + 1
            
            f.write(f"    {player1:<{max_length}} ──┐\n")
            f.write(f"    {' ':<{max_length}}   │-- " + winner + "\n") 
            f.write(f"    {player2:<{max_length}} ──┘\n\n")
        f.write("\n")

def first_rounds(teams, winners, f):
    size = 16
    default_value = 0
    my_list = [default_value] * size
    
    #arrange first round based on seeds 
    my_list[0] = teams[0]
    my_list[1] = teams[15]
    my_list[2] = teams[7]
    my_list[3] = teams[8]
    my_list[4] = teams[4]
    my_list[5] = teams[11]
    my_list[6] = teams[3]
    my_list[7] = teams[12]
    my_list[8] = teams[5]
    my_list[9] = teams[10]
    my_list[10] = teams[2]
    my_list[11] = teams[13]
    my_list[12] = teams[6]
    my_list[13] = teams[9]
    my_list[14] = teams[1]
    my_list[15] = teams[14]
    
    bracket = generate_bracket(my_list)
    print_bracket(bracket, winners, f)

with open('brackets.txt', 'w') as f:
    # Example usage:
    temp = populate_dictionaries.run()
    regions = ["East", "West", "South", "Midwest", "Nothing"]
    #run brackets 
    for i in range(0,4):
        f.write("\nRegion "+ regions[i] + ":\n\n")
        teams = temp[0][i]
        teams_win = temp[i+1][0]
        f.write("Round: 1 \n\n")
        first_rounds(teams, teams_win, f)
        for j in range (0,3):
            f.write("Round: "+str(j+2)+"\n")
            teams = temp[i+1][j]
            teams_R = temp[i+1][j+1]
            brack = generate_bracket(teams)
            print_bracket(brack, teams_R, f)
    
    f.write("Final Four: \n")
    teams = []
    teams.append(temp[3][3][0])
    teams.append(temp[4][3][0])
    teams.append(temp[1][3][0])
    teams.append(temp[2][3][0])
    brack = generate_bracket(teams)
    winners = []
    winners.append(temp[5][0])
    winners.append(temp[5][1])
    print_bracket(brack, winners,f)
    f.write("Final: \n")
    teams = winners
    winners = []
    winners.append(temp[6])
    brack = generate_bracket(teams)
    print_bracket(brack, winners, f)

with open('brackets_eval.txt', 'a') as f2:
    final_four_real = ["UConn Huskies", "Purdue Boilermakers", "Alabama Crimson Tide", "NC State Wolfpack"]
    winner_real = "UConn Huskies"
    final_four = []
    final_four.append(temp[3][3][0])
    final_four.append(temp[4][3][0])
    final_four.append(temp[1][3][0])
    final_four.append(temp[2][3][0])
    winner = temp[6]
    correct = 0
    for item in final_four:
        if item in final_four_real:
            correct = correct + 1
    
    f2.write(str(correct/4) + "\n")



