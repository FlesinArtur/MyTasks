# TODO: 1. Допиши, код який буде зчитувати стрічку з клавіатури і виводити її на екран але кожне слово буде робити з великої букви

text = input('Введіть текст: ')
text2  = ''
al1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
al2 = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

i = 1
i2 = 0


while i < len(al1):
    if  text[0] == al1[i]:
        text2 += al2[i]
        i = 0
        break
    i += 1
    
else:
    text2 = text[0]
    i = 0

i += 1
while i < len(text):
    
    if text[i-1] != ' ':
        text2 += text[i]
    
    else:
        
        while i2 < len(al1):
            if  text[i] == al1[i2]:
                text2 += al2[i2]
                i2 = 0
                break
            i2 += 1
        
        else:
            text2 += text[i]
            i2 = 0
    i += 1            
            

                
print(text2)                   
    
        
# Example:
# "Test 123 test pass TRUE" => "Test 123 Test Pass TRUE"
