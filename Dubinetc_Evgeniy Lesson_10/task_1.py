print("Задача 1")
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    # перегружаю метод инициализации, input_data - это сама матрица
    def __init__(self, input_data):
        # прописываю input_data как атрибут класса
        self.input = input_data
    # перегружаю метод __str__
    def __str__(self):
        # с использованием лист комприхэншен прохожу по списку - self.input, получаю из него линию line, далее с
        # помощью map привожу каждый элемент к строке, разделяю пробелом и превожу каретку на новую строку
        return '\n'.join([' '.join(map(str, line)) for line in self.input])
    # метод __add__ для сложения (matrix_1 + matrix_2)
    def __add__(self, other):
        # создаю переменную для наполнения ее ответом
        answer = ''
        # сравниваю длины полученных матриц
        if len(self.input) == len(other.input):
            # с помощью функции zip получаю каждый элемент из матриц, наполняю линии line_1, line_2
            for line_1, line_2 in zip(self.input, other.input):
                # сравниваю длины полученных линий
                if len(line_1) != len(line_2):
                    return 'Problems with shape'

                # если все отлично, с помощью zip получаю каждый элемент из line_1, line_2 и складываю их,
                # и помещаю во временную переменную summed_line
                summed_line = [x + y for x, y in zip(line_1, line_2)]
                # записываю полученные значения через пробел в строку answer, и перевожу каретку на нову строку \n
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Problems with shape'
        return answer


matrix_1 = Matrix([[5, 7], [5, 1], [8, 9], [7, 9]])
matrix_2 = Matrix([[3, 5], [3, 2], [5, 7], [5, 7]])
print(matrix_1)
print("---")
print(matrix_1 + matrix_2)  # matrix_1.__add__(matrix_2)
