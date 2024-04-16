import sys
from bs4 import BeautifulSoup
import requests
import random

# This is just a helper function so I could debug the percentage values
def percent_to_bool(s):
    # Remove the percent sign and convert to float
    try:
        percentage = float(s.strip('%'))
        return percentage > 0
    except ValueError:
        return False

# This populates the tournament website's dictionary
def populate_tournament(html_file_path):
    html_content = None
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Intermediary variables for the tbody portions
    # tbody = soup.find_all('tbody', class_='Table__TBODY')
    first_tbody = soup.find_all('tbody', class_='Table__TBODY')[0]
    second_tbody = soup.find_all('tbody', class_='Table__TBODY')[1]

    # Get the team names from the first tbody
    team_names = [row.find('span', class_='TeamLink__Name').get_text().strip() for row in first_tbody.find_all('tr', attrs={'data-idx': True})]
    team_details_list = []

    # Get the team details from the second tbody
    for row in second_tbody.find_all('tr'):
        cells = row.find_all('td')
        try:
            # Parsing the seed value as a float and converting to int
            seed = int(float(cells[0].get_text().strip()))
            region = cells[1].get_text().strip()[0]
            final_four = percent_to_bool(cells[3].get_text().strip())
            elite_eight = percent_to_bool(cells[4].get_text().strip())
            sweet_sixteen = percent_to_bool(cells[5].get_text().strip())

            team_details_list.append({
                'Region': region,
                'Seed': seed,
                'Final_4': final_four,
                'Elite_8': elite_eight,
                'Sweet_16': sweet_sixteen
            })
        except ValueError as e:
            print(f"An error occurred while processing row: {row}")
            print(f"Error: {e}")

    # Combine team names with their details based on order
    full_team_data = {name: details for name, details in zip(team_names, team_details_list)}

    return full_team_data

# This populates the resume wesbite's dictionary
def populate_resume(html_file_path):
    html_content = None
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Get the team names from the first tbody
    first_tbody = soup.find_all('tbody', class_='Table__TBODY')[0]
    team_names = [row.find('span', class_='TeamLink__Name').get_text().strip()
                  for row in first_tbody.find_all('tr', attrs={'data-idx': True})]

    # Get the team details from the second tbody
    second_tbody = soup.find_all('tbody', class_='Table__TBODY')[1]
    team_details_list = []

    for row in second_tbody.find_all('tr'):
        cells = row.find_all('td')
        w_l_record = cells[0].get_text().strip().split('-')
        sos_rk = int(cells[5].get_text().strip())

        if len(w_l_record) == 2:
            wins, losses = map(int, w_l_record)
            win_percentage = round(float(wins/(wins + losses)), 2)
            team_details_list.append({
                'Wins': wins,
                'Losses': losses,
                'Win_%': win_percentage,
                'SOS_RK': sos_rk
            })
        else:
            print(f"Unexpected W-L format for row: {row}")

    # Combine team names with their details
    full_team_data = {name: details for name, details in zip(team_names, team_details_list)}

    return full_team_data


# adds teams in dict2 to dict1
def remove_repeats(dict1, dict2):
    for key in dict2:
        if key not in dict1:
            dict1[key] = dict2[key]
    return dict1


# This combines the tournament and the resume website's dictionary into the combined intermediary dictonary, 
def combine_dictionaries(dict1, dict2):
    for key in dict1:
        if key in dict2:
            dict1[key].update(dict2[key])
    return dict1


# This just separates and gives us all of the dictonaries of our dreams (the four regions)
def split_by_region(combined_data):
    east_dict = {}
    west_dict = {}
    south_dict = {}
    midwest_dict = {}

    # The function assumes that 'Region' values are a single character representing the region
    for team, details in combined_data.items():
        region = details.get('Region', '').upper()
        if region == 'E':
            east_dict[team] = details
        elif region == 'W':
            west_dict[team] = details
        elif region == 'S':
            south_dict[team] = details
        elif region == 'M':
            midwest_dict[team] = details
        else:
            print(f"Team {team} has an unexpected region value: {region}")

    return east_dict, west_dict, south_dict, midwest_dict


