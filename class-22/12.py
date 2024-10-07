"""
open(param1 , param2)

param1 = File name / Full File path
param2 = Mode

Mode:
    'r' : Read
    'w' : Write
    'a' : Append
"""

file = open('myfile.txt', 'r')

print(file.read())

file.close()