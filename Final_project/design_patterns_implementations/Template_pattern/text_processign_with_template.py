# suppose in a given context we want to perform a 
# text pre-processing but with two different ways 

from abc import ABC, abstractmethod

class preProcessingTemplate(ABC) :

    @abstractmethod
    def preProcessing (self,text):
        pass

    def replaceSpecialCharacter (self,text):
        text = text.replace('\n', '_')
        return text    
    
    def template_method (self,text):
        preProssecedText = self.preProcessing(text)
        return self.replaceSpecialCharacter(preProssecedText)

class preProcessingType1 (preProcessingTemplate) :

    def preProcessing(self, text):
        text = text.replace(' ','_')
        return text 
        
class preProcessingType2 (preProcessingTemplate) :

    def preProcessing(self, text):
        text = text.replace(' ','')
        return text


t1 = preProcessingType1()
t2 = preProcessingType2()
print(t1.template_method('test text line 1 \n test text line 2'))
print(t2.template_method('test text line 1 \n test text line 2'))