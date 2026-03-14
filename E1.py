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
#Problema da risolvere: sulla variabile se metti una stringa o comunque non un numero non sai se devi risolvere sta roba

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
#Attenzione: quando metto le parentesi quadre dopo una lista sto definendo una lista vuota 
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
    y = float(input("Scrivere un numero: \n"))
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
'''
def analizza_sequenza (x):          #Per x intendo la lista che devo prendere in input
    giri = 0       #Inizializzo il numero di giri a 0 e ad ogni giro del ciclo aumento questo numeor di 1 (andrà poi a ad indicare la lunghezza della stringa finale)
    numeri = [] 
    massimo = x     #Dichiaro una variabile che si chiama massimo e la inizializzo al valore x
    somma = x       #Inizializzo una variabile somma al valore di x e la aggiorno ad ogni giro 
    while (x != 1 and giri<100):     #Faccio lo stesso ciclo di prima con l'if...else per costruire la stringa come da richiesta
        if (x%2 == 0): 
            x = x / 2 
        else: 
            x = (3 * x) + 1
        if (x > massimo):     #Questo if serve per controllare se il nuovo valore è maggiore di quello vecchio e in caso affermativo ridefinire il massimo
            massimo = x  
        giri = giri + 1 
        numeri.append (x)
        somma = somma + x     #Aggiorno la variabile somma aggiungendo a quest'ultima il nuovo valore

    return giri, massimo, somma      #I giri indicheranno proprio la lunghezza della sequenza 

def main ():
    y = float (input("Scrivi un numero: \n"))
    lunghezza, max, som = analizza_sequenza (y)    #Definisco tre variabili che prendono i rispettivi return della funzione e poi gli stampo a video
    print ("La lunghezza della stringa è:", lunghezza)
    print ("Il numero massimo all'interno della stringa è:", max)
    print ("La somma di tutti i valori della stringa è:", som)
main ()
'''

'''
Quinta parte: Scrivete una funzione ricerca(lista) che scorra la lista e stampi solo i 
numeri della sequenza che sono divisibili per 5. Se non ce ne sono, va stampato un 
messaggio dedicato.
''' 

def lista (x):
    numeri = []      
    giri = 0        
    while (x != 1 and giri<100): 
        if (x%2 == 0):     
                x = x / 2 
        else: 
                x = (3 * x) + 1 
        numeri.append (x)
        giri = giri + 1      
    return numeri

def ricerca_lista (y):       #La funzione ha la variabile y ovvero il numero scelto dall'utente
    Multipli_cinque = []      #Creo una stringa vuota dove metterò i mutipli di 5 
    sequenza = lista(y)       #Creo una sequenza che contenga tutti i numeri della lista creata tramite la funzione lista 
    for cifra in sequenza:    #Questo ciclo for mi scorrre tutta la sequenza di numeri della lista e ha come 'variabile' la parola cifra
        if (cifra%5 == 0): 
            Multipli_cinque.append (cifra)   #Se la cifra considerata è divisibile per 5 allora aggiungi la cifra alla stringa Multipli di 5 
    

    return Multipli_cinque

def main(): 
    z = float (input("Scrivi un numero: \n"))
    Multipli_5 = ricerca_lista (z)
    if (Multipli_5 == []):       #Se viene verificata questa condizione vuol dire che all'interno della funzione non sono stati aggiunti valori alla lista vuota 
        print ("Nella lista creata non ci sono numeri divisibili per 5")
    else: 
        print ("I multipli di cinque presenti nella lista sono:", Multipli_5)
main ()