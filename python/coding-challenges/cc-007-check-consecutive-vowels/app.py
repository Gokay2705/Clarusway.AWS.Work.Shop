def isVowel(char):
    return char.lower() in 'aeiou'

word = input("Please enter a string: ")

def isConsecutive(word):
    # initialize vowel count
    vCounter = 0
    for letter in word:
        if isVowel(letter): # <= check if the letter is a vowel
            vCounter += 1
            if vCounter >= 2: # <= do the check right here
                return 'Positive'
        else:
            vCounter = 0

    return 'Negative' # <= if we did not find three vovels in the loop, then there is none

print("Please enter a string: " + word)
print(str(isConsecutive(word)))