#Program that takes a string ad counts the no of lower case vowels in it
"""
Write a function count_vowels(word) that takes the string word as input 
and returns the number of occurrences of lowercase vowels 
(i.e. the lowercase letters "aeiou") in word. 
Hint: Python has a built-in string method that can count the number of occurrences of a letter in a string.
"""
def isVowel(ch):
    return ch in ['a','e','i','o','u']
def count_vowels(word):
    count=0
    for i in range(len(word)):
        if isVowel(word[i]):
            count=count+1
    return count
print(count_vowels("aaassseefffggAAgiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
