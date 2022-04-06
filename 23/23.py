#У исполнителя есть три команды:
#Прибавить 1
#Умножить на 2
#Умножить на 3
#Определите кол-во пограмм исполнителя, которые преобразуют число 1 в 19.
def task(s, e):					#Создаём функцию
	if s > e:					#Первое условие
		return 0				#Функция возвращает 0
	if s == e:					#Второе условие
		return 1 				#Функция возвращает 1
	if s < e:					#Третие условие
		return task(s+1, e) + task(s*2, e) + task(s*3, e)
print(task(1, 19))				#🠉 - вывод функции с помощью трёх команд

#У исполнителя есть две команды:
#Прибавить 1
#Умножить на 3
#Определите кол-во программ исполнителя, которые преобразуют число 2 в 65,
#при условии, что траектория выполнния программы содержит число 15,
#но не содержит число 45.
def task(s, e):					#Создаём функцию
	if s == 45:					#Функция не содержит число 45
		return 0				#Функция возвращает 0
	if s > e:					#Второе условие
		return 0				#Функция возвращает 0
	if s == e:					#Третие условие
		return 1 				#Функция возвращает 1
	if s < e:					#Четвёртое условие
		return task(s+1, e) + task(s*3, e)
print(task(2,15)*task(15,65))	#🠉 - вывод функции с помощью двух команд
#🠉 - делаем функцию от 2 до 15, а после от 15 до 65

#У исполнителя есть две команды:
#– вычесть 2
#– разделить нацело на 2
#Определите количество программ исполнителя, которые преобразуют число 25 в 2,
#при условии, что траектория выполнения программы содержит число 6. В ответ
#запишите целое число – количество программ.
def task(s, e):
	if s < e:
		return 0
	if s == e:
		return 1
	if s > e:
		return task(s-2, e) + task(s//2, e)
print(task(25, 6)*task(6,2))