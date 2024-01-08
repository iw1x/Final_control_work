def filter_strings(strings):
    new_strings = [] # Создаем пустой новый массив
    # Проходимся по исходному массиву
    for string in strings: # Проверяем длину строки    
        if len(string) <= 3:
            new_strings.append(string) # Добавляем строку в новый массив
    return new_strings # Возвращаем новый массив

# Входной массив
input_strings = ["Hello", "2", "world", ":-)"]
# Фильтруем строки
filtered_strings = filter_strings(input_strings)
# Выводим результат
print(filtered_strings)