#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seqList = [[] for _ in range(n)] # create a list of n empty lists
    lastAnswer = 0 # initialize lastAnswer to 0
    result = [] # create an empty list to store the results
    for query in queries:
        index = (query[1] ^ lastAnswer) % n # calculate the index
        if query[0] == 1:
            seqList[index].append(query[2]) # append the element to the list at index
        else:
            lastAnswer = seqList[index][query[2] % len(seqList[index])] # update lastAnswer
            result.append(lastAnswer) # append lastAnswer to the result list
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
