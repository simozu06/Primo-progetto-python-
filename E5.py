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
            tupla_sol = tuple(scacchiera)       # Casting da lista a tupla necessario per due motivi:
                                                # 1. HASHING: Il dizionario delle ripetizioni (Punto 4) richiede chiavi immutabili. 
                                                #    Le liste (mutabili) genererebbero un TypeError, le tuple funzionano perfettamente.
                                                # 2. PASSAGGIO PER RIFERIMENTO: Metodi come .append() salvano un riferimento 
                                                #    all'oggetto, non il suo valore. Modificando la lista originale (es. con shuffle), 
                                                #    la modifica si ripercuoterebbe su tutte le soluzioni già salvate. Il casting 
                                                #    a tupla crea un nuovo oggetto immutabile, slegato dalla lista originale.
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
            print(f"La soluzione {sol} è stata generata casualmente {rip+1} volte.")

#Passiamo adesso alla risoluzione dei punti 5 e 6
def risolvi_punti_5_e_6():
    generatore = random.Random()   ##Creiamo l'oggetto generatore del modulo random che ci servirà per generare una soluzione possibile 
    
    N = 8   #Partiamo dalla classsica scacchiera 8x8 e poi la facciamo crescere
    while True:      #Facciamo partire un while infinito che si fermerà solo con il comando break
        scacchiera = list(range(N))     #Creiamo una lista di N elementi vuota 
        start_time = time.time()    #Facciamo partire il cronometro che ci servirà per il punto 6
        soluzione_trovata = False    #Definiamo una bandiera che ci servirà successivamente 
        
        print(f"Cerco 1 soluzione per scacchiera {N}x{N}...")
        
        # Continua a cercare finché non passano 15 secondi 
        while (time.time() - start_time) < 15:
            generatore.shuffle(scacchiera)   #Mescola casualmente la lista NxN
            if soluzione_ok(scacchiera):   #Se la permutazione della scacchiera va bene 
                soluzione_trovata = True   #abbiamo trovato una soluzione valida in un certo tempo che viene calcolato dopo
                tempo_impiegato = time.time() - start_time
                print(f"   Soluzione trovata in {tempo_impiegato} secondi!")
                break   #Se abbiamo trovato una soluzione in meno di 15 secondi allora possiamo concludere questo while perchè non ci interessa trovarne un'altra per questa dimensione 
                
        if soluzione_trovata:     #Se per la scacchiera NxN abbiamo trovato una soluzione in meno di 15 secondi (la bandiera è alzata, a valore true) passiamo alla dimensione superiore 
            N += 1 # Passa alla scacchiera più grande
        else:   #Se invece soluzione_trovata = false allora vuol dire che per questo N non abbiamo trovato una soluzione in meno di 15 secondi 
            #Se non l'abbiamo trovato allora lo diciamo a video e diciamo a video qual è la dimensione massima su cui
            #siamo riusciti a trovare una soluzione in meno di 15 secondi, ovvero quella prima di N 
            print(f"   Nessuna soluzione trovata in meno di 15s per N={N}.")
            print(f"-> Il lato N più grande risolvibile in < 15s è N={N-1}.")
            break   #finiamo il while esternop perchè abbiamo risolto il punto 6 trovando la dimensione massima 


#Passiamo alla soluzione dell'ultimo punto, ovvero il punto 7: 
#Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi. 
#Scrivete delle funzioni che, una volta trovata una soluzione alla scacchiera, costruiscano le 4 
#soluzioni simmetriche per rotazione. Trovate 5 soluzioni “uniche” e le rispettive soluzioni 
#simmetriche per rotazione per una scacchiera 8x8

