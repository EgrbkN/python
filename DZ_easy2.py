__author__ = 'Баукин Егор Юрьевич'

#Задача-1

fruits = ['яблоко', 'банан', 'киви', 'арбуз']

print('1.', fruits[0])
print('2. ', fruits[1])
print('3.  ', fruits[2])
print('4. ', fruits[3])

#Задача-2

list1 = {1, 2, 4, 7, 25, 5}
list2 = {2, 3, 5, 8, 9, 20}
list3 = list1 - list2
print('Первый список:', list1)
print('Второй список:', list2)
print('Первый список без элементов второго:', list3)

#Задача 3

numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ('Исходный список', numb)
new_numb = []
for i in numb:
    if i % 2 == 0:
        new_numb.append(i / 4)
    else:
        new_numb.append(i * 2)
print('Новый список', new_numb)

