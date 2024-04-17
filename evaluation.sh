#!/bin/bash

rm brackets_eval.txt

for n in {1..50};
do
    python3 bracket_visualization.py tournament_asc.html tournament_desc.html resume_asc.html resume_desc.html
done

python3 final_eval.py