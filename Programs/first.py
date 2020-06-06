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
