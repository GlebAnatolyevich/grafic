import sqlite3

class BDGraf:
    connection = sqlite3.connect('databasegraf.db')
    cursor = connection.cursor()



### Select ###
#   Cписок всех таблиц в БД
    def sqlite_master(self):
        self.cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
        # Получение результатов запроса
        tables = self.cursor.fetchall()

        # Вывод названий таблиц
        for table in tables:
            print(table[0])

#   Cписок всех активных работников
    def select_users(self):
        self.cursor.execute("SELECT * FROM users ;")
        # Получение результатов запроса
        tables = self.cursor.fetchall()
        print(tables)

#   Поиск пользователя по id в таблице users
    def select_user(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id = '" + user_id + "';")
        tables = self.cursor.fetchall()
        return tables

#   Поиск смен за день по дате
    def select_chart_date(self,date):
        self.cursor.execute("SELECT * FROM chart WHERE change_date = '"+date+"';")
        tables = self.cursor.fetchall()
        return tables

    def select_chart_no_type_date(self,):
        self.cursor.execute("SELECT * FROM chart WHERE type_day IS NULL")
        tables = self.cursor.fetchall()
        return tables


   # def select_change_date(self, user_id):
   #     self.cursor.execute("SELECT * FROM chart WHERE user_id = '" + user_id + "';")
    #    tables = self.cursor.fetchall()
    #    return tables


#   Поиск смены для получения информации о таблице change
    def select_change_id(self, change_id):
        self.cursor.execute("SELECT * FROM change WHERE change_id = '" + change_id + "';")
        tables = self.cursor.fetchall()
        return tables
### Select ###




### insert ###

    def insert_chart(self,change_date,user_id,change_id):
        self.cursor.execute('INSERT INTO chart ( change_date, user_id,change_id) VALUES ( ?, ?, ?)', ( change_date,user_id,change_id))
        self.connection.commit()

### insert ###




### UODATE ###
    def update_chart_type_date(self,chart_id,type_date):
        self.cursor.execute('UPDATE chart SET type_day = ? WHERE id = ?',(type_date,chart_id))
        self.connection.commit()
### UODATE ###


#   commit_and_close
    def connection_commit_and_close(self):
        self.connection.commit()
        self.connection.close()