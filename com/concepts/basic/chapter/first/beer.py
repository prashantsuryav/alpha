word = "bottle"
for beer_num in range(9,0,-1):
    print(beer_num, word, " of beer on the wall")
    print(beer_num, word, " of beer")
    print("take one")
    print("pass it around. ")
    if beer_num == 1:
        print("no more bottles of beer on the wall")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
    print('__')
