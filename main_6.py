import math as m
import random as r
import functools as f
import builtins as b
from operator import mul
from asyncio import tasks
#____________________________________________________
N = int(input("\nВведите размер массива N: "))
if N >= 100: 
    N = 100 
if N <= 5: 
    N = 5 
#____________________________________________________

#Генерация массива
#____________________________________________________
mass = []
for i in range(N):
    mass.append(r.randint(-10, 10))
    print('{:d}'.format(mass[i]), end = " ")
print()
#____________________________________________________

#Произведение
#____________________________________________________
l = len(mass)
chet = []
for i in range(l):
    if i % 2 == 0:
        chet.append(mass[i])
print('\nЧетные: ', chet)
print ("Произведение: ", f.reduce(lambda a, b : a * b, chet)) 
#____________________________________________________

#Сумма и сортировка
#____________________________________________________
for i in range(l):
    if mass[i] == 0:
        res = mass[i-1] + mass[i+1]
        print("Сумма: ", res)
sort = list(filter(lambda x: x > 0 & x == 0, mass)) + list(filter(lambda x: x < 0, mass))
print("Отсортированно: ", sort, '\n')
#____________________________________________________
