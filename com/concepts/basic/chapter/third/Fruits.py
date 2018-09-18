fruits = {}
fruits['apple'] = 3
fruits['banana'] = 34

print(fruits['banana'])
print('apple' in fruits)

if 'banana' in fruits:
    fruits['banana'] += 1
else:
    fruits['banana'] = 1

print(fruits)