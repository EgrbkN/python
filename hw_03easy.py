__author__ 'Баукин Егор Юрьевич'

def my_round(number, ndigits):
    x = number * (10 ** (ndigits + 1))
    if x % 10 >= 5:
        number = (x - (x % 10) - 10) / (10 ** (ndigits + 1))
    else:
        number = (x - (x % 10)) / (10 ** (ndigits + 1))
    return number

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

#Задача 2

def lucky_ticket(ticket_number):
    tn1 = ticket_number // 1000
    tn2 = ticket_number % 1000
    sum1 = 0
    sum2 = 0
    length = len(str(ticket_number))
    if length == 6:
        for i in range(3):
            sum1 = sum1 + tn1 % 10
            tn1 = tn1 // 10
            sum2 = sum2 + tn2 % 10
            tn2 = tn2 // 10
    if sum1 == sum2 and length == 6:
        res = 'Билет счастливый!'
    else:
        res = 'Обычный билет :('
    return res


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))