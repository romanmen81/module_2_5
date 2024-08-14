def get_matrix(n, m, value):
    # Если n или m меньше или равно 0, возвращаем пустой список
    if n <= 0 or m <= 0:
        return []

    # Создаем пустой список для матрицы
    matrix = []

    # Внешний цикл для строк
    for i in range(n):
        # Создаем пустой список для строки
        row = []
        # Внутренний цикл для столбцов
        for j in range(m):
            # Заполняем строку значениями value
            row.append(value)
        # Добавляем заполненную строку в матрицу
        matrix.append(row)

    # Возвращаем заполненную матрицу
    return matrix


# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Выводим результаты на консоль
print(result1)
print(result2)
print(result3)