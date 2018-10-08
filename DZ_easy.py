__author__ = 'Баукин Егор Юрьевич'

#Задача 1

number = int (input("Введи число: "))
numberString = str (number)

for index in range (len (numberString)):
    print (numberString [index])
	
#Задача 2
	
a = input ("Выбери и введи значение первой переменной: ")
b = input ("Выбери и введи значение второй переменной: ")

new = a
print ( "Твоя первая переменная: " + b )
print ("Твоя вторая переменная: " + new)


#Задача 3

age = int ( input ( "Сколько тебе лет? "))
 
if age >= 18:
    print("Доступ разрешен!")
else:
    print("Извините, пользование данным ресурсом только с 18 лет.") 