'''
MIT License

Copyright (c) 2018 Packt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

class Publisher:  
    def __init__(self):  
        self.observers = []  
 
    def add(self, observer):  
        if observer not in self.observers:  
            self.observers.append(observer)  
        else:  
            print(f'Failed to add: {observer}')  
 
    def remove(self, observer):  
        try:  
            self.observers.remove(observer)  
        except ValueError:  
            print(f'Failed to remove: {observer}')  
 
    def notify(self):  
        [o.notify(self) for o in self.observers]  
 
class DefaultFormatter(Publisher):  
    def __init__(self, name):  
        Publisher.__init__(self)  
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
        else: 
            self.notify()  
 
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
    print(df)  
 
    print()  
    hf = HexFormatterObs()  
    df.add(hf)  
    df.data = 3  
    print(df)  
 
    print()  
    bf = BinaryFormatterObs()  
    df.add(bf)  
    df.data = 21  
    print(df)  
 
    print()  
    df.remove(hf)  
    df.data = 40  
    print(df)  
 
    print()  
    df.remove(hf)  
    df.add(bf)  
 
    df.data = 'hello'  
    print(df)  
 
    print()  
    df.data = 15.8  
    print(df)  
 
if __name__ == '__main__':  
    main()
    