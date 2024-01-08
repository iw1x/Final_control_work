def filter_strings(strings):
    new_strings = [] # Создаем пустой новый массив
    # Проходимся по исходному массиву
    for string in strings: # Проверяем длину строки    
        if len(string) <= 3:
            new_strings.append(string) # Добавляем строку в новый массив
    return new_strings # Возвращаем новый массив