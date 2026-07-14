#Inizialmente importiamo questi due moduli che ci serviranno a fare una permutazione casuale dele posizioni
#delle regine e a calcolare il tempo 
import random
import time

#Parte introduttiva: abbiamo visto che per evitare lo spreco di memoria andremo a memorizzare le posizioni 
#di una regina con una lista dove l'indice rappresenta la riga e il valore della lista a quel indice la colonna. 
#Ad esempio la regina che è memorizzata come lista[0]=3 sarà sulla riga 0 e la colonna 3. Usando questa memorizzazione
#sappiamo già che due regine non si troveranno mai sulla stessa riga (hanno indici diversi) e neanche sulla stessa
#colonna perchè usando random.shuttle faremo una combinazione casuale dei valori delle liste (da 0 a 7) ma senza
#ripetizioni. Perciò due regine non si troveranno neanche sulla stessa colonna.
#Conclusione: per vedere se due regine si incrociano basterà controllare le diagonali, vediamo come...

#Prima funzione: ritorna vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa diagonale giocando con le distanze
def stessa_diagonale(x0, y0, x1, y1):
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    return dx == dy

#Seconda funzione: Questa funzione controlla se l'ultima regina che abbiamo posizionato (nella riga
#identificata dal parametro riga_corrente) si incrocia in diagonale con una qualsiasi delle regine posizionate 
#nelle righe precedenti. Le posizioni delle regine sulle colonne sono indicate dall'input posizioni che appunto 
#sarò una lista di 8 elementi dove la coppia indice-valore indica le coordinate di una regina.
def incrocia_colonne(posizioni,riga_corrente):
    for c in range(riga_corrente):           #controlliamo su tutte le righe precedenti a quella dell'ultima regina
        # c è la riga, posizioni[c] è la colonna e controlla se due regine su determinate coordinate sono sulla stessa diagonale 
        if stessa_diagonale(c, posizioni[c], riga_corrente, posizioni[riga_corrente]):
            return True
    return False     #Se alla fine viene tornato falso allora vuol dire che la regina corrente non incrocia quelle precedenti sulle diagonali

#Terza funzione: è la funzione finale e controlla se una permutazione (data dall'input soluzione_posizioni) delle regine è una soluzione valida
#facendo un controllo degli incroci sulel diagonali riga per riga con le righe precedenti 
def soluzione_ok(soluzione_posizioni):
    #Usiamo un for per verificare se ci sono incroci sulle diagonali (parto da 1 perchè la regina posizionata
    #sulla riga 0 non ha senso verificarla). Più precisamente vediamo partendo dalla riga 1 fino ad arrivare 
    #alla riga len[soluzione_posizioni], nel caso delle 8 regine sarà 7, se questa incorica sulle diagonali le 
    #regine alle righe precedenti
    for riga_corrente in range(1, len(soluzione_posizioni)):
        if incrocia_colonne(soluzione_posizioni, riga_corrente):
            return False
    return True    #Se alla fine di tutto viene tornato vero allora la soluzione va bene perchè per ogni riga la regina 
                   #su questa riga non incrocia sulle diagonali le righe precedenti 


#Passiamo adesso alla risoluzione dei punti 1,2,3,4 tutti messi in una singola funzione
def risolvi_punti_1_a_4(N=8):         #La funzione è fatta su N che di default è impostato a 8
    
    generatore = random.Random()        #Creiamo l'oggetto generatore del modulo random che ci servirà per generare una soluzione possibile 
    scacchiera = list(range(N))         #Creiamo una lista vuota di N elementi (da 0 a N-1)
    
    soluzioni_uniche = []           # Lista vuota dove salveremo le 10 soluzioni e ne verificheremo poi l'unicità per il punto 3 
    tempi_soluzioni = []            # Lista vuota dove memorizzeremo i tempi con la quale troveremo le singole soluzioni in secondi
    dizionario_ripetizioni = {}     # dizionario vuoto dove conteremo per il punto 4 quante volte una soluzione verrà ripetuta 
    
    tentativi_correnti = 0          # Questo ci servirà per il punto 2 per vedere quanti tentativi faccio prima di trovare una soluzione corretta 
    
    while len(soluzioni_uniche) < 10:       # Questo sarà il ciclo per trovare le soluzionio (girerà fino a che non avrà trovato 10 soluzioni)
        start_time = time.time()        #Facciamo partire il cronometro per trovare la prima soluzione 
        tentativi_correnti += 1         #Aggiungiamo 1 al numero di tentativi perchè stiamo per fare il primo
        
        generatore.shuffle(scacchiera)     #Usando il metodo .shuffle facciamo una permutazione casuale della lista chiamata scacchiera 
        
        if soluzione_ok(scacchiera):           #Se la permutazione è una soluzione allora entriamo nel if 
            tupla_sol = tuple(scacchiera)       # Casting a tupla per poterla usare nei dizionari/liste essendo non modificabili
            
            # Punto 3: Verifica se la soluzione è unica
            if tupla_sol not in soluzioni_uniche:       #Se la tupla trovata è unica (non è tra le soluzioni già trovate)
                tempo_impiegato = time.time() - start_time      #Calcoliamo i secondi impegati a trovare questa soluzione sottraendo il tempo attuale al tempo d'inizio 
                tempi_soluzioni.append(tempo_impiegato)   #Aggiungiamo questo tempo alla lista dei tempi 
                
                soluzioni_uniche.append(tupla_sol)    #Aggiungiamo la soluzione alla lista delle soluzioni solo se non l'abbiamo già trovata (come richiesto dal punto 3)
                dizionario_ripetizioni[tupla_sol] = 0   #Aggiungiamo la tupla al dizionario (sarà la chiave) del punto 4 e inizializziamo il suo valore a 0 per contare le volte in cui la incontro 
                
                # Per il punto 2 stampiamo i tentativi che ci abbiamo messo a trovare la soluzione tupla_sol (unica)
                print(f"Trovata sol. unica {len(soluzioni_uniche)}: {tupla_sol} in {tentativi_correnti} tentativi.")    #Abbiamo trovato la i-esima soluzione che è ... in un certo tempo 
                tentativi_correnti = 0 # Resettiamo per la ricerca della prossima soluzione
                
            else:           #Se la soluzione non è unica dobbiamo aumentare di 1 il valore della chiave del dizionario relativa alla soluzione ripetuta 
                # Punto 4: Contiamo quante volte una soluzione viene ripetuta
                dizionario_ripetizioni[tupla_sol] += 1
                
    #Alla fine di tutto ciò avremo la lista dei tempi, la lista delle soluzioni uniche, abbiamo stampato i tentativi per trovare la singola soluzione e abbiamo il dizionario con le volte che una soluzione si ripete
    # Punto 1: Calcolo del tempo medio
    tempo_medio = sum(tempi_soluzioni) / len(tempi_soluzioni)     #Calcoliamo il tempo medio come somma dei tempi divio il numero di tempi trovati 
    print(f"\n-> Tempo medio per trovare una soluzione: {tempo_medio} secondi.")    
    
    # Punto 4: Stampa delle ripetizioni di quante volte una certa soluzione (ripetuta) è stata trovata 
    print("-> Ripetizioni trovate per le soluzioni:")
    for sol, rip in dizionario_ripetizioni.items():
        if rip > 0:
            print(f"La soluzione {sol} è stata generata casualmente altre {rip} volte.")