# analysis
def analyze(region):
    scale = 0.05
    for team in region:
        sos_per = region[team]["SOS_RK"]/100
        score = round(region[team]["Win_%"] - (scale * sos_per), 2)
        region[team]["Score"] = score

# tiebreaker for similar scores 
def tiebreaker(region, teamName1, teamName2):
    # !CHANGE RANGE DEPENDING ON SCORE
    if abs(region[teamName1]["Score"] - region[teamName2]["Score"]) < 0.01:
        if int(region[teamName1]["Seed"]) > int(region[teamName2]["Seed"]):
            return teamName2
        else:
            return teamName1

# creates a dictonary key: seed, value: team name
def seed_name(region):
    seeds = {}
    for key in region:
        seeds[region[key]["Seed"]] = key
    return seeds


def first_round(region, seeds):
    winners = []
    # random
    per_1_16 = 0.987
    rand_one = random.randint(0,100)/100
    if rand_one <= per_1_16:
        winners.append(seeds[1])
    else:
        winners.append(seeds[16])
    # 9 normally beats 8
    per_8_9 = 0.487
    biased_8 = region[seeds[8]]["Score"] * per_8_9
    biased_9 = region[seeds[9]]["Score"] * (1 - per_8_9)
    if biased_9 >= biased_8:
        winners.append(seeds[9])
    else:
        winners.append(seeds[8])
    per_5_12 = 0.651
    biased_5 = region[seeds[5]]["Score"] * per_5_12
    biased_12 = region[seeds[12]]["Score"] * (1-per_5_12)
    if biased_5 >= biased_12:
        winners.append(seeds[5])
    else:
        winners.append(seeds[12])
    per_4_13 = 0.789
    rand_four = random.randint(0,100)/100
    if rand_four <= per_4_13:
        winners.append(seeds[4])
    else:
        winners.append(seeds[13])
    per_6_11 = 0.618
    biased_6 = region[seeds[6]]["Score"] * per_6_11
    biased_11 = region[seeds[11]]["Score"] * (1 - per_6_11)
    if biased_6 >= biased_11:
        winners.append(seeds[6])
    else:
        winners.append(seeds[11])
    per_3_14 = 0.855
    rand_three = random.randint(0,100)/100
    if rand_three <= per_3_14:
        winners.append(seeds[3])
    else:
        winners.append(seeds[14])
    per_7_10 = 0.609
    biased_7 = region[seeds[7]]["Score"] * per_7_10
    biased_10 = region[seeds[10]]["Score"] * (1 - per_7_10)
    if biased_7 >= biased_10:
        winners.append(seeds[7])
    else:
        winners.append(seeds[10])
    per_2_15 = 0.928
    rand_two = random.randint(0,100)/100
    if rand_two <= per_2_15:
        winners.append(seeds[2])
    else:
        winners.append(seeds[15])
    return winners

def later_rounds(region, teams, num):
    winners = []
    count = 0
    randomness = 87
    while count < num:
        rand = random.randint(0,100)
        team_one = teams[count]
        team_two = teams[count+1]
        score_one = region[team_one]["Score"]
        score_two = region[team_two]["Score"]
        if rand <= randomness:
            if score_one > score_two:
                winners.append(team_one)
            elif score_two > score_one:
                winners.append(team_two)
            else:
                winners.append(tiebreaker(region, team_one, team_two))
        else:
            if score_one > score_two:
                winners.append(team_two)
            elif score_two > score_one:
                winners.append(team_one)
            else:
                winners.append(tiebreaker(region, team_one, team_two))
        count += 2
    return winners


