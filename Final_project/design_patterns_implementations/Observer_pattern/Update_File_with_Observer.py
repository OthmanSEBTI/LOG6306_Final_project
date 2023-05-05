
# Subject class of the observer pattern
class SubjectFile :

    def __init__(self, name) :
        self.__name = name
        self.__observersFiles = []
        self.__modifications = []

    def notify_subscribers(self):
        for observerFiles in self.__observersFiles:
            observerFiles.notify(self.__modifications)

    def subscribe_file (self,observerFile):
        self.__observersFiles.append(observerFile)
    
    def unsubscribe_file (self,observerFile):
        self.__observersFiles.append(observerFile)

    # here we consider modifications as a buffer
    def new_modifications(self, newModifications):
        self.__modifications = newModifications
        if len(self.__modifications) != 0 :
            self.notify_subscribers()


class ObserverFile :

    def __init__(self, name) -> None:
        self.__name = name
    
    def notify (self, modifications) :
        for line in modifications:
            print(f"line added : {line} || needs to be added in file {self.__name}")


file1 = SubjectFile('file1')
file2 = ObserverFile('file2')
file3 = ObserverFile('file3')

file1.subscribe_file(file2)
file1.subscribe_file(file3)

file1.new_modifications(['if (t=0):','  function()'])


