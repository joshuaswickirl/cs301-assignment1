#
#   Fun with Algorithms!
#   CS301
#   Jan 8, 2019
#   Joshua Swick, Edgar Diaz, Matthew Jones
#
#

import time

def timeDiff(_function):
    time_i = time.time()
    _function
    return time.time() - time_i

def timeComparison(n,f1,f2,f3):
    f1_time = timeDiff(print(f1(n)))
    f2_time = timeDiff(print(f2(n)))
    f3_time = timeDiff(print(f3(n)))

    # Find fasts time, compare others to that



#1. Sum of the 1st n positive integers

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

def sumOfN_Comparison(n):
    
    print("Joshua's")    
    joshuas_time = timeDiff(print(sumOfN_Joshua(n)))

    print("Edgar's")    
    time_i = time.time()
    print(sumOfN_Edgar(n))
    edgars_time = time.time() - time_i

    print("Matts's")    
    time_i = time.time()
    print(sumOfN_Matt(n))
    matts_time = time.time() - time_i

    print(f"Joshua's: {joshuas_time}")
    print(f"Edgar's: {edgars_time}")
    print(f"Matt's: {matts_time}")

sumOfN_Comparison(10000000)

#
#   Scrabble logic
#

#2. Given word, check if it's a valid word



#3. Given set of tiles and a word



#4 Given set of tiles, find words that can be made



#5. 