def create_dictionary():
    # Создание словаря с начальными значениями
    dictionary = {
        "пока": "bye",
        "мир": "world",
        "привет": "hello",
        # Добавьте нужные слова и их переводы в словарь
    }
    return dictionary


def translate_word(word, dictionary):
    # Переводит слово с использованием словаря, если есть соответствующий перевод, иначе оставляет слово без изменений
    translated_word = dictionary.get(word, word)
    return translated_word


def translate_text(text, dictionary):
    # Переводит весь текст, разделяющий его на отдельные слова и переводя каждое слово с помощью функции translate_word
    translated_text = ""
    words = text.split()
    for word in words:
        translated_word = translate_word(word, dictionary)
        translated_text += translated_word + " "
    return translated_text.strip()


dictionary = create_dictionary()
input_text = input("Введите текст: ")
translated_text = translate_text(input_text, dictionary)
print("Переведенный текст:", translated_text)