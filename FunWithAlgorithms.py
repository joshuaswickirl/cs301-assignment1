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
def timeComparison(input_for_functions, list_of_functions):
    """
    Measures and compares approximate runtimes for each function in 
    list_of_functions when ran with the input_for_functions argument.
    """
    numFunctions = len(list_of_functions)
    
    # Get runtimes and print results
    runTimes = []  # Init array for function durations
    for _function in list_of_functions:

        time_start = time.time() # Init time
        output = _function(input_for_functions)
        time_end = time.time()
        runtime = time_end - time_start
        runTimes.append(runtime)
        print(f"{_function.__name__}: {output}")

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
    print(f"\n{slowestFunction.__name__} was the slowest algorithm at {slowestTime:.4f} seconds.")

    # Compare runtimes
    for index in range(numFunctions):
        if index == slowestFunctionIndex:
            pass
        else:
            runTime = runTimes[index]
            percentFaster = slowestTime / runTime
            functionName = list_of_functions[index]
            print(f"{functionName.__name__} is {percentFaster:.2f}% faster at {runTime:.4f} seconds.")

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

    timeComparison(input_for_functions = n, list_of_functions = list_of_functions)

#
#   Scrabble logic
#

# 2. Given word, check if it's a valid word



# 3. Given set of tiles and a word



# 4 Given set of tiles, find words that can be made



# 5. Find all possible words for given puzzle



# 6. Sets of eight letters to form most possible bingos



if __name__ == "__main__":

    # Run question 1
    sumOfN_Comparison()