class Stock:
    def __init__(self,symbol,name,previousPrice,currentPrice):
        self.__symbol=symbol
        self.__name=name
        self.__previousPrice=previousPrice
        self.__currentPrice=currentPrice
    def getName(self):
        return self.__name
    def getSymbol(self):
        return self.__symbol
    def setPreviousPrice(self,previousPrice):
        self.__previousPrice=previousPrice
    def getPreviousPrice(self):
        return self.__previousPrice
    def setCurrentPrice(self,currentPrice):
        self.__currentPrice=currentPrice
    def getCurrentPrice(self):
        return self.__currentPrice
    def getChangePercent(self):
        return (self.__currentPrice - self.__previousPrice)/self.__previousPrice*100

