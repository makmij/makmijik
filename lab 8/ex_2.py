def add_books():
    # Функция для добавления книг в словарь
    books = {}  # Инициализация пустого словаря
    while True:
        author = input("Введите фамилию автора (или введите 'stop' чтобы закончить): ")

        if author == 'stop':
            break

        book = input("Введите название книги: ")

        if author not in books:
            books[author] = [book]
        else:
            books[author].append(book)

    return books


def print_books_by_author(books, author):
    # Функция для вывода книг по заданному автору
    if author in books:
        print(f"Книги автора {author}:")
        for book in books[author]:
            print(book)
    else:
        print("Нет книг данного автора")


books = add_books()  # Добавление книг в словарь
author = input("Введите фамилию автора, чтобы вывести его книги: ")
print_books_by_author(books, author)  # Вывод книг по заданному автору