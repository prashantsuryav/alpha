vowel = ['a', 'e', 'i', 'o', 'u']
# word = "Prashant"
word = input('provide a word: ')
found = []

for ch in word:
    if ch in vowel:
        if ch not in found:
            found.append(ch)

print('vowels hits: ', found)
print('count: ', len(found))

word = ['idk', 'lol']
#lifo = word.pop()
#print(lifo)
fifo = word.pop(0)
print(fifo)
