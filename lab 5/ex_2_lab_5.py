import re


def get_input():
    user_input = input("Введите строку: ")
    if user_input == '':
        print("\nПрограмма завершена пользователем.")
        exit()
    return user_input


def clean_whitespace(input_str):
    cleaned_str = input_str.strip() # удаляет табуляцию в начале и в конце
    return cleaned_str


def format_sentence(sentence):
    sentence = sentence.lower() # возвращает копию строки, где все буквы строчные
    sentence = sentence.capitalize() # делает первую букву слова заглавной
    if sentence.endswith('!'): # ищет данный шаблон в конце строки
        sentence = sentence[:-1]
    if sentence.endswith('...'):
        sentence = sentence[:-3]
    if sentence.endswith('?'):
        sentence = sentence[:-1]
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


def process_input(input_str):
    cleaned_str = clean_whitespace(input_str)
    sentences = re.split(r'\s+', cleaned_str) # s+ больше одной табуляции
    formatted_sentences = [format_sentence(sentence) for sentence in sentences]
    result_str = ' '.join(formatted_sentences)
    return result_str


user_input = get_input()
result = process_input(user_input)
print("Отформатированная строка:", result)