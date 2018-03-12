#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

def populate_matrices(seq1, seq2):
    scoring_matrix = [[]]
    backtrack_matrix = [[]]
    scoring_matrix = initialise_scoring(scoring_matrix, len(seq1), len(seq2))
    backtrack_matrix = initialise_backtrack(backtrack_matrix, len(seq1), len(seq2))
    scoring_matrix, backtrack_matrix = create_scoring(scoring_matrix, seq1, seq2, backtrack_matrix)
    #print_matrix(scoring_matrix)
    #print()
    #print_matrix(backtrack_matrix)
    #print()

    best_score = scoring_matrix[len(seq1)][len(seq2)]
    seq1, seq2 = track_back(backtrack_matrix, seq1, seq2)

    return seq1, seq2, best_score


def create_scoring(scoring_matrix, seq1, seq2, backtrack_matrix):
    for i in range(1, len(scoring_matrix)):
        for j in range(1, len(scoring_matrix[0])):
            backtrack_matrix, score = max_value(c(seq1[j - 1], seq2[i - 1]) + scoring_matrix[i - 1][j - 1], scoring_matrix[i - 1][j] - 2, scoring_matrix[i][j - 1] - 2, backtrack_matrix, i)
            scoring_matrix[i].append(score)
    return scoring_matrix, backtrack_matrix


def track_back(backtrack_matrix, seq1, seq2):
    j = len(seq1)
    i = len(seq2)
    fin1 = ''
    fin2 = ''
    current = backtrack_matrix[i][j]
    while current != "E":
        if current == "D":
            i -= 1
            j -= 1
            fin1 = seq1[j] + fin1
            fin2 = seq2[i] + fin2
        elif current == "L":
            j -= 1
            fin1 = seq1[j] + fin1
            fin2 = '-' + fin2
        elif current == "U":
            i -= 1
            fin1 = '-' + fin1
            fin2 = seq2[i] + fin2
        current = backtrack_matrix[i][j]
    return fin1, fin2


def max_value(scoreD, scoreU, scoreL, backtrack_matrix, i):
    if scoreD >= scoreU and scoreD >= scoreL:
        backtrack_matrix[i].append("D")
        return backtrack_matrix, scoreD
    elif scoreU >= scoreL:
        backtrack_matrix[i].append("U")
        return backtrack_matrix, scoreU
    backtrack_matrix[i].append("L")
    return backtrack_matrix, scoreL


def c(i, j):
    if i == j:
        if i == 'A' or i == 'C':
            return 3
        if i == 'G' or i == 'T':
            return 2
    return -1


def initialise_scoring(scoring_matrix, i, j):
    value = 0
    for i in range(i + 1):
        scoring_matrix[0].append(value)
        value -= 2
    value = -2
    for i in range(j):
        scoring_matrix.append([value])
        value -= 2
    return scoring_matrix


def initialise_backtrack(backtrack_matrix, i, j):
    backtrack_matrix[0].append("E")
    for i in range(i):
        backtrack_matrix[0].append("L")
    for i in range(j):
        backtrack_matrix.append(["U"])
    return backtrack_matrix


def print_matrix(matrix):
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
    for i in range(min(len(string1), len(string2))):
        if string1[i] == string2[i]:
            string3 = string3 + "|"
        else:
            string3 = string3 + " "
    print('Alignment ')
    print('String1: ' + string1)
    print('         ' + string3)
    print('String2: ' + string2 + '\n\n')


# ------------------------------------------------------------

# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open('Sequence data/length5000_A.txt', 'r')  # changed from original
seq1 = file1.read()
file1.close()
file2 = open('Sequence data/length5000_B.txt', 'r')
seq2 = file2.read()
file2.close()
start = time.time()

# -------------------------------------------------------------

# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Initialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 

best_alignment = []
best1, best2, best_score = populate_matrices(seq1, seq2)
best_alignment.append(best1)
best_alignment.append(best2)

# -------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken = stop - start

# Print out the best
print('Time taken: ' + str(time_taken))
print('Best (score ' + str(best_score) + '):')
# displayAlignment(best_alignment)

# -------------------------------------------------------------
