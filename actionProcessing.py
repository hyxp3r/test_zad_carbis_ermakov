from apiRequest import API_GetData
from db import WorkWithData
import sys
from interface import ValidateInputData, InterfaceShow

class ActionProcessing:

    def __init__(self) -> None:
        
        self.actions = {
            1 : self.SearchAdressProcess,
            2: self.UpdateApiProcess,
            3: self.UpdateLanguageProcess,
            4: self.ExitProcess      
        }
    

    def ProcessDistribution(self, choice):

        result = None

        for key, function in self.actions.items():
            
            if key == choice:
                result = function()
            
        if result:
            return f'\n{result}\n'
        else:
            return "Введенного номера действия не существует\n"

    def SearchAdressProcess(self):
        
        query = ValidateInputData().address_input()
      
        dict_adresses, error = API_GetData().getAllAdresses(query = query)

        if error:
            return error
        
        dict_adresses = dict_adresses.json()

        if not dict_adresses:
            return "Адреса не найдены"
        
        data = {}
        k = 1

        for item in dict_adresses["suggestions"]:
            data.update({k: item["unrestricted_value"]})
            k += 1

        error = InterfaceShow().showAddresses(data = data)

        if error:
            return error
        
        itog_adress = ValidateInputData().address_input_count(data = data)

        result, error = API_GetData().getOneArdess(query = data[itog_adress])

        if error:
            return error
        
        result = result.json()

        geo_lat, geo_lon = result["suggestions"][0]["data"]["geo_lat"], result["suggestions"][0]["data"]["geo_lon"]

        if not geo_lat or not geo_lon:
            return 'Точные координаты не найдены'


        return f'Широта: {geo_lat}\nДолгота: {geo_lon}'



    def UpdateApiProcess(self):

        key = ValidateInputData().API_Input()

        result = WorkWithData().updateApi(key = key)

        return result
    
    def UpdateLanguageProcess(self):

        language = ValidateInputData().language_input()

        result = WorkWithData().updateLanguage(language = language)

        return result


     
    def ExitProcess(self):
        
        print("\nБольшое спасибо за использование программы!")
        sys.exit()
