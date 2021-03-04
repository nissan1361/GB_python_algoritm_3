# 9 Найти максимальный элемент среди 
# минимальных элементов столбцов матрицы

matrix1 = [[1, 2, 4],[8, 5, 0], [4, 0, 3]]
min_itms = []
min_count = 1000 # К сожалению подругому не работает!

for i in matrix1:
    for j in i:
        if j <= min_count:
            min_count = j

    min_itms.append(min_count)
    min_count = 0

print(min_itms)


max_itm = min_itms[0]
for itm in min_itms:
    if itm >= max_itm:
        max_itm = itm

print(max_itm)