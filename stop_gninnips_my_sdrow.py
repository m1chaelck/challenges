"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(sentence):
    l = sentence.split()
    for i in range(len(l)):
        if len(l[i]) >= 5:
            l[i] = l[i][::-1]
    return " ".join(l)