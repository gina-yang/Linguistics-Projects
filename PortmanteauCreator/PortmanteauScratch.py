# Scratchwork for portmanteau creation

# Type 1: The words share a common letter.
# The letter is removed from the second word and the words are appended.
# Ex. beefalo = beef + buffalo; Reagan + economics = Reaganomics
def commonEndLetter(string1, string2):
    for i in range(len(string1) - 1, 0, -1):
        print("hello")
        for j in range(0, len(string2)):
            if string1[i] == string2[j]:
                pme = string1[0:i + 1] + string2[j + 1: len(string2)]
                return pme

# Sees if there is a string of length 3 in common between the words. If so, removes from the first word everything
# after the common string and removes from the second word the common string and everything before it
# and concatenates them
# Returns "n/a" if no string in common. Otherwise, returns the concatenated string
# Ex. hamster + termite = hamstermite
def common3String(string1, string2):
    for i in range(len(string1), 2, -1):
        for j in range(0, len(string2) - 2):
            if string1[i-3:i] == string2[j:j+3]:
                return string1[:i] + string2[j+3:]
    return "n/a"

# Returns a list with vowel positions in input string
def vowelFinder(string):
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    vowelList = []
    for i in string:
        if i in vowels:
            vowelList.append(counter)
        counter += 1
    return vowelList

# Returns the portmanteau if the strings contain the same vowel (excluding the first 2 letters of the first word
# and the last 2 letters of the second word)
def sameVowelComp(string1, string2):
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(2, len(string1)):
        for j in range(0, len(string2) - 2, -1):
            print("Looking at: ", j)
            if string1[i] == string2[j] and string1[i] in vowels and string2[j] in vowels:
                return string1[:i] + string2[j:]
    return "n/a"

def diffVowelComp(vowelList1, vowelList2, string1, string2):
    max1 = max(vowelList1)
    min2 = min(vowelList2)
    # print(max1)
    # print(min2)
    return string1[:max1] + string2[min2:]

# Portmanteau handler function
def pme(string1, string2):
    if common3String(string1, string2) != "n/a":
        # print("3 string common")
        return common3String(string1, string2)
    elif sameVowelComp(string1, string2) != "n/a":
        # print("Same vowel")
        return sameVowelComp(string1, string2)
    else:
        # print("Different vowel")
        return diffVowelComp(vowelFinder(string1), vowelFinder(string2), string1, string2)

def main():
    word1 = input("Enter a word: ")
    word2 = input("Enter another word: ")

    print(pme(word1, word2))


main()