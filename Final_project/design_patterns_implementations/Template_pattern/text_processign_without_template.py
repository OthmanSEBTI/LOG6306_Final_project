# suppose in a given context we want to perform a 
# text pre-processing but with two different ways 

def preProcessingType1 (text) :
    text = text.replace(' ','_')
    text = text.replace('\n', '_')
    return text 

def preProcessingType2 (text) :
    text = text.replace(' ','')
    text = text.replace('\n', '_')
    return text 


t1 = preProcessingType1('test text line 1 \n test text line 2')
t2 = preProcessingType2('test text line 1 \n test text line 2')

print(t1)
print(t2)