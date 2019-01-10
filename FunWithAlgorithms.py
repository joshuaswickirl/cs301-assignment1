#
#   Fun with Algorithms!
#   CS301
#   Jan 8, 2019
#   Joshua Swick, Edgar Diaz, Matthew Jones
#
#

import time

#
#   Helper function for measuring and comparing runtime of algorithms
#
def compareRuntimes(list_of_args, list_of_functions):
    """
    Measures and compares approximate runtimes for each function in 
    list_of_functions when ran with the list_of_args argument.
    """
    numFunctions = len(list_of_functions)

    runTimes = []  # Init array for function durations
    if len(list_of_args) == 1:
        # Get runtimes and print results
        for _function in list_of_functions:
            time_start = time.time() # Init time
            output = _function(list_of_args[0])
            time_end = time.time()
            runtime = time_end - time_start
            runTimes.append(runtime)
            print(f"\n{_function.__name__}: {output}")
    elif len(list_of_args) == 2:
        # Get runtimes and print results
        for _function in list_of_functions:
            time_start = time.time() # Init time
            output = _function(list_of_args[0],list_of_args[1])
            time_end = time.time()
            runtime = time_end - time_start
            runTimes.append(runtime)
            print(f"\n{_function.__name__}: {output}")

    # Get slowest runtime
    slowestFunction = list_of_functions[0]
    slowestTime = runTimes[0]
    slowestFunctionIndex = 0
    for index in range(numFunctions):
        if slowestTime < runTimes[index]:
            slowestFunction = list_of_functions[index]
            slowestTime = runTimes[index]
            slowestFunctionIndex = index
        else:
            pass
    print(f"\n{slowestFunction.__name__} was the slowest algorithm at {slowestTime:.5f} seconds.")

    # Compare runtimes
    for index in range(numFunctions):
        if index == slowestFunctionIndex:
            pass
        else:
            runTime = runTimes[index]
            percentFaster = slowestTime / runTime
            functionName = list_of_functions[index]
            print(f"{functionName.__name__} is {percentFaster:.2f}% faster at {runTime:.5f} seconds.")

#
#   Assignment Questions
#

# 1. Sum of the 1st n positive integers
def sumOfN_Joshua(n):
    sum = 0
    while(n > 0):
        sum += n
        n -= 1
    return sum


def sumOfN_Edgar(n):
    sum = (n * (n +1))/2
    return sum


def sumOfN_Matt(n):
    count=0
    final=0
    while(count < (n+1)):
        final = (count+final)
        count = (count+1)
    return final


def sumOfN_Comparison(n=None):
    list_of_functions = [sumOfN_Joshua, sumOfN_Edgar, sumOfN_Matt]
    print("\nQuestion 1. What is the sum of the first n positive integers?")
    if n == None:
        while(True):
            n = input("\nEnter a positive integer: ")
            try:
                if int(n) < 0:
                    print("Integer is less than 0.")
                else:
                    n = int(n)
                    break
            except (ValueError):
                print("Value is not an integer.")
    compareRuntimes(list_of_args=[n], list_of_functions=list_of_functions)

#
#   Scrabble logic
#

# 2. Given word, check if it's a valid word
def validateWord_Joshua(word_input):
    with open("words.txt", 'r') as words_file:
        for word in words_file:
            if word_input.lower() == word.rstrip():
                return True
        return False # False if word not found


def validateWord_Edgar(word_input):
    pass


def validateWord_Matt(word_input):
    pass


def validateWord_Comparison(word=None):
    list_of_functions = [validateWord_Joshua]
    print("\nQuestion 2. Given a proposed word that someone wants to play, can you check that is a valid word?")
    if word == None:
        word = input("\nEnter a word: ")
    compareRuntimes(list_of_args=[word], list_of_functions=list_of_functions)


# 3. Given set of tiles and a word, check if word can be made
def makeWord_Joshua(char_set, word):
    word_length = len(word)
    word_as_list = list(word)
    word_index = 0
    for char in word_as_list:
        if char in char_set and word_index == word_length -1:
            #print(f"The word '{word}' can be made with {str(char_set)}.")
            return True
        elif char in char_set:
            word_index += 1
        else:
            #print(f"The word '{word}' can not be made with {str(char_set)}.")
            return False


def makeWord_Edgar(char_set, word):
    pass


def makeWord_Matt(char_set, word):
    pass

            
def makeWord_Comparison(char_set=None, word=None):
    list_of_functions = [makeWord_Joshua]
    print("\nQuestion 3. Given a set of tiles and a word, can you check if the word can be made from the tiles?")
    if char_set == None:
        if word == None:
            word = input("\nEnter a word: ")
        if char_set == None:
            char_set = set()  # Init set
            tiles = input("\nEnter a list of letters seperated by a comma. (ex. h,e,l,l,o): ")
            char_list = tiles.split(",")
            set_length = len(char_list)
            for i in range(set_length):
                char_set.add(char_list[i])
    compareRuntimes(list_of_args=[char_set, word], list_of_functions=list_of_functions)


# 4 Given set of tiles, find words that can be made
def findWords_Joshua(char_set):       
    confirmed_words = set()  # Empty set
    with open("words.txt", 'r') as words_file:
        for word in words_file:
            word = word.rstrip()
            word_length = len(word)
            word_as_list = list(word)
            word_index = 0
            for char in word_as_list:
                if char in char_set and word_index == word_length - 1:
                    confirmed_words.add(word)
                elif char in char_set:
                    word_index += 1
                else:
                    break
    #print(f"The following words can be made with {str(char_set)}.\n {str(confirmed_words)}")
    return confirmed_words


def findWords_Edgar(char_set):
    pass


def findWords_Matt(char_set):
    pass


def findWords_Comparison(char_set=None):
    list_of_functions = [findWords_Joshua]
    if char_set == None:
        char_set = set()  # Init set
        tiles = input("\nEnter a list of letters seperated by a comma. (ex. h,e,l,l,o): ")
        char_list = tiles.split(",")
        set_length = len(char_list)
        for i in range(set_length):
            char_set.add(char_list[i])
    compareRuntimes(list_of_args=[char_set], list_of_functions=list_of_functions)


# 5. Find all possible words for given puzzle



# 6. Sets of eight letters to form most possible bingos



if __name__ == "__main__":

    # # Run question 1
    # sumOfN_Comparison()

    # # Run question 2
    # validateWord_Comparison()

    # # Run question 3
    makeWord_Comparison()

    # Run question 4
    # char_set = {'h','e','l','o'}
    # findWords_Comparison(char_set)
