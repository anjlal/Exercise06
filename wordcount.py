from sys import argv
import string

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

    #iterating through the list of words in the input file
    for word in word_list:

        word = word.strip(string.punctuation)

        #if the word is not found in the dictionary
        #insert the word and initialize the value to 1
        if word_dict.get(word) == None:
            word_dict[word] = 1
        else:
            # increment the value by 1
            word_dict[word] += 1

    sorted_dict = {}

    #iterating through the word dictionary and
    #and grouping the words by frequencies
    for key, value in word_dict.iteritems():
        if sorted_dict.get(value) == None:
            sorted_dict[value] = [key]
        else:
            sorted_dict[value].append(key)

    #sorting by highest to lowest frequency
    for i in reversed(sorted(sorted_dict.keys())):
        #sorting the same frequency alphabetically
        for word in sorted(sorted_dict[i]):
            print word, i
            
main()