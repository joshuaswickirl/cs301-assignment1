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
    if list_of_args == None:
        for _function in list_of_functions:
            try:
                time_start = time.time() # Init time
                output = _function()
                time_end = time.time()
                runtime = time_end - time_start
                if runtime < 0.000001:
                    runTimes.append(None)
                else:
                    runTimes.append(runtime)
                print(f"\n{_function.__name__}: {output}")
            except:
                print(f"\n{_function.__name__}: None")
                runTimes.append(None)

    elif len(list_of_args) == 1:
        # Get runtimes and print results
        for _function in list_of_functions:
            try:
                time_start = time.time() # Init time
                output = _function(list_of_args[0])
                time_end = time.time()
                runtime = time_end - time_start
                if runtime < 0.000001:
                    runTimes.append(None)
                else:
                    runTimes.append(runtime)
                print(f"\n{_function.__name__}: {output}")
            except:
                print(f"\n{_function.__name__}: None")
                runTimes.append(None)
    elif len(list_of_args) == 2:
        # Get runtimes and print results
        for _function in list_of_functions:
            try:
                time_start = time.time() # Init time
                output = _function(list_of_args[0],list_of_args[1])
                time_end = time.time()
                runtime = time_end - time_start
                if runtime < 0.00001:
                    runTimes.append(None)
                else:
                    runTimes.append(runtime)
                print(f"\n{_function.__name__}: {output}")
            except:
                print(f"\n{_function.__name__}: None")
                runTimes.append(None)

    # Get slowest runtime
    slowestFunction = list_of_functions[0]
    slowestTime = runTimes[0]
    slowestFunctionIndex = 0
    try:
        for index in range(numFunctions):
            if runTimes[index] != None:
                if slowestTime < runTimes[index]:
                    slowestFunction = list_of_functions[index]
                    slowestTime = runTimes[index]
                    slowestFunctionIndex = index
                else:
                    pass
        print(f"\n{slowestFunction.__name__} was the slowest algorithm at {slowestTime:.5f} seconds.")
    except:
        print("\nNo comparisons to be made.")

    # Compare runtimes
    for index in range(numFunctions):
        if index == slowestFunctionIndex:
            pass
        else:
            if runTimes[index] != None and slowestTime != None:
                runTime = runTimes[index]
                percentFaster = float(slowestTime) / float(runTime)
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


def validateWord_Edgar():
    if 'look' in open('words.txt').read():
        print (True)
    else:
        print (False)
        

def validateWord_Matt(word_input):
    with open("words.txt", 'r') as datafile:
        found = False
        for word in datafile:
            if word_input in word:
                found = True
                break
        if found:
            return True
        else:
            return False


def validateWord_Comparison(word=None):
    list_of_functions = [validateWord_Joshua, validateWord_Edgar, validateWord_Matt]
    print("\nQuestion 2. Given a proposed word that someone wants to play, can you check that is a valid word?")
    if word == None:
        word = input("\nEnter a word: ")
    compareRuntimes(list_of_args=[word], list_of_functions=list_of_functions)


# 3. Given set of tiles and a word, check if word can be made
def makeWord_Joshua(char_list, word):
    word_length = len(word)
    word_index = 1
    for char in word:
        if char in char_list and word_index == word_length:
            return True
        elif char in char_list:
            char_list.remove(char)
            word_index += 1
        else:
            return False


def makeWord_Edgar(char_set, word):
    pass


def makeWord_Matt(char_set, word):
    for each_letter in word:
        try:
            char_set.remove(each_letter)
        except:
            return False            
    return True

            
def makeWord_Comparison(char_list=None, word=None):
    list_of_functions = [makeWord_Joshua, makeWord_Edgar, makeWord_Matt]
    print("\nQuestion 3. Given a set of tiles and a word, can you check if the word can be made from the tiles?")
    if char_list == None:
        if word == None:
            word = input("\nEnter a word: ")
        if char_list == None:
            tiles = input("\nEnter a list of letters seperated by a comma. (ex. h,e,l,l,o): ")
            # Actually a list to allow duplicate letters. Sets cannot have duplicate values.
            char_list = tiles.split(",")
    compareRuntimes(list_of_args=[char_list, word], list_of_functions=list_of_functions)


# 4 Given set of tiles, find words that can be made
def findWords_Joshua(char_list):
    confirmed_words = []
    with open("words.txt", 'r') as words_file:
        for word in words_file:
            word_as_list = list(word.rstrip())
            word_length = len(word_as_list)
            word_index = 0
            chars = char_list.copy()
            for letter in word_as_list:
                if letter in chars and word_index == word_length-1:
                    confirmed_words.append(word.rstrip())
                elif letter in chars:
                    chars.remove(letter)
                    word_index += 1
                else:
                    break
    #print(f"The following words can be made with {str(char_list)}.\n {str(confirmed_words)}")
    return confirmed_words


def findWords_Edgar(char_list):
    pass


def findWords_Matt(char_list):
    confirmed_words = []
    with open("words.txt", 'r') as words_file:
        chars = char_list.copy()
        for word in words_file:
            candidate = True
            letterlist=list(chars)
            for letter not in letterlist:
                candidate = False
                break
            else:
                letterlist.remove(letter)
        if candidate==True:
            confirmed_words.append(word)
    return confirmed_words


