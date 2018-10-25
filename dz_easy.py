__author__: 'Баукин Егор Юрьевич'
import math
 
 
class Triangle:
	def __init__(self, A, B, C):
		def sideLen(dot1, dot2):
			return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)
		self.A = A
		self.B = B
		self.C = C
		self.AB = sideLen(self.A, self.B)
		self.BC = sideLen(self.B, self.C)
		self.CA = sideLen(self.C, self.A)
	def square(self):
		return self.AB * self.BC // 2
	def perimeter(self):
		return self.AB + self.BC + self.CA
	def height(self):
		return self.square() / (self.AB / 2)
	def info(self):
		print('Площадь треугольника равна: ', int(self.square()))
		print('Периметр треугольника равен: ', int(self.perimeter()))
		print('Высота треугольника равна: ', int(self.height()))
		
threeugol = Triangle((3, 2), (6, 7), (0, 12))
 
print(threeugol.info())