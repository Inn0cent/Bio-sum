#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

def populateMatrices(seq1, seq2):
    scoringMatrix = [[]]
    backtrackMatrix = [[]]
    scoringMatrix = initialiseScoring(scoringMatrix, seq1, seq2)
    backtrackMatrix = initialiseBacktrack(backtrackMatrix, seq1, seq2)
    scoringMatrix, backtrackMatrix = createScoring(scoringMatrix, seq1, seq2, backtrackMatrix)
    printMatrix(scoringMatrix)
    print()
    printMatrix(backtrackMatrix)
    print()

    bestScore = scoringMatrix[len(seq1)][len(seq2)]
    seq1, seq2 = trackBack(backtrackMatrix, seq1, seq2)

    return seq1, seq2, bestScore


def createScoring(scoringMatrix, seq1, seq2, backtrackMatrix):
    for i in range(1, len(scoringMatrix)):
        for j in range(1, len(scoringMatrix[0])):
            backtrackMatrix, score = maxValue(c(seq1[j - 1], seq2[i - 1]) + scoringMatrix[i - 1][j - 1], scoringMatrix[i - 1][j] - 2, scoringMatrix[i][j - 1] - 2, backtrackMatrix, i, j)
            scoringMatrix[i].append(score)
    return scoringMatrix, backtrackMatrix


def trackBack(backtrackMatrix, seq1, seq2):
    i = len(seq1)
    j = len(seq2)
    fin1 = ''
    fin2 = ''
    current = backtrackMatrix[i][j]
    while current != "E":
        if current == "D":
            i -= 1
            j -= 1
            fin1 += seq1[j]
            fin2 += seq2[i]
        elif current == "L":
            j -= 1
            fin1 += seq1[j]
            fin2 += '-'
        elif current == "U":
            i -= 1
            fin1 += '-'
            fin2 += seq2[i]
        current = backtrackMatrix[i][j]
    return fin1[::-1], fin2[::-1]


def maxValue(scoreD, scoreU, scoreL, backtrackMatrix, i, j):
    if scoreD >= scoreU and scoreD >= scoreL:
        backtrackMatrix[i].append("D")
        return backtrackMatrix, scoreD
    elif scoreU >= scoreL:
        backtrackMatrix[i].append("U")
        return backtrackMatrix, scoreU
    backtrackMatrix[i].append("L")
    return backtrackMatrix, scoreL


def c(i, j):
    if i == j:
        if i == 'A' or i == 'C':
            return 3
        if i == 'G' or i == 'T':
            return 2
    return -1


def initialiseScoring(scoringMatrix, seq1, seq2):
    value = 0
    for i in range(len(seq1) + 1):
        scoringMatrix[0].append(value)
        value -= 2
    value = -2
    for i in range(len(seq2)):
        scoringMatrix.append([value])
        value -= 2
    return scoringMatrix


def initialiseBacktrack(backtrackMatrix, seq1, seq2):
    backtrackMatrix[0].append("E")
    for i in range(len(seq1)):
        backtrackMatrix[0].append("L")
    for i in range(len(seq2)):
        backtrackMatrix.append(["U"])
    return backtrackMatrix


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()


# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 

best_alignment = []
best1, best2, best_score = populateMatrices(seq1, seq2)
best_alignment.append(best1)
best_alignment.append(best2)

#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------


