print("Задача 1")
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


result = {}
for i in range(2, 10):
    result[i] = []
    for n in range(2, 100):
        if n % i == 0:
            result[i].append(n)
    print(f'Для числа {i} в диапазоне от 2 до 99 - {len(result[i])} кратных')