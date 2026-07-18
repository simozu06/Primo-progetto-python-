#Questo script utilizza l'approccio EAFP ("Easier to Ask Forgiveness than Permission") per la gestione degli errori. Invece di verificare preventivamente 
#la validità di un'operazione (LBYL), si tenta di eseguirla direttamente all'interno di un blocco 'try' e si gestiscono le eventuali conseguenze (eccezioni) in un blocco 'except' a posteriori.
#Nota generale) il programa per quel che riguarda la gestione del gioco ha le stesse righe di codice di LBYL, infatti i commenti si pososno riutilizzare uguali
#Ciò che cambia è la gestione dell'errore: Nel primo file (LBYL) la gestione dell'errore è preventiva: si usano i costrutti if per controllare in anticipo se l'operazione è sicura 
#(es. la lettera è nuova?) e prevenire la nascita di un'eccezione. Nel secondo file (EAFP) la gestione è reattiva: si tenta subito l'operazione dentro un try e si sfrutta
#l'eccezione (ValueError) intercettandola con except per capire che la lettera non era ancora presente e procedere ad aggiungerla.

import json
import random

with open("parole.json", "r") as file:
    parole = json.load(file)

parola = random.choice(parole)

lettere_indovinate = []
tentativi = 8


while tentativi > 0:

    parola_nascosta = ""

    for lettera in parola:
        if lettera in lettere_indovinate:
            parola_nascosta += lettera
        else:
            parola_nascosta += "_"

    print("\nParola:", parola_nascosta)
    print("Tentativi rimasti:", tentativi)

    if "_" not in parola_nascosta:
        print("Complimenti! Hai vinto!")
        break
    
    #stampiamo le lettere che l'utente ha già provato
    print(f"Lettere già provate: {lettere_indovinate}")
    risposta = input("Inserisci una lettera o la parola: ").lower()

    #Ecco qua il cambio della gestione dell'errore. Questo cambia il modo di vedere se la lettera è corretta o è già stata inserita 
    try:        #Iniziamo il blocco in cui proviamo a fare l'operazione 

        if len(risposta) == 1:      #Separiamo il caso in cui l'utente inserisce la singola lettera e la parola 
            # EAFP per il controllo alfabetico: se non è una lettera, lancia un AssertionError e salta giù!
            assert risposta.isalpha()       #per farlo usiamo il comando assert che genera un errore se ciò che viene dopo è errato (quindi in questo caso se non abbiamo inserito una lettera)

            lettere_indovinate.index(risposta)      #Cerchiamo l'indice della lettera nella lista usando .index. Se la lettera non c'è, questa riga fallisce immediatamente, genera un ValueError e salta direttamente all'except (dove controlleremo la correttezza della lettera). Se invece la lettera c'è, il codice continua alla riga successiva.
            print("Lettera già inserita.")      #Se l'indice della lettera c'è vuol dire che la lettera appartiene alle lettere inserite

        else:       #Caso in cui l'utente ha inserito una parola 

            if risposta.split() == parola.split():    #Verifica se la parola è corretta oppure no (esattamente come nel caso LBYL)
                print("Hai indovinato la parola!")
                break
            else:
                tentativi -= 1

    except AssertionError:
        # Se siamo finiti qui, è perché l'assert è fallito: l'utente ha messo un numero o un simbolo!
        print("Errore: inserisci solo lettere, non numeri o simboli!")
        
    except ValueError:      #Quando il try è fallito (ovvero vi è un valuerror nel caso del len(risposta)==1). Quindi ho inserito una nuova lettera allora: 

        lettere_indovinate.append(risposta)     #la appendo alla lista delle lettere inserite

        if risposta not in parola:  #controllo se sta nella parola e in caso abbasso i tentativi 
                tentativi -= 1

#Quando l'utente ha finito le lettere da inserire (tentativi)
if tentativi == 0:
    print("Hai perso!")
    print("La parola era:", parola)