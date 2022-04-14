#Файл хранит в себе последовательность целых чисел из диапазона [-10000, 10000].
#Нам необходимо найти количество пар элементов, из которых оба числа кратны 9, а также
#минимальную сумму элементов таких пар. В качестве пары рассматривается два любых
#разных элемента последовательности, а порядок не учитывается. Ответ запишите без
#пробелов: сначала количество, за ним минимальное значение.
f = open('17.txt')
a = []
for s in f:
	a.append(int(s))
pars = []
for i in range(len(a) - 1):
	for j in range(i+1, len(a) - 1):
		if i != j:
			if (a[i] % 9 == 0) and (a[j] % 9 == 0):
				pars.append(a[i] + a[j])
print(len(pars), min(pars))


# Файл хранит в себе последовательность целых чисел из диапазона [-10000, 10000]. 
#Нам необходимо найти количество пар элементов, из которых как минимум одно число 
#кратно 4, а также максимальную сумму элементов таких пар. В качестве пары 
#рассматриваются два элемента, идущих друг за другом. Ответ запишите без пробелов: 
#сначала количество, за ним максимальное значение. 
f = open('17.txt')
a = []
pars = []
for s in f:
    a.append(int(s))
for i in range(len(a) - 1):
    if a[i] % 4 == 0 or a[i + 1] % 4 == 0:
        pars.append(a[i] + a[i + 1])
print(len(pars), max(pars))
