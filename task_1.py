# TODO: 1. Допиши, код який буде зчитувати стрічку з клавіатури і виводити її на екран але кожне слово буде робити з великої букви

text = input('Введіть текст: ')
text2  = ''
al1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
al2 = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


for ind2, val2 in enumerate(al1):
        if val2 == text[0]:
                text2 += al2[ind2]            
                break

for ind, val in enumerate(text): 
    if text[ind-1] != ' ':
        text2 += val
    else:
        for ind2, val2 in enumerate(al1):
            if val2 == text[ind]:
                text2 += al2[ind2]            
                break
    
                
                
print(text2)                   
    
        
# Example:
# "Test 123 test pass TRUE" => "Test 123 Test Pass TRUE"
