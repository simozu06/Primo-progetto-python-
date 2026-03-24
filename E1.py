'''
File: E1.py
Author: Simone Zuppa
Date: 2026/03/15
Version: 1.0
Description: Analisi di una lista di numeri secondo la congettura di Collatz
'''

#Domande da fare a riga 33 e 34 e in più il programmma deve contenere meno righe di codice possibile (Fai l'esempio della lunghezza della lista)

# 1) FUNZIONE is_pari
# Controlla se un numero è pari.
# Restituisce True se il resto della divisione per 2 è 0,
# altrimenti restituisce False.


def is_pari(n):
#l'espressione n%2 == 0 restituisce già un valore booleano, quindi si può gia ritornare il valore senza passare per l'if
    return n % 2 == 0      


# 2) FUNZIONE intero_positivo
# Chiede all'utente di inserire un numero intero positivo.
# Se il numero inserito è:
# - negativo
# - uguale a zero
# - non intero (es. 3.5)
# il programma continua a chiedere un nuovo input.
# La funzione termina solo quando il valore è corretto.

def intero_positivo():

    #!!!!!!!!!!Se io inserisco un numero come 4.000000000000000000000000000000000000000000001 lo considera come 4 quindi non mi chiede di inserire un altro numero, è un errore che devo risolvere?
    #!!!!!!!!!!primo input dell'utente (Qua se metto float mi da errore esattamente come quando al posto di inserire un numero inserisco una stringa)

    n = float(input("Dammi un numero intero positivo: \n"))

    # il ciclo continua finché:
    # - n è minore o uguale a 0
    # - oppure n non è intero (resto della divisione per 1 diverso da 0)
    while (n <= 0 or n % 1 != 0):

        # nuovo tentativo dell'utente
        n = float(input("Non è un numero intero positivo, riprova: \n"))

    # restituisco il valore convertito in intero
    return int(n)


# 3) FUNZIONE lista
# Genera la sequenza secondo la congettura di Collatz:
#
# se il numero è pari -> n = n / 2
# se il numero è dispari -> n = 3*n + 1
#
# Il processo continua finché:
# - il numero diventa 1
# oppure
# - la lista supera i 100 elementi

def lista(n):

    # creo una lista. Questa lista se il numero è 1 la inizializzo a 1 e se è il numero è diverso da 1 la faccio vuota. Questo perchè 
    # se è 1 e non la inizializzo a 1 non entreremo mai nel ciclo, perciò la sequenza sarà vuota, se invece è diverso da 1 e la inizializzo a 
    # 1, nella maggior parte dei casi ci saranno due 1 nella sequenza
    if n == 1: 
        sequenza = [1]
    else: 
        sequenza = []

    # il ciclo continua finché:
    # - n è diverso da 1
    # - la lunghezza della lista è minore di 100, per vedere ciò uso la funzione len
    while (n != 1 and len(sequenza) < 100):

        # controllo se il numero è pari
        if is_pari(n):
            n = n // 2

        # se non è pari allora è dispari
        else:
            n = (3 * n) + 1

        # aggiungo il nuovo valore alla lista
        sequenza.append (n)

    # restituisco la sequenza generata
    return sequenza


# 4) FUNZIONE analizza_sequenza
# Riceve in input una lista e calcola:
# - valore massimo
# - lunghezza della lista
# - somma di tutti i valori
# Restituisce questi tre risultati.

#Attenzione: la funzione non può ritornare 3 valori devi fare una lista che contenga i tre valori e poi riprenderla nella main

def analizza_sequenza(sequenza):

    # valore massimo presente nella lista tramite la funzione max che analizza il massimo valore nella stringa
    massimo = max(sequenza)

    # numero totale di elementi della lista tramite la funzione len
    lunghezza = len(sequenza)

    # somma di tutti i numeri della lista tramite la funzione somm
    somma = sum(sequenza)

    lista_sequenza = (lunghezza, massimo, somma)
    return lista_sequenza


# 5) FUNZIONE ricerca_lista
# Genera la sequenza di Collatz e cerca al suo interno
# tutti i numeri divisibili per 5.
#
# Se trova multipli di 5 li salva in una lista.
# Alla fine restituisce la lista dei multipli trovati.

#La funzione prende come variabile la sequenza di Collatz generata dalla funzione precedente
def ricerca_lista(sequenza):

    # lista che conterrà i multipli di 5
    Multipli_cinque = []

    # scorro tutti gli elementi della sequenza
    for n in sequenza:

        # controllo se il numero è divisibile per 5
        if (n % 5 == 0):

            # se lo è, lo aggiungo alla lista dei multipli
            Multipli_cinque.append(n)

    return Multipli_cinque


# FUNZIONE PRINCIPALE main
# Gestisce il flusso principale del programma:
#
# 1) chiede quanti numeri analizzare
# 2) salva i numeri inseriti dall'utente
# 3) per ogni numero genera la sequenza di Collatz
# 4) analizza la sequenza
# 5) cerca eventuali multipli di 5

def main():

    # chiedo quanti numeri l'utente vuole analizzare
    x = int(input("Di quanti numeri vuoi analizzare la lista: \n"))

    # lista che conterrà tutti i numeri inseriti
    numeri = []

    # ciclo che richiede all'utente x numeri
    for i in range(x):

        # richiamo la funzione che garantisce un intero positivo
        z = intero_positivo()

        # aggiungo il numero alla lista
        numeri.append(z)

    # analizzo ogni numero della lista
    for n in numeri:

        print("Analisi del numero:", n)

        # genero la sequenza di Collatz
        sequenza = lista(n)
        
        print(sequenza)

        # analizzo la sequenza
        l, m, s = analizza_sequenza(sequenza)      # l = lunghezza, m = massimo e s = somma solo che avevo già usato tutti questi nomi dentro la funzione

        print("La sequenza è:", sequenza)
        print("La lunghezza della sequenza è:", l)
        print("Il numero massimo della sequenza è:", m)
        print("La somma dei valori della sequenza è:", s)

        # cerco i multipli di 5 nella sequenza
        multipli_5 = ricerca_lista(sequenza)

        # controllo se ne esistono
        if multipli_5 == []:
            print("Nella lista non ci sono numeri divisibili per 5")

        else:
            print("I multipli di 5 nella sequenza sono:", multipli_5)


# avvio del programma
main()