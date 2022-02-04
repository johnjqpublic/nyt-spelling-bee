"""
Convert the word list text file generated from
    cat /usr/share/dict/words > words.txt
to a JSON file

Author: John Q
Date: 26 August 2020
"""


import datetime
import json


# Start the clock
start_time = datetime.datetime.now(); print(str(start_time) + '\n')

word_dict = {}

# Open the word list text file and load it into a Python dictionary
with open('words.txt', 'r') as txt_file:
    for line in txt_file:
        word_dict[line.strip()] = 1

# Write the word list dictionary to a json file
with open('words.json', 'w') as json_file:
    json.dump(word_dict, json_file)

# Stop the clock
stop_time = datetime.datetime.now(); print('\n' + str(stop_time))
run_time = stop_time - start_time
print(str(run_time) + '\n')
