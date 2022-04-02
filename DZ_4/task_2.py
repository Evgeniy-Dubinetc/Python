print("Задача 2")
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.


import math

# Функция поиска i-го простого числа, без использования алгоритма «Решето Эратосфена»


def sieve_without_eratosthenes(i):
    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


# Функция поиска i-го простого числа, используя алгоритм «Решето Эратосфена»
def sieve_eratosthenes(i):
    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]

# Функция возвращает верхнюю границу отрезка на котором лежат i-e количество простых чисел.
# Функция основана на теореме о распределении простых чисел. Количество простых чисел на отрезке
# [1 n] растёт с увеличением n как n / ln(n).


def prime_counting_function(i):
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


user_number = int(input('Введите номер по счету простого числа: '))
print(sieve_without_eratosthenes(user_number))

print('Алгоритм без использования «Решето Эратосфена»')
print(f'{sieve_without_eratosthenes(user_number)} - {user_number} по счёту простое число')

print('Алгоритм с использованием «Решето Эратосфена»')
print(f'{sieve_eratosthenes(user_number)} - {user_number} по счёту простое число')
