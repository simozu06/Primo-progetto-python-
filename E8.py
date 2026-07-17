#Prima di tutto importiamo le librerie che ci servono (json perchè lavoriamo con file json e random per generare una parola casuale dal file)
import json
import random

# Lettura del file JSON
with open("parole.json", "r") as file:      #Apriamo il file json in modalità lettura e lo chiamiamo file 
    parole = json.load(file)        #Legge il file JSON e ricostruisce l'oggetto Python (in questo caso, una lista di stringhe).

# Sceglie casualmente un elemento dalla lista appena letta usando il metodo .choice del modulo random 
# A cosa serve il metodo .choice? La sua funzione è prendere una sequenza di elementi (come una lista, una tupla o anche una stringa) e scegliere un singolo elemento a caso al suo interno.
parola = random.choice(parole)

#Inizializzo queste due variabili necessarie per il gioco 
lettere_indovinate = []     
tentativi = 8   #I tentativi scenderanno mano a mnao che l'utente sbaglia 


while tentativi > 0:        #Ciclo che chiede all'utente di indovinare la lettera seguente fino a che ha tentativi 

    # Mostra la parola 
    parola_nascosta = ""     #Costruiamo la parola da indovinare (inizalmente sarà fatta da tutti trattini poi mano a mano che si indovinano lettere vengono messe al posto del trattino)

    for lettera in parola:      #Per ogni lettera della parola 
        if lettera in lettere_indovinate:       #Se la lettera è tra le lettere indovinate allora la concatena alla parola_nascosta perchè già stata indovinata 
            parola_nascosta += lettera
        else:           #Se non ha ancora indovinato la lettera allora ci metto il trattino 
            parola_nascosta += "_"

    #Stampiamo la parola_nascosta (che sarà fatta da trattini e lettere già indovinate) e il numero di tentativi rimasti 
    print("\nParola:", parola_nascosta)         
    print("Tentativi rimasti:", tentativi)

    if "_" not in parola_nascosta:   #Se non ci sono trattini nella parola_nascosta (vuol dire che l'utente ha indovinato tutto) allora ha vinto e si esce dal while che gira sui tentativi rimasti 
        #Nota) Questa vittoria avviene quando l'utente indovina tutte le lettere non quando decide di sparare la parola (in quel caso abbiamo un altro controllo)
        print("Complimenti! Hai vinto!")
        break

    #Chiediamo all'utente di inserire la lettera che vuole verificare e la convertiamo in minuscolo con .lower per non avere problemi con lettere maiuscole
    risposta = input("Inserisci una lettera o la parola: ").lower()     

    #A questo punto vediamo i due controlli con i due metodiù

    #Primo metodo LBYL: La tecnica LBYL (Look Before You Leap, ovvero "guarda prima di saltare") consiste
    #nel verificare preventivamente con degli if che un'operazione sia sicura e valida prima di eseguirla.
    #Tutti i controlli gli faremo con degli if a cascata
    if len(risposta) == 1:      #Controllo preventivo 1: L'utente ha inserito una singola lettera?

        if risposta.isalpha():      #Controllo preventivo 2: È una lettera dell'alfabeto (e non un numero o simbolo)?

            if risposta not in lettere_indovinate:      #Controllo preventivo 3: L'aveva già inserita?
                lettere_indovinate.append(risposta)     #Se ha superato i controlli, la aggiunge alla lista delle lettere che ha già inserito 

                if risposta not in parola:      #Se la lettera non fa parte della parola segreta, toglie un tentativo 
                    tentativi -= 1
            #I vari else servono a comunicare all'utente eventuali errori d'inserimento 
            else:       
                print("Lettera già inserita.")

        else:
            print("Inserisci solo lettere.")

    else:   #Se l'utente ha inserito più di un carattere, il programma assume che voglia indovinare l'intera parola.
        
        #Controlla se il tentativo di indovinare la parola intera è corretto. Se lo è, vince 
        #e fa break. Se sbaglia, perde una vita.

        if risposta == parola:
            print("Hai indovinato la parola!")
            break
        else:
            print("Parola sbagliata.")
            tentativi -= 1

#L'ultimo if fuori dal while e questo si attiva quando i tentativi sono uguali a 0 quindi vuol dire 
#che non ha indovinato la parola e ha finito i tentativi. Se è cosi gli dice ha perso e qual'era la parola da indovinare 
if tentativi == 0:
    print("Hai perso!")
    print("La parola era:", parola)