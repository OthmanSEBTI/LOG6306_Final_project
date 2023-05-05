def format_text1(text):
    text.replace('\n','')
    return text

def format_text2(text):
    text.replace('\t','')
    return text

def format_text(text, i):
    if i == 1 :
        return format_text1 (text)
    else :
        return format_text1 (text)

print(format_text('text1 \n text2',1))
print(format_text('text1 \t text2',2))