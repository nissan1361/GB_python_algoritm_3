# 1 
# В диапазоне натуральных чисел от 
# 2 до 99 определить, сколько из 
# них кратны каждому из чисел в диапазоне от 2 до 9

numbers = []
for i in range(2, 100):
    numbers.append(i)

# print(numbers)

delitel = [2, 3, 4, 5, 6, 7, 8, 9]
result = {}

for num in numbers:
    num = 0
    for i in delitel:
        if (num // i) == 0:
            num += 1
            result[i] = num


print(result) # Выводится Dict, ключ = делитель: значение = количество кратных ему чисел

