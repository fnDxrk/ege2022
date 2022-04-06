#Файл с текстом состоит не более чем из 10^6 символов X, Y, Z. 
#Определите максимальное количество идущих подряд символов, среди которых нет
#символа X. В ответе запишите целое число — длину последовательности.
#Первый способ решения
f = open("24_1.txt")
s = f.readline()
a = s.split('X')	   #Убирает X и разъединяет слова
print(max(a), key=len) #Максимум по длине
#Второй способ решения
f = open('24_1.txt')
s = f.readline()
n = 0
b = 0
for i in range(len(s)):
	if s[i] != 'X':
		n += 1
		b = max(n, b)
	else:
		n = 0
print(b)


#Файл с текстом состоит не более чем из 10^6 символов. Определите самую большую
#последовательность, состоящую только из нечётных цифр. 
#В ответе запишите целое число — длину последовательности.
f = open("24_1.txt")
s = f.readline()
n = 0
b = 0
for i in range(len(s)):
	if s[i] in "13579":
		n += 1
		b = max(n, b)
	else:
		n = 0
print(b)


#В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E, F. 
#Найдите количество цепочек длины 3, удовлетворяющих следующим условиям: 
#2-й символ — один из F, D, E; 
#3-й символ — один из B, C, D, который не совпадает со вторым;
#1-й символ — совпадает с третьим.
#В ответе запишите целое число — количество подходящих цепочек.
f = open('24_1.txt')
s = f.readline()
n = 0
for i in range(len(s)):
	if s[i] == s[i+2] and s[i+1] in "FDE" and s[i+2] != s[i+1] and s[i+2] in "BCD":
		n += 1
print(n)


#В файле в одну строку записаны символы W, X, Y, Z. Задача — найти самую длинную
#последовательность, состоящую из символов X, Y, Z, при условии, что соседние символы
#различны. В ответ запишите длину найденной последовательности.
f = open('24.txt')
s = f.readline()
n = 1
b = 1
for i in range(len(s) - 1):
    if s[i] != s[i+1] and s[i] != 'W' and s[i+1] != 'W':
        n += 1
        b = max(b, n)
    elif s[i+1] != 'W':
        n = 1
    else:
        n = 0
print(b)


#Файл с текстом состоит не более чем из 10^6 символов X, Y, Z. 
#Определите максимальное количество идущих подряд символов, среди которых символ
#Z встречается не более одного раза.
f = open('24.txt')
s = f.readline()
a = s.split('Z')
b = 0
for i in range(len(a) - 1):
	is len(a[i]) + len(a[i+1]) + 1 > b:
	b = len(a[i]) + len(a[i+1]) + 1 
print(b)


#Файл с текстом состоит не более чем из 10^6 символов символов X, Y и Z.
#Определите максимальное количество идущих подряд символов, среди которых нет
#подстроки YXZX.
f = open('24.txt')
s = f.readline()
a = s.split('YXZX')
#print(a.index(max(a, key = len))) #Узнать порядковый номерстроки
#print(0, len(a) - 1) # Проверить где он находится(первый, в центре, последний)
					  # Если первый или последний, то +3, а не +6
print(len(max(a, key = len))+ 6)


#Файл с текстом состоит не более чем из 10^7 строчных букв английского алфавита.
#Найдите максимальную длину подстроки, в которой символы «a» и «d» не стоят рядом.
#Для выполнения этого задания следует написать программу. 
f = open('24.txt')
s = f.readline()
s = s.replace('ad', 'a d')
s = s.replace('da', 'd a')
a = s.split()
print(len(max(a, key = len)))


#Текстовый файл содержит строки различной длины. Общий объём файла не
#превышает 1 Мбайт. Строки содержат только строчные буквы латинского алфавита
#(abc...z).
#В строках, содержащих менее 25 букв g, нужно определить и вывести максимальное
#расстояние между одинаковыми буквами в одной строке.
f = open('24.txt')
a = 0
b = "qwertyuiopasdfghjklzxcvbnm" # Пишем алфавит
for s in f:
	if s.count('g') < 25:
		for i in range(len(b)):
			if b[i] in s:
				if s.rindex(s[i]) - s.index(s[i]) > a:
					a = s.rindex(s[i]) - s.index(s[i])
print(a)
