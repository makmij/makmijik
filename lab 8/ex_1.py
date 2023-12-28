data = {
    'Иванов': 20,
    'Сидоров': 68,
    'Петров': 26,
    'Смирнов': 68
}

# Добавляем свои данные в словарь
data['Мирошниченко'] = 52
data['Кузнецов'] = 72

# Вычисляем сумму всех баллов
total_score = sum(data.values())

# Вычисляем средний балл
average_score = total_score / len(data)

# Выводим список участников, у которых балл выше среднего
above_average = [name for name, score in data.items() if score > average_score] #создаем генератор списка, который проходит по  элементам словаря data
print("Участники с баллами выше среднего:", above_average)

# Находим минимальный и максимальный баллы
min_score = min(data.values())
max_score = max(data.values())

# Находим участников с минимальным и максимальным баллом
min_score_participants = [name for name, score in data.items() if score == min_score]
max_score_participants = [name for name, score in data.items() if score == max_score]

# Выводим результаты
print("Минимальный балл:", min_score, "Участники:", min_score_participants)
print("Максимальный балл:", max_score, "Участники:", max_score_participants)
print("Средний балл:", average_score)