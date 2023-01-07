#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns
sentence = "At school, I learnt C!"
str1 = "" 
length, first = multiple_returns(str1)
print("Length: {:d} - First character: {}".format(length, first))
