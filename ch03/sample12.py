my_book = (2010, '자바', 200)
your_book = [2010, '자바', 200]

print(my_book)
print(your_book)

print('-'*30)
your_book[0] = 2025
your_book.append('자바책입니다.')
your_book.remove('자바')
your_book.insert(1,'1교시sample12.py')
print(your_book)