from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10]

# Use lambda function with `filter()`
filtered_list = list(filter(lambda x: (x*2 > 10), my_list))

# Use lambda function with `map()`
mapped_list = list(map(lambda x: x*2, my_list))

# Use lambda function with `reduce()`
reduced_list = reduce(lambda x, y: x+y, my_list)

print(filtered_list)
print(mapped_list)
print(reduced_list)