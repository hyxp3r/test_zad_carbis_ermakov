from db import DataBase
import requests

class API_Connection(DataBase):

    def __init__(self) -> None:

        super().__init__()
        self.data = self.cursor.execute("""SELECT url.url, api.key, language.name
                  FROM request
                  JOIN api
                  ON api.id = request.api_id
                  JOIN url
                  ON url_id = url.id
                  JOIN language
                  ON language_id = language.id
                 """).fetchall()

        self.url = self.data[0][0]
        self.key = self.data[0][1]
        self.language = self.data[0][2]
        self.conn.close()

        self.headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Token {self.key}',
            }

class API_Errors:

    error = "Запрос отклонен!\n1. Проверьте ваш API ключ\n2. Проверьте ваше соединение с интернетом "


    def checkResponseError(self, status_code:int):

        if status_code == 200:
            return False
        else:
            return self.error

class API_GetData(API_Connection, API_Errors):


    def getAllAdresses(self, query):

        data = {
                'query': query,
                "language": self.language
                }
        try:
            response = requests.post(url = self.url, headers = self.headers, json = data)
        except:
            return None, self.error

        error = self.checkResponseError(status_code = response.status_code)

     

        return response, error
    
    def getOneArdess(self, query):

        data = {
                'query': query,
                "language": self.language,
                'count': 1
                }
        
        response = requests.post(url = self.url, headers = self.headers, json = data)

        error = self.checkResponseError(status_code = response.status_code)

        return response, error