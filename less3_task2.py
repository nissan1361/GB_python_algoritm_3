# 2 Во втором массиве сохранить индексы четных элементов первого массива. 
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив 
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. 
# именно в этих позициях первого массива стоят четные числа

first_array = []
array_size = int(input("Введите размер первого массива:\n >>> "))
i = 0
while i < array_size:
    item = int(input("Введите элемент массива: \n >> "))
    first_array.append(item)
    i += 1

print(first_array)

second_array = []

ind = 0
while ind < array_size:
    if (first_array[ind] % 2) == 0:
        second_array.append(ind)
    ind = ind + 1

print("индексы четных элементов: \n {}".format(second_array))

