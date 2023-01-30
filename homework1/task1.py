#Найдите сумму цифр трехзначного числа.

n = int(input ("Введите трехзначное число  "))

digit1 = n % 10
digit2 = n % 100 // 10
digit3 = n // 100
 
print (digit1+digit2+digit3)

