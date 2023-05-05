
# Subject class of the observer pattern
class SubjectFile :

    def __init__(self, name, FilesToNotify) :
        self.__name = name
        self.__modifications = []
        self.__FilesToNotify = FilesToNotify

    def notify_subscribers(self):
        for Files in self.__FilesToNotify:
            Files.notify(self.__modifications)

    # here we consider modifications as a buffer
    def new_modifications(self, newModifications):
        self.__modifications = newModifications
        if len(self.__modifications) != 0 :
            self.notify_subscribers()


class FileToNotify :

    def __init__(self, name) -> None:
        self.__name = name
    
    def notify (self, modifications) :
        for line in modifications:
            print(f"line added : {line} || needs to be added in file {self.__name}")



file2 = FileToNotify('file2')
file3 = FileToNotify('file3')

file1 = SubjectFile('file1',[file2,file3])

file1.new_modifications(['if (t=0):','  function()'])


