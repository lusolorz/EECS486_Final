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



---------------
resume_desc.html
---------------



--------------------
tournament_asc.html
--------------------



--------------------
tournament_desc.html
--------------------



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

percent_to_bool() - 

populate_tournament() - 

Populate_resume() - 

remove_repeats() -

combine_dictionaries() - 

delete_keys_from_dict() - 

split_by_region() - 

analyze() - 

tiebreaker() - This function helps settle ties in scores. If two teams have scores that are within a threshold, this function helps prioritize a function based on their seeding value. (the lower the seed, the higher the priority for that team) 

seed_name() - 

first_round() - 

later_rounds() - 

diff_regions() - 

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





