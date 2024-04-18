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

---------------------------
| bracket_visualization.py|
---------------------------

Functions:
generate_braket() - implements custom bracket data structure. Takes in a list of teams for the current round as an argument and 
returns a bracket data structure

print_bracket() - prints bracket data structure. Takes in a bracket data structure and a list of winning teams for respective round
and writes round bracket to brackets.txt file

first_round() - prints and generates bracket for the first round of the tournament. Called for each region once. Takes in all required 
arguments for generate_bracket() and print_bracket(). Takes in a sorted list of teams based on seeds ASC and arranges matches based on seeds.

----------------
| brackets.txt |
----------------

Contains the 50th bracket generated after running bash script. Brackets are organized by region by round with a final four and final matchup. 

---------------------
| brackets_eval.txt |
---------------------

Contains precision scores for each individual bracket for the 50 brackets generated with the bash script. 

-----------------
| final_eval.py |
-----------------

Reads in precision scores from brackets_eval.txt and outputs a final precision score averaged over 50 brackets when run with bash script 





