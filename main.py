import requests
from db import WorkWithTables, WorkWithData
import os
from interface import InterfaceShow, ValidateInputData
from actionProcessing import ActionProcessing




if __name__ == "__main__":


    if not WorkWithTables().checkTables():

        key = ValidateInputData().API_Input()
        language = ValidateInputData().language_input()

        WorkWithTables().createTables()

        WorkWithData().addUrl()
        WorkWithData().addApi(key = key)
        WorkWithData().addLanguage(language = language )
        WorkWithData().addRequest()


    while True:

        InterfaceShow().showMain()
        choice = ValidateInputData().mainChoice_input()
        result = ActionProcessing().ProcessDistribution(choice = choice)
        print(result)
        
