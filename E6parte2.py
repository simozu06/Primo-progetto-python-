#Questa seconda parte: Avvia un ciclo continuo (un menu) che aspetta i comandi digitati dall'utente sulla 
#tastiera. A seconda del comando inserito (APRI, AGGIUNGI, SALVA, ecc.), fa da "ponte": chiede all'utente 
#le informazioni necessarie e poi passa questi dati ai metodi della classe Rubrica per eseguire 
#materialmente il lavoro.

from E6parte1 import Rubrica        #Cerca un file chiamato E6parte1.py nella stessa cartella e importa la classe Rubrica che vi è contenuta.

rubrica = None  #Crea una variabile chiamata rubrica e la lascia "vuota"
while True:     #Avvia un ciclo infinito. Il programma continuerà a girare in tondo finché non viene interrotto forzatamente dall'interno.
    scelta = input("Operazione: ") #Qua verrà salvata la scelta dell'operazione da fare con la rubrica (le scritte vanno messe in minuscolo)
    if scelta == "EXIT":        #se l'utente digita EXIT allora usciamo dal ciclo infinito 
        break

    #Apertura di una Rubrica
    elif scelta == "apri":      #Se l'utente a digitato apri allora dobbiamo aprire la rubrica con le apposite funzioni però prima dobbiamo vedere se l'utente sta creando da un file json o un file txt
        tipo = input("json o txt? ")

        if tipo == "json":
            nome = input("Nome file: ")    #chiediamo il nome del file che vuole creare
            rubrica = Rubrica.da_json(nome) #usiamo il metodo .da_json della classe Rubbrica applicato al nome del file e lo salviamo nella variabile rubrica (ora non è vuota)
        
        #analogamente se sceglie txt
        elif tipo == "txt":
            nome = input("Nome file: ")
            rubrica = Rubrica.da_testo(nome)
    
    elif scelta == "aggiungi":      #se ha scelto di aggiungere un contatto alla rubrica 

        if rubrica is None:     #Se la rubrica è None allora vuol dire che è chiusa (perciò non esiste) e quindi diciamo all'utente che prima deve aprirla con l'apposita operazione 
            print("Prima apri una rubrica")
            continue        #cotinue è fondamentale è serve a saltare tutto il blocco sottostante e tornare direttamente all'inizio del while
        
        #altrimenti se la rubrica è aperta allora chiede tutti i dati del contatto da aggiungere e poi gli salva usando una coppia chiave-valore ovvero nome_dati dove dati è un altro dizionario nella variabile rubrica 
        nome = input("Nome: ")  

        giorno = int(input("Giorno: "))
        mese = input("Mese: ")
        anno = int(input("Anno: "))
        eta = int(input("Età: "))
        sesso = input("Sesso: ")
        mail = input("Mail: ")

        dati = {
            "giorno": giorno,
            "mese": mese,
            "anno": anno,
            "età": eta,
            "sesso": sesso,
            "mail": mail
        }

        rubrica.aggiungi(nome, dati)           #usiamo l'apposito metodo aggiungi del file Rubrica per aggiugere un contatto

    #Se l'utente ha scelto di rimuovere un contatto 
    elif scelta == "rimuovi":

        if rubrica is None:     #anche in questo caso se la rubrica è vuota (non esiste) allora diciamo che prima bisogna aprirla 
            print("Prima apri una rubrica")
            continue

        nome = input("Nome da eliminare: ")    #Chiediamo il nome della persona da rimuovere 

        rubrica.rimuovi(nome)       #usiamo il metodo .rimuovi del file Rubrica per rimuovere il contatto con il nome richiesto 

    #Le stesse cose le fa per l'operazione di salva e stampa chiedendo nel caso dell'operazione salva come salvare (se json o txt) e nel caso 
    #di stampa il nome del contatto da stampare 

    elif scelta == "salva":

        if rubrica is None:
            print("Prima apri una rubrica")
            continue

        nome = input("Nome file: ")

        rubrica.salva(nome)

    elif scelta == "stampa":

        if rubrica is None:
            print("Prima apri una rubrica")
            continue

        nome = input("Nome: ")

        rubrica.stampa(nome)

    #l'ultimo else e serve nel momento in cui l'operazione inserita non rientra tra quelle disponibili 
    else:
        print("Operazione non valida")