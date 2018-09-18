evenNumbers = [2,4,6,8,10]


def doubling(someInteger:int) -> int:
    return someInteger + someInteger


doubleList = list(map(doubling, evenNumbers))
print(doubleList)


# using lambda
doubleList = list(map(lambda x: x+x, evenNumbers))
print(doubleList)

# filter
doubleList = list(filter(lambda x: x < 18, evenNumbers))
print(doubleList)

