# 4
# Определить, какое число в массиве встречается чаще всего

array1 = []

array_size = int(input("Введите размер массива:\n >>> "))

i = 0
while i < array_size:
    item = int(input("Введите элемент массива: \n >> "))
    array1.append(item)
    i += 1

# print(array1)

dict1 = {}
i = 0


for it in array1:
    for it2 in array1:
        if it == it2:
            i += 1
            dict1[it] = i
    i = 0

print(dict1) # Выводим количество повторений чисел

