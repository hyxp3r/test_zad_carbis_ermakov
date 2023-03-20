class InterfaceShow:

    main ={
     1: "Поиск адреса",
     2 : "Обновить API ключ",
     3 : "Обновить язык вывода",
     4 : "Выйти"}
    
    error_empty = "Не найдено ни одного адреса"

    def showMain(self):

        for k, v in self.main.items():

            print(f"{k} - {v}")

    def showAddresses(self, data):

        if data:
            for k, v in data.items():
                print(f"{k} - {v}")
        else:
            return self.error_empty




class ValidateInputData(InterfaceShow):

    main_text = "Введите номер действия: "
    main_error_dateType = "\nДействие должно быть числовым!\n"
    main_range_error = "\nВыбор выходит за диапазон\n"
    api_text = "Введите API ключ: "
    adress_text = "Введите адрес: "
    language_text = "Введите язык, на котором будут приходить ответы:\n1 - Русский\n2 - Английский\n"

    api_error = "\nAPI ключ не может быть пустым!\n"
    address_error = "\nАдрес не может быть пустым!\n"
    language_error_empty = "\nЯзык не может быть пустым\n"
    language_error_count = "\nВозможно выбрать только значение 1 или 2\n"
    language_error_dataType = "\nВвод должен быть числовым\n"

    address_count = "Введите цифру адреса: "
    address_error_dataType = "\nВвод должен быть числовым\n"
    address_range_error = "\nВыбор выходит за диапазон\n"

    def __init__(self) -> None:
        
        self.error = True

    def mainChoice_input(self):

        len_data = len(self.main)

        while self.error:

            try:
                choice = int(input(self.main_text))
            except:
                print(self.main_error_dateType)
                continue

            if choice < 1 or choice > len_data:
                print(self.main_range_error)
            else:
                self.error = False
                return choice



    def API_Input(self):

        while self.error:
            api = str(input(self.api_text))

            if api:
                self.error = False
                return api
            else:
                print(self.api_error)

    def address_input(self):

        while self.error:
            address = str(input(self.adress_text))

            if address:
                self.error = False
                return address
            else:
                print("Адрес не может быть пустым!")
    
    def language_input(self):

        while self.error:

            try:
                language = int(input(self.language_text))
            except:
                print(self.language_error_dataType)
                continue

            if language:
                if language in (1,2):

                    self.error = False
                    return language
                else:
                    print(self.language_error_count)
            else:
                print(self.language_error_empty)

    def address_input_count(self, data):

        len_data = len(data)

        while self.error:

            try:
                address_count = int(input(self.address_count))
                print(address_count)
            except:
                print(self.address_error_dataType)
                continue
            
            if address_count > len_data or address_count < 1:
                print(self.address_range_error)
            else:
                self.error = False
                return address_count








