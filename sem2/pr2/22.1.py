import json

try:
    with open('animals.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Файл не найден")
except json.JSONDecodeError:
    quit()

birds = [animal for animal in data['animals'] if animal['animal_type'] == "Bird"]
print('Данные о птицах:')
for bird in birds:
    print(bird)

diurnal_count = len([animal for animal in data['animals'] if animal["active_time"] == 'Diurnal'])
print('Количество дневных животных:', diurnal_count)

animal_with_min_weight = min(data['animals'], key=lambda x: x['weight_min'])
print('Животное с наименьшим весом:', animal_with_min_weight)