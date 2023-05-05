
class Formater : 
    text = None
    def format_text(self,text):
        pass

class FormaterType1 (Formater):
    def format_text(self,text):
        self.text = text
        self.text.replace('\n','')
        return self.text

class FormaterType2 (Formater):
    def format_text(self,text):
        self.text = text
        self.text.replace('\t',' ')
        return self.text
    
class FormaterFactory():
    def format_text(self,text):
        Formater = self.create_formater()
        FormatedText = Formater.format_text(text)
        return FormatedText
    def create_formater():
        pass

class FormaterType1Factory(FormaterFactory) :
    def create_formater():
        return FormaterType1()
    
class FormaterType2Factory(FormaterFactory) :
    def create_formater():
        return FormaterType2()
    

formater1 = FormaterType1()
formater2 = FormaterType2()


print(formater1.format_text('text1 \n text2'))
print(formater2.format_text('text1 \t text2'))