def change():
    expense = 23.75
    money = 100
    print ("Ingresar gasto:")
    print(expense)
    print ("Dinero recibido")
    print(money)
    
    print("\nVuelto\n")
    
    vuelto = (money - expense)
    
    print ("Pesos:")
    
    Pesos= int(vuelto)
    
    print(Pesos)
    
    print("Centavos:")
    centavos = int((vuelto-Pesos)*100)
    
    print(centavos)



