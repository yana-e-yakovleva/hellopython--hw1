# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите число долек "))
m = int(input("Введите число долек "))
k = int(input("Сколько долек отломить "))

if  (k%m==0 or k%n==0) and (k < m*n):
    print('Отлично')
else:
    print('Красиво разломить не удалось')