def findWords_Comparison(char_list=None):
    list_of_functions = [findWords_Joshua, findWords_Edgar, findWords_Matt]
    print(f"\nQuestion 4. Given a set of tiles, can you find all the words you can make with them?")
    if char_list == None:
        tiles = input("\nEnter a list of letters seperated by a comma. (ex. h,e,l,l,o): ")
        char_list = tiles.split(",")
    compareRuntimes(list_of_args=[char_list], list_of_functions=list_of_functions)


# 5. Find all possible words for given puzzle
def puzzleWords_Joshua(puzzle_letters):
    confirmed_words = []
    with open("words.txt", 'r') as words_file:
        for word in words_file:
            word_as_list = list(word.rstrip())
            word_length = len(word_as_list)
            if word_length >= 5:  # skip words w/ less than 5 letters
                word_index = 0
                chars = puzzle_letters.copy()
                center_letter = puzzle_letters[0]
                has_center_letter = False
                for letter in word_as_list:
                    if letter == center_letter:
                        has_center_letter = True
                    if letter in chars and word_index == word_length-1 and has_center_letter:
                        confirmed_words.append(word.rstrip())
                    elif letter in chars:
                        word_index += 1
                    else:
                        break
            else:
                continue
    #print(f"The following words can be made with {str(puzzle_letters)}.\n {str(confirmed_words)}")
    return len(confirmed_words)


def puzzleWords_Edgar(puzzle_letters):
    pass


def puzzleWords_Matt(puzzle_letters):
    pass


def puzzleWords_Comparison(puzzle_letters=None):
    list_of_functions = [puzzleWords_Joshua, puzzleWords_Edgar, puzzleWords_Matt]
    print(f"\nQuestion 5. Can you write a function to tell you all of possible words for a given puzzle?")
    if puzzle_letters == None:
        tiles = input("\nEnter a puzzle letters. Center letter first. (ex. l,a,b,c,i,n,r): ")
        puzzle_letters = tiles.split(",")
    compareRuntimes(list_of_args=[puzzle_letters], list_of_functions=list_of_functions)


# 6. Sets of eight letters to form most possible bingos
def mostBingos_Joshua():
    bingos = {
        #word: [other, words],
    }
    _8char_words = []
    # Find words that have 8 chars
    with open('words.txt', 'r') as words_file:
        for word in words_file:
            word = word.rstrip()  # remove \n
            word_length = len(word)
            if word_length != 8:  # skip words that are not 8 letters
                continue
            else:
                bingos[str(word.rstrip())] = []
                _8char_words.append(word.rstrip())
    for bingo in bingos:
        # Check if words, using same letters exist
        bingo_chars = list(str(bingo))
        other_bingos = []
        for other_word in _8char_words:
            other_word_list = list(other_word)
            other_word_length = len(other_word_list)
            if other_word != bingo:  # skip duplicates
                other_word_index = 0
                chars = bingo_chars.copy()
                for char in other_word_list:
                    if char in chars and other_word_index == other_word_length -1:
                        other_bingos.append(other_word)
                        #print(f"A match for {bingo} is {other_word}")
                    elif char in chars:
                        chars.remove(char)
                        other_word_index += 1
                    else:
                        continue  # word doesn't match bingo_chars
        bingos[bingo] = other_bingos
    # Compare num of words found, per set
    winning_chars_all = []
    num_winning_charset = 0
    for bingo_chars in bingos:
        if len(bingos[bingo_chars]) > num_winning_charset:
            winning_chars_all.clear()  # reset winning_chars
            winning_chars = []
            winning_chars.append(bingo_chars)
            winning_chars.append(bingos[bingo_chars])
            winning_chars_all.append(winning_chars)
            num_winning_charset = len(bingos[bingo_chars])
        elif len(bingos[bingo_chars]) == num_winning_charset:
            exist_already = False
            for winning_set in winning_chars_all:  # compare to existing winners
                if bingo_chars == winning_set[0]:
                    exist_already = True
                for word in winning_set[1]:
                    if bingo_chars == word:
                        exist_already = True
            if exist_already == False:
                winning_chars = []
                winning_chars.append(bingo_chars)
                winning_chars.append(bingos[bingo_chars])
                winning_chars_all.append(winning_chars)
        else:
            continue
    # Print winning chars and words
    for winner in winning_chars_all:
        chars = winner[0]
        other_words = winner[1]
        num_other_words = len(other_words)
        print(f"The tiles in '{chars}' can spell {str(num_other_words)} other words including:")
        print(str(other_words))
    # Return winner
    return winning_chars_all


def mostBingos_Edgar():
    pass


def mostBingos_Matt():
    pass


def mostBingos_Comparison():
    list_of_functions = [mostBingos_Joshua, mostBingos_Edgar, mostBingos_Matt]
    print(f"\nQuestion 6. What set(s) of eight letters form(s) the most possible bingos?")
    print("This one takes a while, please wait...")
    compareRuntimes(list_of_args=None, list_of_functions=list_of_functions)


if __name__ == "__main__":

    # Run question 1
    #sumOfN_Comparison()

    # Run question 2
    # validateWord_Comparison()

    # # Run question 3
    # makeWord_Comparison()

    # # Run question 4
    # findWords_Comparison()

    # # Run question 5
    puzzleWords_Comparison()

    # # Run question 6
    # mostBingos_Comparison()