def diff_regions(team_one, region_one, team_two, region_two):
    randomness = 90
    rand = random.randint(0,100)
    score_one = region_one[team_one]["Score"]
    score_two = region_two[team_two]["Score"]
    if rand <= randomness:
        if score_one >= score_two:
            return team_one, region_one
        elif score_two > score_one:
            return team_two, region_two
        else:
            if region_one[team_one]["Seed"] > region_two[team_two]["Seed"]:
                return team_one, region_one
            else:
                return team_two, region_two
    else:
        if score_one > score_two:
            return team_two, region_two
        elif score_two > score_one:
            return team_one, region_one
        else:
            if region_one[team_one]["Seed"] > region_two[team_two]["Seed"]:
                return team_one, region_one
            else:
                return team_two, region_two

# Main!
if __name__ == '__main__':

    # How to run the code
    if len(sys.argv) != 5:
        print("Usage: python3 populate_dictionaries.py tournament_asc.html tournament_desc.html resume_asc.html resume_desc.html")
        sys.exit(1)

    # Systems arguments from command line, to pass in the required html portions
    tournament_asc_html = sys.argv[1]
    tournament_desc_html = sys.argv[2]
    resume_asc_html = sys.argv[3]
    resume_desc_html = sys.argv[4]

    # Tournament dictonary portion, along with its respective print command
    tournament_asc = populate_tournament(tournament_asc_html)
    tournament_desc = populate_tournament(tournament_desc_html)
    tournament = remove_repeats(tournament_asc, tournament_desc)
    # for team, details in tournament.items():
    #     print(f"{team}: {details}")
    # new function for descending teams on tournament page

    # Resume dictonary portion, along with its respective print command
    resume_asc = populate_resume(resume_asc_html)
    resume_desc = populate_resume(resume_desc_html)
    resume = remove_repeats(resume_asc, resume_desc)
    # for team, details in resume.items():
    #     print(f"{team}: {details}")

    # print("\n\nhere it comes\n\n")

    # Combined dictonary portion, along with its respective print command
    combined = combine_dictionaries(tournament, resume)
    # print("SIZE: " + str(len(combined.keys())))
    # for team, details in combined.items():
    #     print(f"{team}: {details}")

    # Region-wise dictonary portion, along with its respective print command
    east, west, south, midwest = split_by_region(combined)
    analyze(east)
    analyze(west)
    analyze(south)
    analyze(midwest)
    east_seeds = seed_name(east)
    west_seeds = seed_name(west)
    south_seeds = seed_name(south)
    mid_seeds = seed_name(midwest)

    # EAST REGION
    east_first = first_round(east, east_seeds)
    east_second = later_rounds(east, east_first, 8)
    east_third = later_rounds(east, east_second, 4)
    east_winner = later_rounds(east, east_third, 2)

    # WEST REGION
    west_first = first_round(west, west_seeds)
    west_second = later_rounds(west, west_first, 8)
    west_third = later_rounds(west, west_second, 4)
    west_winner = later_rounds(west, west_third, 2)

    # SOUTH REGION
    south_first = first_round(south, south_seeds)
    south_second = later_rounds(south, south_first, 8)
    south_third = later_rounds(south, south_second, 4)
    south_winner = later_rounds(south, south_third, 2)

    # MIDWEST REGION
    mid_first = first_round(midwest, mid_seeds)
    mid_second = later_rounds(midwest, mid_first, 8)
    mid_third = later_rounds(midwest, mid_second, 4)
    mid_winner = later_rounds(midwest, mid_third, 2)

    # ALL REGIONS (FINAL FOUR ONWARD)
    south_mid, region_one = diff_regions(south_winner, south, mid_winner, midwest)
    east_west, region_two = diff_regions(east_winner, east, west_winner, west)
    champ, region = diff_regions(south_mid, region_one, east_west, region_two)

    # Sanity check print statements for the regions
    # print("\n\neast\n\n")
    # for team, details in east.items():
    #     print(f"{team}: {details}")
    
    # print("\n\nwest\n\n")
    # for team, details in west.items():
    #     print(f"{team}: {details}")

    # print("\n\nsouth\n\n")   
    # for team, details in south.items():
    #     print(f"{team}: {details}")

    # print("\n\nmidwest\n\n") 
    # for team, details in midwest.items():
    #     print(f"{team}: {details}")