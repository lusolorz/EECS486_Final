import sys
from bs4 import BeautifulSoup
import requests

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

# Main!
if __name__ == '__main__':

    # How to run the code
    if len(sys.argv) != 5:
        print("Usage: python3 populate_dictionaries.py tournament_asc_html tournament_desc_html resume_asc_html resume_desc_html")
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

    print("\n\nhere it comes\n\n")

    # Combined dictonary portion, along with its respective print command
    combined = combine_dictionaries(tournament, resume)
    print("SIZE: " + str(len(combined.keys())))
    # for team, details in combined.items():
    #     print(f"{team}: {details}")

    # Region-wise dictonary portion, along with its respective print command
    east, west, south, midwest = split_by_region(combined)

    # Sanity check print statements for the regions
    print("\n\neast\n\n")
    for team, details in east.items():
        print(f"{team}: {details}")
    
    print("\n\nwest\n\n")
    for team, details in west.items():
        print(f"{team}: {details}")

    print("\n\nsouth\n\n")   
    for team, details in south.items():
        print(f"{team}: {details}")

    print("\n\nmidwest\n\n") 
    for team, details in midwest.items():
        print(f"{team}: {details}")

