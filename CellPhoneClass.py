class CellPhone:
    def __init__(self, manufacturer, modelNo, retailPrice):
        self.__manufacturer = manufacturer
        self.__modelNo = modelNo
        self.__retailPrice = retailPrice

    def set_manufact(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_model(self, modelNo):
        self.__modelNo = modelNo

    def set_retail_price(self, retailPrice):
        self.__retailPrice = retailPrice

    def get_manufact(self):
        return self.__manufacturer

    def get_model(self):
        return self.__modelNo

    def get_retail_price(self):
        return self.__retailPrice
