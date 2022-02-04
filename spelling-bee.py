"""
Solves the New York Times Spelling Bee game.

How to Play:
    Create words using letters from the hive.
        - Words must contain at least 4 letters.
        - Words must include the center letter.
        - Our word list does not include words that are obscure, hyphenated, or proper nouns.
        - No cussing either, sorry.
        - Letters can be used more than once.
    Score points to increase your rating.
        - 4-letter words are worth 1 point each.
        - Longer words earn 1 point per letter.
        - Each puzzle includes at least one “pangram” which uses every letter. These are worth 7 extra points!

Author: John Q
Date: 26 August 2020
"""


import datetime
import json
import pprint


#dictionary_filename = 'words_dictionary.json'
dictionary_filename = 'words.json'


def get_invalid_letters(req_letter, rem_letters, debug=False):
    """ Generates a list of invalid letters based on the required letter and the remaining six valid letters """
    # Initialize a list of all the letters in the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Create a list of all the valid letters by combining the required letter and remaining letters
    val_letters = list(req_letter) + rem_letters
    if debug: print('Valid letters are: ' + str(val_letters))
    # Initialize a list for the invalid letters
    inv_letters = []
    # Iterate over the alphabet
    for letter in alphabet:
        if letter not in val_letters:
            # Letter is invalid
            inv_letters.append(letter)

    # Return the list of invalid letters
    if debug:
        print('Invalid letters are: ')
        print(inv_letters)
        print('')
    return inv_letters


def is_valid(word, req_letter, inv_letters, req_length, debug=False):
    """ Determines whether a word is a valid answer """
    contains_req_letter = False
    # Check that the length of the word is greater-than/equal to the requirement
    if len(word) >= req_length:
        # Check if the word is capitalized (i.e., is a proper noun)
        if word[0].isupper():
            return False    # Word is invalid => return False
        # Iterate over the letters in the word and check if any of them are invalid
        for i in range(0, len(word)):
            for inv_letter in inv_letters:
                if word[i] == inv_letter:
                    return False    # Word is invalid => return False
            # Check if the letter is the required letter
            if word[i] == req_letter:
                contains_req_letter = True
        # If the word hasn't been discarded yet, this means that it only includes valid letters
        # and may or may not include the required letter
        # Therefore, check if the word includes the required letter
        if contains_req_letter:
            return True    # Word is valid => return True
        else:
            return False    # Word is invalid => return False


def calc_score(word, req_letter, rem_letters, debug=False):
    """ Calculates the score of a word """
    # Initialize score to zero
    score = 0

    # 4-letter words are worth 1 point each
    # Longer words earn 1 point per letter
    if len(word) == 4:
        score = 1
    elif len(word) > 4:
        score = len(word)

    # Iterate over the letters in the word and check if the word contains every valid letter
    # (i.e., is a "pangram")
    val_letters = list(req_letter) + rem_letters
    for i in range(0, len(word)):
        if word[i] in val_letters:
            val_letters.remove(word[i])
    if len(val_letters) == 0:
        # Add seven points for being a pangram
        score += 7

    # Return the score
    return score


if __name__ == "__main__":
    # Set debug
    debug = False

    # Get user input
    req_letter = input('Please enter the required letter: ')
    if debug: print(req_letter)
    rem_letters = list(input('Please enter the remaining six letters: '))
    if debug: print(rem_letters)
    print('')

    # Start the clock
    start_time = datetime.datetime.now(); print(str(start_time) + '\n')

    # Invalid letters cannot be part of the answer words
    inv_letters = get_invalid_letters(req_letter, rem_letters, debug)

    # Load the word list from the json file into a Python dictionary
    with open(dictionary_filename, 'r') as json_file:
        word_dict = json.load(json_file)

    # Initialize the dictionary of answers
    # This dictionary will include the word's score
    # as well as whether it is a pangram
    answers = {}

    # Iterate over the word list dictionary
    for word in word_dict:
        # Determine whether the word is a valid answer
        if is_valid(word, req_letter, inv_letters, 4, False):
            # Calculate the word's score
            score = calc_score(word, req_letter, rem_letters, False)
            # Use the score to determine if the word is a pangram
            # and store the word in the answers dictionary as appropriate
            if score == len(word)+7:
                answers[word] = {'score': score, 'pangram': '*'}
            else:
                answers[word] = {'score': score, 'pangram': ''}
        else:
            pass    # The word is not a valid answer

    # Print the answers
    print(str(len(answers)) + ' possible answers found')
    print('-'*(len(str(len(answers)))+23))
    #pprint.pprint(answers)
    for answer in answers:
        s = answers[answer]['score']
        p = answers[answer]['pangram']
        print(f'{answer:19} {s:2d} {p:1}')

    # Stop the clock
    stop_time = datetime.datetime.now(); print('\n' + str(stop_time))
    run_time = stop_time - start_time
    print(str(run_time) + '\n')
