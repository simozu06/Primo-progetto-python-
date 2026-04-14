#
# File: Otto_regine.py
#
# Author: E.Romelli, D.Tavagnacco
#
# Date: 2026/04/14
#
# Version: 1.0
#
# Description: Example program to solve 8 queen-like problem 
#              using brute force + random approach
#


def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    # distanza lungo y
    dy = abs(y1 - y0)
    
    # distanza lungo x
    dx = abs(x1 - x0) 

    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression
    return dx == dy     


def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti 
    '''
    # controllo tutte le precedenti fino a questa 'col'
    for c in range(col):     
        # la coordinata X (la riga) è indice (c) 
        # la coordinata Y,(la colonna) è valore lista nell'indice (c)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            # stop se trovo problemi
            return True  
    # nessun incrocio, la posizione va bene e NON incrocia altre colonne        
    return False   


def soluzione_ok(soluzione_posizioni):
    '''Controlla tutte le posizioni della possibile soluzione
       'soluzione_posizioni' per verificare se ognuna delle posizioni 
       (colonne dela permatazione) ogni colonna incrocia la diagonale
       di qualche altra posizione
    '''

    for col in range(1, len(soluzione_posizioni)):
        # verifica se incrocia
        #if incrocia_colonne(soluzione_posizioni, col) == True:
        if incrocia_colonne(soluzione_posizioni, col):
            # stop se trova incroci, la soluzione non è valida
            return False 

    # Se non è ritornato prima, 
    # allora nessun incrocio trvato: posizioni della soluzione valide 
    return True 



import random
import time 

def main():
    # inizializzo generatore permutazioni
    random_generator = random.Random() 
    
    # preparo la "possibile soluzione" con posizoni da testare
    scacchiera = list(range(8)) 
    
    # conto le soluzioni trovate, inizio da 0           
    solutions = 0                 
    
    # misuro il tempo di partenza per la ricerca della soluzione
    start_time = time.time()            
    
    tempo = 0    #Riga per punto 1 

    lista_soluzione = []   #Riga per punto 3 

    # loop finchè non trovo una soluzione
    while solutions < 10:
    
        # permutazione casuale della soluzione 'mescolando' posizioni
        random_generator.shuffle(scacchiera) 
        
        # verifica se la permutazione casuale e' soluzione  
        #if soluzione_ok(scacchiera) == True: 
        if soluzione_ok(scacchiera):
            if tuple(scacchiera) not in lista_soluzione:        #Riga per punto 3 
                # se la soluzione è buona, scrive
                print(f'Found solution {scacchiera} in {time.time() - start_time} s.')
                
                scacchiera_tupla = tuple(scacchiera)      #Cambio il post it della scacchiera facendo un casting da lista a tupla per il punto 3 
                
                lista_soluzione.append (scacchiera_tupla)      #Riga per punto 3 

                tempo = (time.time() - start_time) + tempo    #Riga per punto 1 

                # incremento contatore soluzioni trovate (condizione stop loop)

                solutions = solutions + 1      
            
                # reset timer ricerca soluzione
                start_time = time.time()

            else: 
                print ('Soluzione già trovata')

    media_tempo = tempo / 10  #Riga per punto 1 

    print (f'Il tempo medio in cui si trova una soluzione è {media_tempo} s.')     #Riga per punto 1 

# chiamo la funzione principale 
main()