from sys import argv
import string
from operator import itemgetter

def main():
    # assigning arguments
    script, filename = argv

    # opening, reading and closing the file
    txt = open(filename)
    file_read = txt.read()
    txt.close()

    # normalizing the text file
    # converting all letters to lowercase
    # splitting the file into a list based on whitespace
    word_list = string.replace(file_read, "--", " ").lower().split()

    # creating an empty dictionary
    word_dict = {}

    # iterating through the list of words in the input file
    for word in word_list:

        word = word.strip(string.punctuation)

        # if the word is not found in the dictionary
        # insert the word and initialize the value to 1
        if word_dict.get(word) == None:
            word_dict[word] = 1
        else:
            # increment the value by 1
            word_dict[word] += 1

    # made dict --> list of tuples
    # sort tuples by words first, and then by frequency in desc

    word_tuples = word_dict.items()
    sorted_word = sorted(word_tuples, key=itemgetter(0))
    sorted_freq = sorted(sorted_word, key=itemgetter(1), reverse=True)

    # print highest to lowest frequency, in alphabetical order
    for key, value in sorted_freq:
        print key, value

           
main()