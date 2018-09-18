alist = [1,2,3]


def squrt(anylist):
    for i in anylist:
        yield i*i


# print(squrt(alist))
# d = squrt(alist)
# print(d)
for j in squrt(alist):
    print(j)