#Definiamo prima di tutto una funzione che presa la scacchiera la ruota di 90 gradi. In input questa
#funzione prende la combinazione da ruotare di 90 gradi e la dimensione della scacchiera 
def ruota_90_gradi(posizioni, N):
    nuova_pos = [0] * N      #Creiamo una lista con tutti 0 di dimensione N dove andremo a posizionare le regine una volta ruotata la scacchiera 
    for r in range(N):      #A questo punto scorriamo la lista che indica le vecchie posizioni delle regine e calcoliamo le nuove (chiaramente non serve scorrere tutta la scacchiera, 64 posizioni, perchè considerando la lista eliminiamo tutti gli 0 e consideriamo solo le posizioni delle regine)
        c = posizioni[r]    #Così facendo so che la regina si troverà in coordinate (r, posizioni[r]) ovvero (r, c)
        #Come trovare la nuova posizione della regina una volta ruotata la scacchiera di 90 gradi (rotazione di una matrice di 90 gradi): 
        #Nuova riga = vecchia colonna 
        #Nuova colonna = si ottiene partendo dall'estremità destra della scacchiera (N - 1) e sottraendovi la vecchia coordinata "riga"
        nuovo_r = c
        nuovo_c = N - 1 - r
        nuova_pos[nuovo_r] = nuovo_c    #Riempiamo la nuova lista con le nuovew posizioni delle regine a seguito della rotazione 
    return tuple(nuova_pos)    #Ritorniamo la lista come tupla perchè in seguito dovremo verificarne l'unicità e questa cosa non si può fare con le liste in quanto modificabili

def risolvi_punto_7(N=8):
    generatore = random.Random()
    scacchiera = list(range(N))    #Di nuovo andiamo a definire il generatore e la scacchiera (come lista) di dimensione N per generare una qualsiasi combinazione di regine 
    soluzioni_uniche_trovate = 0     #Contatore per trovare le 5 soluzioni uniche 
    famiglie_soluzioni = []    #Lista dove per ciascuna soluzione salveremo la soluzione con le sue 3 rotazioniin modo poi da controllare ogni volta se trovata una nuova soluzione questa non è uguale alle vecchie + le loro rotazioni. Chiameremo la sol + le 3 rotazioni una famiglia che è formata da 4 liste
    
    while soluzioni_uniche_trovate < 5:     #Continuiamo a girare fino a che non troviamo 5 famiglie di soluzioni (la soluzione + le rotazioni) uniche
        generatore.shuffle(scacchiera)    #Creiamo una permutazione casuale della scacchiera 8x8
        if soluzione_ok(scacchiera):     #Verifichiamo se la soluzione va bene con il controllo sulle diagonali fatto con la solita funzione
            tupla_sol = tuple(scacchiera)     #Convertiamo la scacchiera valida da lista a tupla per verificarne l'unictà.
            
            # Controlla che non faccia parte di una famiglia (base + rotazioni) già trovata
            is_nuova = True   #Supponiamo che la soluzione sia nuova (quidni non rientri nelle famiglie di soluzioni)
            for famiglia in famiglie_soluzioni:     #Iniziamo a scorrere le varie famiglie già archiviate in famiglie_soluzioni
                if tupla_sol in famiglia:    #Controlliamo se la tupla trovata rientra in una di tutte le possibili configurazioni già salvate 
                    is_nuova = False   #Se è cosi allora abbassiamo la bandiera e chiudiamo il for per controllare l'unicità della soluzione 
                    break
                    
            if is_nuova:   #Se a seguito del controllo la bandiera è ancora alzata allora la soluzione trovata nopn rientra in una di tutte le possibili configurazioni 
                soluzioni_uniche_trovate += 1           #Aumentiamo il contatore delle soluzioni trovate 
                rot_90 = ruota_90_gradi(tupla_sol, N)   #Facciamo ruotare la scacchiera tupla_sol prima di 90, poi di nuovo di 90 (quindi 180) e infine di nuovo di 90 (quindi di 270)
                rot_180 = ruota_90_gradi(rot_90, N)
                rot_270 = ruota_90_gradi(rot_180, N)
                
                # Salviamo l'intera famiglia nella lista dedicata alle famiglie 
                famiglie_soluzioni.append((tupla_sol, rot_90, rot_180, rot_270))
                
                #Stampiamo a vidoe che abbiamo trovato la i-esima famgilia di 5 e poi stampiamo la soluzione trovata e le rispettive rotazioni 
                print(f"\nFamiglia {soluzioni_uniche_trovate}:")
                print(f"  Base (0°):   {tupla_sol}")
                print(f"  Ruotata 90°: {rot_90}")
                print(f"  Ruotata 180°:{rot_180}")
                print(f"  Ruotata 270°:{rot_270}")


#Chiamiamo tutte le funzioni una a una 
print(f" Soluzioni punti 1,2,3,4:")
risolvi_punti_1_a_4()
print("\n=========================================\n")    #Separatore tra le due funzioni 
print(f" Soluzioni punti 5,6:")
risolvi_punti_5_e_6()
print("\n=========================================\n")    #Separatore tra le due funzioni 
print(f" Soluzioni punto 7:")
risolvi_punto_7()