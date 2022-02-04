"""
???

Author: John Q
Date: 26 August 2020
"""


import datetime
import json
import os.path
import sys

# Start the clock
start_time = datetime.datetime.now(); print(str(start_time) + '\n')

# Load the word list from the json file into a Python dictionary
with open('words_dictionary.json', 'r') as json_file:
    word_dict = json.load(json_file)

# Initialize the starting letter
starting_letter = 'a'
# Set the output file name based on the starting letter
outfile = starting_letter + '.json'
# Initialize the new word dictionary
new_word_dict = {}
# Print status
print('Now processing: ' + starting_letter)

for word in word_dict:
    # Check if the starting letter has changed
    if word[0] != starting_letter:
        # Write the new word list dictionary to a json file
        with open(outfile, 'w') as f:
            json.dump(new_word_dict, f)
        # Update the starting letter
        starting_letter = word[0]
        # Update the output file name
        outfile = starting_letter + '.json'
        # Re-initialize the new word dictionary
        new_word_dict = {}
        # Print status
        print('Now processing: ' + starting_letter)

    # Check if the word begins with the starting letter
    # and is more than 4 characters long
    if word[0] == starting_letter and len(word) >= 4:
        # Add the word to the new word dictionary
        new_word_dict[word] = 1
        #print(word + ' -> ' + outfile)
    else:
        pass # The word is invalid



# Stop the clock
stop_time = datetime.datetime.now(); print('\n' + str(stop_time))
run_time = stop_time - start_time
print(str(run_time) + '\n')
