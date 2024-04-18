# EECS486_Final
To run the entire project enter the following command in terminal after navigating to the project
folder:

$ bash ./evaluation.sh

This command will run 50 iterations of the bracket maker and output a precision score as a percentage.
The precision score is an automated output for the accuracy of the final four of our generated bracket compared 
to the final 2024 March Madness bracket.

Precision = (# of correct members of final four predicted)/(number of total members in final four)

We do not calculate recall as total number of relevant members equals total number of members in the final four. (precision
and recall would be the same)

#FILES AND FUNCTION DESCRIPTIONS

-------------
fetch_html.py
-------------

fetch_and_save_html() - This function retrieves each of the raw HTML files for a given link and saves them into a passed-in file. This takes in the required header to simulate a browser request, the link we'd like to retrieve, and the file we'd like to have the HTML code in. This gives us a file with completed HTML code of a website.

crawl_websites() - This function runs the four instances of the fetch_and_save_html file and runs the four instances of the fetch_and_save_html function to retrieve all of the data. This doesn't have input arguments.

main() - This runs the crawl_websites() function and gives you a prompt to clarify when the links are being crawled.

---------------
resume_asc.html
---------------

Sorted in ascending order by seed values, this file provides a detailed summary of team performances over the season, including win-loss records and strength rankings such as the Strength of Record (SOR) and Strength of Schedule (SOS). It's vital for bracket predictions, offering insights into each team's capabilities and historical performance.

---------------
resume_desc.html
---------------

This file offers a descending order dataset of the same performance metrics found in 'resume_asc.html'. It ensures no crucial data is missed during the scraping process, capturing complete information for all teams, particularly those hidden in dynamically-loaded content areas of the website.

--------------------
tournament_asc.html
--------------------

This file contains tournament-related data sorted in ascending order by seed values. It includes team progression probabilities through various tournament stages, region assignments, and seed numbers. The data is essential for generating keys in dictionaries that handle region-specific details and probabilities necessary for in-depth bracket analysis.

--------------------
tournament_desc.html
--------------------

Complementary to the 'tournament_asc.html', this file presents the same tournament data sorted in descending order. It ensures thorough data capture, especially useful for sections of the webpage that might not load all content in one view, such as data behind dynamic 'Show More' buttons.

-------------
evaluation.sh
-------------

Includes bash script to run the population and evaluation of our data. THIS DOES NOT INCLUDE THE SCRAPING FOR OUR DATA. We initally scraped once and
saved the HTML files to our project. If you wish to re-scrape you will have to run fetch_html before running the bash script. 

Run the following command in your terminal to execute bash script:

$ bash ./evaluation.sh

------------------------
populate_dictionaries.py
------------------------

Functions:

percent_to_bool() - This function converts a string percentage into a boolean. It strips the percent symbol from the string, converts it to a float, and returns True if the percentage is greater than 0, otherwise False. This function is mainly used to handle boolean logic based on percentage values in your dataset. It takes in a string and gives a bool back.

populate_tournament() - This function reads an HTML file, parses its content using BeautifulSoup, and extracts tournament team names and their corresponding details (like seed, region, and probabilities for reaching certain tournament stages). It returns a dictionary where team names are keys and their details are values. This function helps build the primary dataset from tournament information.

populate_resume() - Similar to populate_tournament(), this function processes another HTML file to gather team performance statistics like wins, losses, win percentage, and strength of schedule ranking. It returns a dictionary with team names as keys and detailed statistics as values, enriching the dataset with performance metrics.

remove_repeats() - This function merges two dictionaries by adding entries from the second dictionary to the first only if the keys do not already exist in the first. It is used to ensure there are no duplicate teams in your data while combining data from ascending and descending lists. It takes in two dictionaries and returns one back, with all of the keys added. 

combine_dictionaries() - This function combines two dictionaries by updating the values of the first dictionary with values from the second dictionary for matching keys. This is crucial for merging different sets of data about the same teams. It takes in two dictionaries and returns one back with all of the extra values.

delete_keys_from_dict() - This function removes specific entries from a dictionary based on a list of keys to remove. It's used to eliminate teams that are not part of the simulation or analysis, helping to focus on the relevant subset of data. It takes in a dictionary that we'd like to delete keys from and list of keys to be deleted and returns back the dictionary with the specified keys deleted.

split_by_region() - This function divides a dictionary into four separate dictionaries based on team regions (East, West, South, Midwest). Each team's region is determined from their details in the combined dictionary, facilitating regional analyses and simulations within the tournament structure. This takes in one large combined dictionary and returns four smaller dictionaries based on region.

analyze() - This function takes in a dictonary for a specific region and outputs nothing. This function adds the key "Score" to each team in the dictonary that is passed in. Score slightly alters the win% using SOS RK.

tiebreaker() - This function helps settle ties in scores. If two teams have scores that are within a threshold, this function helps prioritize a function based on their seeding value. (the lower the seed, the higher the priority for that team) 

seed_name() - This function takes in a dictonary where the key is the name of a team and the value is a list of stats for a specific region and outputs a dictonary where the key is the seed number and the value is the name of the team.

first_round() - This function takes in two dictonaries for a specific region. This function outputs a list of team names that won their games for the first round in this region(16 teams, 8 games). 

later_rounds() - This function takes in a dictonary for a specific region, the list of winners from the pervious round, and the number of games in this round. This function outputs a list of winners for this round in a particular region.

diff_regions() - This function takes in a team name and the dictonary for that region and another team name and the dictonary for that region. This function handles games when the teams are in different regions during the Final Four and Champsion games. This function ouputs the team name of the winner and the dictionary of the region they are in.

run() - This function calls all functions required to fill a list with all relevant information (initial 16 for each region and winners for each matchup) 
separated by region and tournament life cycle. 


-------------------------
 bracket_visualization.py
-------------------------

Functions:
generate_braket() - implements custom bracket data structure. Takes in a list of teams for the current round as an argument and 
returns a bracket data structure

print_bracket() - prints bracket data structure. Takes in a bracket data structure and a list of winning teams for respective round
and writes round bracket to brackets.txt file

first_round() - prints and generates bracket for the first round of the tournament. Called for each region once. Takes in all required 
arguments for generate_bracket() and print_bracket(). Takes in a sorted list of teams based on seeds ASC and arranges matches based on seeds.

-------------
 brackets.txt 
-------------

Contains the 50th bracket generated after running bash script. Brackets are organized by region by round with a final four and final matchup. 

------------------
 brackets_eval.txt 
------------------

Contains precision scores for each individual bracket for the 50 brackets generated with the bash script. 

--------------
 final_eval.py 
--------------

Reads in precision scores from brackets_eval.txt and outputs a final precision score averaged over 50 brackets when run with bash script 

--------------
 BracketsScoring.ods
--------------

This file is meant to have all of the actual data analysis within excel format for the scoring.

Pages:

Raw Scoring (Human & Expert) - This has all of the raw scoring metrics for the 10 Human brackets and the 3 Expert brackets

Raw Scoring (BracketGenius) - This has all of the raw scoring metrics for the 10 Generated Brackets

Human Data Evals - This has the precision and the statistical data evaluations for the Human scored brackets.

Combined Data - This is page for the average precisions per round for all of the three scored data sources, to help compare their efficacies.

Bracket Data Evals -  This has the precision and the statistical data evaluations for the Generated scored brackets.

Expert Data Evals -  This has the precision and the statistical data evaluations for the Expert scored brackets.
