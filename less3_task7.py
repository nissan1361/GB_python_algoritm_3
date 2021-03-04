# 7 
# В одномерном массиве целых чисел 
# определить два наименьших элемента

array1 = [1, 8, 2, 6, 3, 9]
min_itm = array1[1]
for itm in array1:
    if itm <= min_itm:
        min_itm = itm

array1.remove(min_itm)

min_itm2 = array1[1]
for itm in array1:
    if itm <= min_itm2:
        min_itm2 = itm

print("Два наименьших числа: {}, {}".format(min_itm, min_itm2))