from random import random

class quantumBool:
    def __init__(self, value: bool):
        self.__value = value

    def __str__(self) -> str:
        returnVal = str(self.__value)
        self.__getobserved()
        return returnVal

    def __bool__(self) -> bool:
        returnVal = self.__value
        self.__getobserved()
        return returnVal
        
    def __lt__(self, other: object) -> bool:
        returnVal = self.__value < other
        self.__getobserved()
        return returnVal
    
    def __le__(self, other: object) -> bool:
        returnVal = self.__value <= other
        self.__getobserved()
        return returnVal
        
    def __eq__(self, other: object) -> bool:
        returnVal = self.__value == other
        self.__getobserved()
        return returnVal
    
    def __ne__(self, other: object) -> bool:
        returnVal = self.__value != other
        self.__getobserved()
        return returnVal
    
    def __gt__(self, other: object) -> bool:
        returnVal = self.__value > other
        self.__getobserved()
        return returnVal
    
    def __ge__(self, other: object) -> bool:
        returnVal = self.__value >= other
        self.__getobserved()
        return returnVal
    
    def __getobserved(self):
        self.__value = random() < 0.5
        


if __name__ == "__main__":
    print("hee hee")

    a = quantumBool(True)

    print()
    print("a")
    print(a)
    print(a)
    print(a)
    print(a)
    print(a)

    print()
    print("comparisons")
    print(a < True)
    print(a <= True)
    print(a == True)
    print(a != True)
    print(a > True)
    print(a >= True)
    