# Scratchwork for portmanteau creation

# Type 1: The words share a common letter, which the first word ends with.
# The letter is removed from the second word and the words are appended.
# Ex. beefalo = beef + buffalo; Reagan + economics = Reaganomics
def pme1(string1, string2):
    for i in range(len(string1) - 1, 0, -1):
        for j in range(0, len(string2)):
            if string1[i] == string2[j]:
                pme = string1[0:i + 1] + string2[j + 1: len(string2)]
                return pme

# def main():
#     word1 = input("Enter a word: ")
#     word2 = input("Enter another word: ")
#     portmanteau = pme1(word1, word2)
#     print(portmanteau)
#
#
# main()