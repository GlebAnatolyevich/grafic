import sqlite3

class BDGraf:
    connection = sqlite3.connect('databasegraf.db')
    cursor = connection.cursor()



### Select ###
#   Cписок всех таблиц в БД
    def sqlite_master(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        # Получение результатов запроса
        tables = self.cursor.fetchall()

        # Вывод названий таблиц
        for table in tables:
            print(table[0])

#   Cписок всех активных работников
    def select_user(self):
        self.cursor.execute("SELECT * FROM users ;")
        # Получение результатов запроса
        tables = self.cursor.fetchall()

        print(tables)

#   Поиск смен за день по дате
    def select_change_date(self,date):
        self.cursor.execute("SELECT * FROM chart WHERE change_date = '"+date+"';")
        tables = self.cursor.fetchall()
        return tables

#   Поиск пользователя по id в таблице users
    def select_users(self,user_id):
        self.cursor.execute("SELECT name FROM users WHERE user_id = '" + user_id + "';")
        tables = self.cursor.fetchall()
        return tables

#   Поиск смены для получения информации о таблице change
    def select_change(self, change_id):
        self.cursor.execute("SELECT time_start,time_end FROM change WHERE change_id = '" + change_id + "';")
        tables = self.cursor.fetchall()
        return tables
### Select ###


#   commit_and_close
    def connection_commit_and_close(self):
        self.connection.commit()
        self.connection.close()