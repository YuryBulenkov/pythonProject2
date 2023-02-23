#Задача 2: Найдите сумму цифр трехзначного числа.
#Пример: 123 -> 6(1 + 2 + 3)

print('Введите трехзначное число: ')
n = int(input())  #трехзначное число содержит а,в,с

c = n % 10  #находим 3 цифру трезначного числа
n = n //10  #находим 1 и 2 цифру трехзначного числа
b = n % 10  #находим 2 цифру трехзначного числа
a = n // 10 #находим 1 цифру трехзначного числа
print('Сумма цифр трехзначного числа: ', (a + b + c))



#задача 4: Петя и Сережа делают из бумаги журавликов.
#Вместе они сделали S журавликов. Сколько журавликов сделал
#каждый ребенок, если известно, что Петя и Сережа сделали
#одинаковое количество журавликов, а катя сделала в два раза
#больше журавликов, чем Петя и Сережа?
#Пример: 6 -> 1 4 1

print('Введите сколько сделали всего журавликов : ')
n = int(input()) #S журавликов = n

P = n // 6 #Петя
K = (n // 6) * 4 #Катя
S = n // 6 #Сергей
print('n ->', P, K, S)



#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачиваетесь
#за проезд и получали билет с номером. Счастливым билетом называют
#такой билет с шестизначным номером, где сумма первых трех цифр равна
#сумме последних трех. Т.е. билет с номером 385916 - счастливый, т.к.
#3 + 8 + 5 = 9 + 1 + 6. Вам требуется написать программу, которая проверяет
#счастливость билета.
#Пример: 385916 -> yes
#        123456 -> no

print('Введите шестизначное число билета: ')
k = str(input())

k_1 = int(k[0]) + int(k[1]) + int(k[2])
k_2 = int(k[3]) + int(k[4]) + int(k[5])

if k_1 == k_2:
   print('Билет счастливый: yes')
elif k_1 != k_2:
   print('Билет счастливый: no')



#Задача 8: Требуется определить, можно ли от шоколадки размером
#n x m долек отломить k долек, если разрешается сделать один
#разлом по прямой между дольками(то есть разломить на два прямоугольника).
#Пример: 3 2 4 -> yes
#        3 2 1 -> no

print('Введите длину n: ')
n = int(input())
print('Введите высоту m : ')
m = int(input())
print('Введите число долек k: ')
k = int(input())

if (k < (m * n)) and (k % n == 0 or k % m == 0):
   print(n, m, k,'-> yes')
else:
   print(n, m, k,'-> no')
