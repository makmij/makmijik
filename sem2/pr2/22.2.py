def read_csv_file(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def write_csv_file(filename, data):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)



try:
    filename = 'countries.csv'
    output_filename_1 = 'countries_income.csv'
    output_filename_2 = 'countries_inflation.csv'
    countries_data = read_csv_file(filename)
    print(countries_data)
    min_income = float(input("Введите минимальный показатель доходов: "))
    max_income = float(input("Введите максимальный показатель доходов: "))
    filtered_countries_income = filtered_countries = [country for country in countries_data if min_income <= float(country[2]) <= max_income]
    write_csv_file(output_filename_1, filtered_countries_income)
    print(f"Данные о странах с показателем доходов от {min_income} до {max_income} записаны в файл {output_filename_1}")

    sorted_countries_inflation = sorted(countries_data, key=lambda x: float(x[3]))
    write_csv_file(output_filename_2, sorted_countries_inflation)
    print(f"Данные о странах, упорядоченные по показателю инфляции, записаны в файл {output_filename_2}")

except Exception as e:
    print(f"Произошла ошибка: {e}")