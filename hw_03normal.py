

def fibonacci(n, m):
	fib = [1, 1]
	for i in range(m - 2):
		fib.append(fib[i] + fib[i + 1])
	return fib[n - 1:]

print(fibonacci(10, 17))

#Задача 2

def sort_to_max(origin_list):
	
	for i in range(1, len(origin_list)):
		value = origin_list[i]
		j = i - 1
		while j >= 0:
			if value < origin_list[j]:
				origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
				j = j - 1
			else:
				break
				
a = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(a)
print(a)

#Задача 3

def my_filter(func, x):
	y = []
	for i in range(len(x)):
		if bool(func(x[i])) == True:
			y.append(x[i])
	return y
	
print(my_filter(len, ['', 'not null', 'bla', '', '10']))
print(list(my_filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))

#Задача 4

def parallelogramm(A1, A2, A3, A4):
	if(((abs(A1[0]-A2[0]) == abs(A3[0] - A4[0])) and (abs(A1[1] - A2[1]) == abs(A3[1] - A4[1]))) or
	+(((abs(A1[0] + A2[0])/2 - abs(A3[0] + A4[0])/2 < 0.0001) and (abs(A1[1] + A2[1])/2 - abs(A3[1] + A4[1])/2 < 0.0001)))):
		res = 'Точки являются вершинами параллелограмма.'
	else:
		res = 'Точки не являются вершинами параллелограмма.'
	return res
	
A = []
x = []
for i in range(4):
	x = (input('Введите через пробел координаты {} точки: '.format(i+1))).split(' ')
	A.append(x)
	A[i][0] = float(A[i][0])
	A[i][1] = float(A[i][1])
	
print(parallelogramm(A[0], A[1], A[2], A[3]))