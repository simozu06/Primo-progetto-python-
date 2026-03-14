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
'''

'''
Terza parte:Scrivete una funzione che usando il numero scelto dall’utente, generi una lista
seguendo questa regola: se il numero è pari, va diviso per 2; se è dispari, va moltiplicato
per 3 e aggiunto 1. Il processo va ripetuto finchè si arriva a 1 o la lista abbia piu’ di 
100 numeri
'''
'''
def lista (x):
    numeri = []       #Questa riga e la riga 69 sono righe in più che non servono per come viene posto l'esercizio ma le ho utilizzate solo per vedere a video la lista finale per vedere se veniva giusto 
    giri = 0        #Dichiaro una variabile giri in modo da contare i giri del ciclo per fermarmi una volta arrivati a 100 che ci indica che la lista ha 100 elementi 
    while (x != 1 and giri<100):       #Entro nel ciclo se il numero è diverso da 1 e se il numero di cicli è minore di 100
        if (x%2 == 0): 
                x = x / 2 
        else: 
                x = (3 * x) + 1 
        numeri.append (x)
        giri = giri + 1      #Aggiorno il numero di giri 
    return numeri 

def main (): 
    y = int(input("Scrivere un numero: \n"))
    lista_finale = lista(y)
    print ("La lista di numeri è:")    #Anche queste due righe non sono necessarie ma servono solo per vedere la lista finale a video
    print (lista_finale)
main ()
'''

'''
Quarta parte: Scrivete una funzione analizza_sequenza(lista) che riceva la lista generata 
e restituisca tre valori: il valore massimo raggiunto, la lunghezza della sequenza e la 
somma di tutti i numeri.
''' 

Def analizza_sequenza (x):          #Per x intendo la lista che dveo prende in input
    giri = 0     #Stessa operazione del punto prima per creare la lista
    numeri [] 
    massimo = x 
    z = x      
    while (z != 1 and giri<100):
        if (z%2 == 0): 
                z = x / 2 
        else: 
                z = (3 * x) + 1 
        giri = giri + 1 
        if (z > x): 
            massimo = z 
        else: 
            massimo = 
        numeri.append (z)    

    #Definisco il massimo della lista

    return giri      #I giri indicheranno proprio la lunghezza della sequenza 

