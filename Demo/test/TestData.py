#!/usr/bin/python3

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]

for i in range(4):
   print([row[i] for row in matrix])

'''
[1, 5, 9]
[2, 6, 10]
[3, 7, 11]
[4, 8, 12]
'''

