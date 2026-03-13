#Esercizio 1, Simone Zuppa 

'''
Prima parte: scrivete una funzione di controllo, is_pari(n), che accetti come parametro 
un numero intero e restituisca True se il numero è pari, False altrimenti.
'''
'''
def is_pari (n): 
    risultato = False  #Preimposto il valore della variabile risultato a False e la faccio poi variare di conseguenza 

    if (n%2 == 0):   #Se il resto della divisine tra n è due è zero (numero pari)
        risultato = True 

    return risultato 

def main ():   #definisco la funzione main che indica l'inizio del vero e proprio programma 

    numero = int (input ("Scrivere un numero per verificare se è pari o dispari: \n"))

    result = is_pari(numero)   #Definisco una variabile result alla quale assegno il risultato della funzione is_pari con il valore scelto dall'utente

    print (result)

main()
'''

'''
Seconda parte: Create una funzione di generazione che chieda all’utente un numero intero 
positivo e lo restituisca come risultato della funzione. Se l’utente inserisce un numero 
non valido (es. negativo o zero), il ciclo deve continuare a richiederlo finché l’input 
non è corretto.
'''

def intero_positivo (n): 
    n = 0   #preimposto come valore di n zero in modo da entrare nel ciclo

    while (n <= 0 or n%1 != 0):   #Creo un ciclo che chieda un numero intero positivo. Entreremo nel ciclo solo se almeno una condizione è vere perciò se il numero è negativo o nullo o se il resto della divisione tra il numero è uno è diverso da 0
        n = float (input("Dammi un numero intero positivo: \n"))   #Metto float perchè se no quando inserisco un numero decimale darà errore, la stessa cosa se inserisco una stringa ma non so come risolvere l'errore

    return n 

def main (): 

    intero = None    #Definisco una variabile senza valore chiamata intero 

    numero = intero_positivo (intero)

    print ("Il numero da te scelto è...")
    print (numero)

main ()


