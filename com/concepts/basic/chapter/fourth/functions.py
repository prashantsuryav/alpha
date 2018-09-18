def searchForVowels1():
    vowels = set('aeiou')
    word = input("Enter word of your choice")
    found = vowels.intersection(set(word))
    for ch in found:
        print(ch)


def searchForVowels2(word):
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for ch in found:
        print(ch)


def searchForVowels3(word):
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found


def searchForVowel4(word:str) -> set:
    vowels = set('aeiou')
    return vowels.intersection(set(word))