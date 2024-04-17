# Open the file in read mode ('r')
with open('brackets_eval.txt', 'r') as f:
    # Read each line of the file
    total = 0
    count = 0
    for line in f:
        count = count+1
        # Process each line (e.g., print it)
        curr = float(line.strip())  # Strip trailing newline character
        total += curr
    
print("Precision for Final four: " + str((total/count)*100) + "%")
        