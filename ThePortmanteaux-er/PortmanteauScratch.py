# Scratchwork for portmanteau creation

# Type 1: The words share a common letter.
# The letter is removed from the second word and the words are appended.
# Ex. beefalo = beef + buffalo; Reagan + economics = Reaganomics
def commonEndLetter(string1, string2):
    for i in range(len(string1) - 1, 0, -1):
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

# Portmanteau handler function
def pme(string1, string2):
    return common3String(string1, string2)


def main():
    word1 = input("Enter a word: ")
    word2 = input("Enter another word: ")
    portmanteau = pme(word1, word2)
    print(portmanteau)


main()