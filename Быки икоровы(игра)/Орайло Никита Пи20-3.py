#Быки и коровы
#Тут создаеться рандомный список из 4 чисел.
import random
number1 = ['0','1','2','3','4','5','6','7','8','9']
random.shuffle(number1)
number = []
n = 0
for i in range(4):
    number.append(number1[n])
    n+=1
print('Введите четырех значное число: ' )
print(number)




#Идет сравнение чисел с загаднным числом.
m = True
while m == True:
    b =input()
    if len(b)>4:
        print('Вы ввели слишком большое число! ')
    elif len(b)<4:
        print('Вы ввели слишком маленькое число! ')
    elif number[0]==b[0] and number[1]==b[1] and number[2]==b[2] and number[3]==b[3]:
        print('Вы угадали число! ')
        m = False
    elif len(set(b))<4:
        print('Вы ввели повторяющиеся числа! ')
    else:
        spisik_bull=[]
  
        
        
        
#Если хотябы одно из чисел совподает с загаданным, то его добавляют в список.(Проще говоря это число совпавших Быков)        
        bull = 0
        if number[0]==b[0]:
            bull+=1
            spisik_bull.append(b[0])
        if number[1]==b[1]:
            bull+=1
            spisik_bull.append(b[1])
        if number[2]==b[2]:
            bull+=1
            spisik_bull.append(b[2])
        if number[3]==b[3]:
            bull+=1
            spisik_bull.append(b[3])
        print('Быков:'+ str(bull))
      


#Выводы.
        mnogestvo_bull = set(spisik_bull)
        mnogestvo_b = set(b)
        mnogestvo_zagad_chislo = set(number)
        mnogestvo_zagad_chislo.difference_update(mnogestvo_bull)
        mnogestvo_b .difference_update(mnogestvo_bull)
        
        
        
#Здесть выодит число совпавших КОРОВ.        
        cow = 0
        for i in mnogestvo_b:
            if i in mnogestvo_zagad_chislo:
                cow+=1
        print('Коров: '+str(cow))
