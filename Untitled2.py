#pedir la edad 
edad=int(input("ingrese un valor:"))
if edad>0 and edad <12:
    print ("es un niño")
elif edad>13 and edad<17:
    print ("es un adolescente")
elif edad>18 and edad <64:
    print ("es un adulto")
else:
    print("es un adulto mayor")