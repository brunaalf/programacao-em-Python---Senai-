n1 = float (input("digite a primeira nota: "))
n2 = float (input("digite a segunda nota: "))
n3 = float (input("digite a terceira nota: "))


media = (n1 + n2 + n3) /3 
print (f'''
       
aprovado? - {media >= 7}
recuperação? {media < 7 and media > 6}
reprovado? {media <=5}
       ''')
print (n1) 

print (n2) 

print (n3) 

