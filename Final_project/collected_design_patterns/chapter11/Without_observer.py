
 
class DefaultFormatter:  
    def __init__(self, name):    
        self.name = name  
        self._data = 0  
 
    def __str__(self):
        return f"{type(self).__name__}: '{self.name}' has data = {self._data}"
 
    @property  
    def data(self):  
        return self._data  
 
    @data.setter  
    def data(self, new_value):  
        try:  
            self._data = int(new_value)  
        except ValueError as e:  
            print(f'Error: {e}')  
         
 
class HexFormatterObs:  
    def notify(self, publisher):  
        value = hex(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now hex data = {value}")  
 
class BinaryFormatterObs:  
    def notify(self, publisher):  
        value = bin(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now bin data = {value}")  

def main():  

    df = DefaultFormatter('test1')  
    formatters_list = []
    print(df)  
 
    print()  
    hf = HexFormatterObs()
    formatters_list.append(hf)  
    df.data = 3  
    for formater in formatters_list :
        formater.notify(df)
    print(df)  
 
    print()  
    bf = BinaryFormatterObs()  
    formatters_list.append(bf)   
    df.data = 21 
    for formater in formatters_list :
        formater.notify(df) 
    print(df)  
 
    print()  
    formatters_list.remove(hf)  
    df.data = 40  
    for formater in formatters_list :
        formater.notify(df) 
    print(df)  
 
    print()   
 
    df.data = 'hello'
    for formater in formatters_list :
        formater.notify(df) 
    print(df)  
 
    print()  
    df.data = 15.8  
    for formater in formatters_list :
        formater.notify(df) 
    print(df)  
 
if __name__ == '__main__':  
    main()
    