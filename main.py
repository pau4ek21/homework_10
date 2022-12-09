# class MinStat:
#
#     def __init__(self):
#         self.number = []
#
#     def add_number(self, n):
#         self.number.append(n)
#
#     def result(self):
#         if self.number == []:
#             return None
#         else:
#             return min(self.number)
#
#
# class MaxStat:
#
#     def __init__(self):
#         self.number = []
#
#     def add_number(self, n):
#         self.number.append(n)
#
#     def result(self):
#         if self.number == []:
#             return None
#         else:
#             return max(self.number)
#
#
# class AverageStat:
#
#     def __init__(self):
#         self.number = []
#
#     def add_number(self, n):
#         self.number.append(n)
#
#     def result(self):
#         if self.number == []:
#             return None
#         else:
#             return sum(self.number) / len(self.number)  # сумма и количество элементов
#
#
# # Проверка
# print("Пример 1.")
# values = [1, 2, 4, 5]
#
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
#
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
#
# print('Пример 2.')
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
#
# print(mins.result(), maxs.result(), average.result())
#
# print('Пример 3.')
# values = [1, 0, 0]
#
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
#
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))


# ============================================================================

class Table(object):

    def __init__(self, rows, cols):
        self.rows = rows  # строка
        self.cols = cols  # столбец
        # self.table = [[0] * cols] * rows # почему так нельзя???
        self.table = [[0] * cols for i in range(rows)]

    def get_value(self, row, col):
        if self.rows > row >= 0 and self.cols > col >= 0:
            return self.table[row][col]
        else:
            return None

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        del self.table[row]
        self.rows -= 1

    def delete_col(self, col):
        for row in range(self.rows): # для каждой строки в диапозоне (self.rows)
            self.table[row].pop(col) # удалить столбец с элементом 0 в строку [row]
        self.cols -= 1

    def add_row(self, row):
        self.table.insert(row, [0] * self.cols)
        self.rows += 1

    def add_col(self, col):
        for row in range(self.rows):  # для каждой строки в диапозоне (self.rows)
            self.table[row].insert(col, 0)  # добавить столбец с элементом 0 в строку [row]
        self.cols += 1


print("Пример 1.")
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
#
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

print("Пример 2.")
tab = Table(2, 2)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_col(1)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

print("Пример 3.")
tab = Table(1, 1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 1000)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_row(2)
tab.add_col(0)
tab.add_col(2)

tab.set_value(0, 0, 2000)
tab.set_value(0, 2, 3000)
tab.set_value(2, 0, 4000)
tab.set_value(2, 2, 5000)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()