def is_pari (n):    #Funzioni che ritorna True se il numero è pari e Flase se il numeor e dispari

    risultato = False 

    if (n%2 == 0): 
        risultato = True 

    return risultato 

main (): 

    numero = int (input ("Dammi un numero per vedere se è pari o dispari: "))

    result = is_pari (numero)

    print (result)

main ()