def menu():
    op = int(input("Ingresen la opción que desean realizar: "))
    print("1. Decimal a Hexagecimal")
    print ("2. Hexagecimal a Decimal") 
    if op == 1:
        DecimalAHexadecimal()
    if op == 2:
        print(HexadecimalADecimal(input("escribe el hexadecimal a convertir a decimal : "))) 
    else:
        print("adiós")
        
          
            
        
values = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8": 8, "9": 9, "A": 10, "B": 11, "C":12, "D":13, "E": 14, "F":15}


def HexadecimalADecimal(number):
    list=[]
    number = number.upper()
    sum=0
    power=0

    for i in number:
        list.append(i)
    list.reverse()
    for i in list:
        t=values.get(i)
        sum=sum+t*16**power
        power=power+1


    return sum

   
          
    
def DecimalAHexadecimal(): 
    decimal = int(input("Introduzca numero decima a convertir a hexadecimal: ")) 
    hexadecimal = "" 
    while decimal != 0: 
        rem = cambios(decimal % 16)
        hexadecimal = str(rem) + hexadecimal
        decimal = int(decimal / 16)
    print("Resultado: " + hexadecimal) 

def cambios(digitos): 
    decimal =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for c in range(7):
        if digitos == decimal[c - 1]:
            digitos = hexadecimal[c - 1]
    return digitos

menu()
