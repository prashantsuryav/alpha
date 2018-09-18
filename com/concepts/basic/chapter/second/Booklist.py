book = "My Name is Lakhan and your's trruly"
booklist = list(book)
print(booklist)
print(''.join(booklist[0:3]))
print(''.join(booklist[-6:]))

backwards = booklist[::-1]
print(''.join(backwards))