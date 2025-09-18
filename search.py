def search_books_by_author(author_name):

    # Подключение к серверу MySQL
    with pymysql.connect(**config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"USE {db_name}")
            # Запрос имени автора у пользователя
            #author_name = input("Введите имя автора (или его часть): ")

            # SQL-запрос для поиска книг по имени автора
            query = """
                SELECT id, title, author, price
                FROM books
                WHERE author LIKE %s
            """
            cursor.execute(query, ('%' + author_name + '%',)) # LIKE '%leo%'

            # Вывод результатов
            count = 0
            print("\nПодходящие книги:")
            for row in cursor:
                print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Price: {row[3]}")
                count += 1
            if count == 0:
                print("не найдены.")


def search_books_by_client(client_name):
    # Подключение к серверу MySQL
    with pymysql.connect(**config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"USE {db_name}")
            # Запрос имени клиента у пользователя
            #client_name = input("Введите имя клиента (или его часть): ")

            # SQL-запрос для поиска клиентов по имени
            query = """
                SELECT id, firstname, lastname
                FROM users
                WHERE firstname LIKE %s OR lastname LIKE %s
            """
            cursor.execute(query, ('%' + client_name + '%', '%' + client_name + '%'))
            user_list = [user for user in cursor]

            print("\nКлиенты и прочитанные ими книги:")
            for user in user_list:
                user_id = user[0]
                firstname = user[1]
                lastname = user[2]

                # SQL-запрос для поиска книг, прочитанных клиентом
                books_query = """
                    SELECT b.id, b.title, b.author, r.readingyear
                    FROM reading r
                    JOIN books b ON r.bookid = b.id
                    WHERE r.userid = %s
                """
                cursor.execute(books_query, (user_id,))

                count_books = 0
                print(f"\nКлиент: {firstname} {lastname}")
                for book in cursor:
                    count_books += 1
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")
                if count_books == 0:
                    print("не читал книг.")
            if len(user_list) == 0:
                print("не найдены.")

def calculate_total_expenses_by_user(limit):
    # Подключение к серверу MySQL
    with pymysql.connect(**config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"USE {db_name}")
            # Запрос количества строк для вывода у пользователя
            # limit = int(input("Введите количество строк для вывода: "))

            # SQL-запрос для вычисления суммарных затрат каждого пользователя
            query = """
                SELECT u.firstname, u.lastname, SUM(b.price) AS total_expenses
                FROM reading r
                JOIN users u ON r.userid = u.id
                JOIN books b ON r.bookid = b.id
                GROUP BY u.firstname, u.lastname
                ORDER BY total_expenses DESC
                LIMIT %s
            """
            cursor.execute(query, (limit,))

            # Вывод результатов
            print("\nСуммарные затраты каждого пользователя:")
            for row in cursor:
                print(f"{row[0]} {row[1]}, Total Expenses: {row[2]}")


def calculate_total_income_by_book(limit):
    # Подключение к серверу MySQL
    with pymysql.connect(**config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"USE {db_name}")
            # Запрос количества строк для вывода у пользователя
            # limit = int(input("Введите количество строк для вывода: "))

            # SQL-запрос для вычисления общего дохода, сгенерированного каждой книгой
            query = """
                SELECT b.author, b.title, SUM(b.price) AS total_income
                FROM reading r
                JOIN books b ON r.bookid = b.id
                GROUP BY b.author, b.title
                ORDER BY total_income DESC
                LIMIT %s
            """
            cursor.execute(query, (limit,))

            # Вывод результатов
            print("\nОбщий доход, сгенерированный каждой книгой:")
            for row in cursor:
                print(f"Author: {row[0]}, Title: {row[1]}, Total Income: {row[2]}")

def search_books_by_title(title_part):
    # Подключение к серверу MySQL
    with pymysql.connect(**config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"USE {db_name}")
            # Запрос части названия книги у пользователя
            # title_part = input("Введите часть названия книги: ")

            # SQL-запрос для поиска книг по части названия
            query = """
                SELECT id, title, author, price
                FROM books
                WHERE title LIKE %s
            """
            cursor.execute(query, ('%' + title_part + '%',))

            # Получение результатов
            results = [res for res in cursor]

            # Вывод результатов
            if results:
                print("\nНайденные книги:")
                for row in results:
                    print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Price: {row[3]}")
            else:
                print("Книги не найдены.")



