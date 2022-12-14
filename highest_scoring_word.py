"""
challenge from codewars.com
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
"""

import string

def high(x):
    d = {}
    l = x.split()
    l_res = []
    
    for k,v in enumerate(string.ascii_lowercase, 1):
        d[v] = k
    total = 0
    for i in l:
        temp = 0
        for j in i:
            temp += d[j]
        if temp > total:
            total = temp
            l_res.append(i)
    return l_res.pop()