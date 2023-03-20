import sqlite3

class DataBase:

    def __init__(self) -> None:
        
        self.conn = sqlite3.connect("main.db")
        self.cursor = self.conn.cursor()

class WorkWithTables(DataBase):

    def checkTables(self):

        tables = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        self.conn.close()

        if ('api',) not in tables:
            return False
        else:
            return True

            
    def createTables(self):

        self.cursor.execute('''CREATE TABLE api
             (id INT PRIMARY KEY     NOT NULL,
              key TEXT    NOT NULL);''')
        
        self.cursor.execute('''CREATE TABLE url
             (id INT PRIMARY KEY     NOT NULL,
              url TEXT    NOT NULL);''')
        
        self.cursor.execute('''CREATE TABLE language
             (id INT PRIMARY KEY     NOT NULL,
              name TEXT    NOT NULL);''')
        
        self.cursor.execute('''CREATE TABLE request (
                   id INTEGER PRIMARY KEY,
                   url_id INTEGER,
                   api_id INTEGER,
                   language_id INTEGER,
                   FOREIGN KEY (url_id) REFERENCES url (id),
                   FOREIGN KEY (api_id) REFERENCES api (id),
                   FOREIGN KEY (language_id) REFERENCES language (id)

                )''')
        
        self.conn.commit()
        self.conn.close()
        
        
        return "Success"
    
class WorkWithData(DataBase):

    def addUrl(self):
                         
        self.cursor.execute("INSERT INTO url (id, url) VALUES (?, ?)", (1, 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address'))
        self.conn.commit()    
        self.conn.close()

    def addApi(self, key:str):

        self.cursor.execute("INSERT INTO api (id, key) VALUES (?, ?)", (1, key))
        self.conn.commit()
        self.conn.close()
    
    def addLanguage(self, language:str):

        if language == 1:

            self.cursor.execute("INSERT INTO language (id, name) VALUES (?, ?)", (1, 'ru'))
        else:
            self.cursor.execute("INSERT INTO language (id, name) VALUES (?, ?)", (1, 'en'))
            
        self.conn.commit()
        self.conn.close()


    def addRequest(self):

        self.cursor.execute("INSERT INTO request (id, url_id, api_id, language_id ) VALUES (?, ?, ?, ?)", (1, 1, 1, 1))
        self.conn.commit()
        self.conn.close()


    
    def updateApi(self, key:str):

        
        self.cursor.execute("UPDATE api SET key = ? WHERE id = ?", (key, 1))
       
        self.conn.commit()
        self.conn.close()

        return "API ключ успешно обновлен!"
    
    def updateLanguage(self, language:str):
        if language == 1:

            self.cursor.execute("UPDATE language SET name = ? WHERE id = ?", ("ru", 1))
        else:
            self.cursor.execute("UPDATE language SET name = ? WHERE id = ?", ("en", 1))

        self.conn.commit()
        self.conn.close()

        return "Язык успешно обновлен!"





         
        
                





