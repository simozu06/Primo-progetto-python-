#La prima cosa che facciamo è definire una particolare funzione (che presenta la scritta yield) detta generatore
#Questa prende in input un parametro (ovvero il numero della tabellina) e tramite un ciclo (da 0 a 10) restituisce 
#due valori: il moltiplicatore e il prodotto (es. tabellina del 3: 3x7 avrò che 7 è il moltiplicatore e 21 il risultato)
def tabellina(numero):
    for i in range(11):
        yield i, numero * i


# Passiamo alla funzione che definisce il gioco delle tabelline 
def gioco():

    while True:     #Creiamo un loop infinito che termina quando vi è break e serve a chiedere il numero della tabellina da analizzare
        try:        #Tenta di eseguire il blocco di codice successivo (permette di gestire potenziali errori).
            numero = int(input("Scegli una tabellina (0-10): "))        #chiediamo il numero della tabellina

        #Gestiamo gli errori (se ho un numero non compreso tra 0 e 10, inclusi, o se l'utente non ha inserito un numero intero)

            if numero < 0 or numero > 10:
                print("Inserisci un numero tra 0 e 10.")
            else:
                break       #Usciamo dal ciclo perchè l'utente ha inserito un numero valido 

        except ValueError:      #Caso particolare: se il try fallisce perchè la conversione di una lettera/simbolo in int genera un valuerror allora stampiamo un messaggio di errore e continuiamo il while 
            print("Errore: inserisci un numero intero.")

    print("\nPer uscire dal gioco scrivi 'basta'.\n")       #Avvisiamo come si esce dal gioco 

    # Uso del generatore per chiedere in maniera interattiva il valore corrente della tabellina 
    for moltiplicatore, risultato in tabellina(numero):     #Prendiamo i risultati del generatore volta per volta (perchè è presente la funzione yield) e li mettiamo in moltiplicatore = i e risultato = numero * i. Questa cosa cotninua per i moltiplicatori dallo 0 al 10 

        while True:     #Crea un nuovo loop infinito per tenere l'utente "bloccato" sulla stessa domanda (il risultato della tabellina corrente) finché non risponde correttamente.

            risposta = input(f"{moltiplicatore} x {numero} = ")    #Stampa a video tramite una f-string il quesito: quanto fa moltiplicatore x numero della tabellina?

            # Uscita personalizzata. Se l'utente ha inserito basta usciamo dalal funzione gioco tramite return 
            if risposta == "basta":
                print("\nGrazie per aver giocato. Arrivederci!")
                return

            try:        #Tenta di convertire e verificare la risposta.
                risposta = int(risposta)        #Convertiamo il numero in intero 

                if risposta == risultato:   #Se la risposta è giusta usciamo dal while e passiamo al moltiplicatore successivo
                    print("Corretto!\n")
                    break
                else:       #Se è sbagliato allora continuiamo il while fino a che non fa giusto 
                    print("Sbagliato, riprova.")

            except ValueError:      #Caso particolare: se la conversione in int fallisce (valuerror con lettere o caratteri) allora messaggio di errore e ricominciamo il while 
                print("Inserisci solo numeri interi oppure 'basta' per uscire.")


# chiamimao la funzione del gioco oer avviare il programma 
gioco()