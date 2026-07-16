#Nota generale) A cosa serve encoding="utf-8"? encoding="utf-8" serve a leggere e scrivere correttamente i caratteri speciali (come le lettere accentate) all'interno di un file.
#Nota generale 2) Istanza e oggetto della classe con la stessa cosa e rappresentano la singola rappresentazione 

import json     #Serve per leggere e scrivere file JSON e più avanti nell'esercizio ci servirà fare ciò


class Rubrica:      #Stiamo creando una classe chiamata Rubrica che farà quindi da modello a un certo oggetto/istanza specifica della classe
                    #Per capire il rapporto classe-oggeto ci si può immaginare la classe come l'automobile e l0oggetto come una specifica automobile (per esempio una fiat panda)
                    #Nel nostro caso la classe sarà la rubrica e gli oggetti saranno le singole rubriche (rubrica1, rubrica2, e via dicendo)
    #La funzione init prende in input i dati di un oggetto e lo crea fisicamente come dato dandogli determinati attributi 
    def __init__(self, rubrica):        #Questa è una funzione che viene eseguita automaticamente (poichè si chiama __init__) sul singolo oggetto (dato in input = rubrica) quando viene creato (self serve a dire che si agisce sul singolo oggetto)
        self.contatti = rubrica     #Diremo che l'attributo .contatti (ovvero la caratteristica del singolo oggetto self) corrisponde con la rubrica data in input
        self.aperta = True      #Diremo che l'attributo .aperte è true ovvero che la nostra rubrica è aperta 

    #Vediamo adesso due funzioni per creare la nostra istanza rubrica a partire prima da un file json e poi da un file testo

    @classmethod        #Questa riga indica che il metodo (metodo = funzione scritta all'interni della classe) appartiene alla classe e non ad un oggetto.
    #Questa funzione ci serve per invece di partire da dati già pronti nel codice, crea una nuova Rubrica leggendo i contatti direttamente da un file JSON salvato sul computer.
    def da_json(cls, nome_file):        #Il primo parametro è cls perchè ci troviamo in un classmethod e il secondo è il file da leggere
        with open(nome_file, "r", encoding="utf-8") as file:    #Apriamo in modalità lettura il file nome_file con with open (che verrà chiuso in automatico) e da quel momento in poi lo indichiamo con 'file'
            dati = json.load(file)      #leggiamo il contenuto del file e lo convertiamo in un dizionario python che indichiamo con dati
            return cls(dati)    #restituisce una nuova istanza della classe rubrica (chiamando quindi implicitamente init) passandone i dati appena letti 
        
    @classmethod        
    #Questa funzione è progettata per leggere un file di testo semplice (dove i dati sono separati da un punto e virgola, tipo un file CSV) e trasformarlo in una Rubrica.
    def da_testo(cls, nome_file):   #Anche in questo caso il primo parametro è cls perchè abbiamo un classmethod e il secondo è il nome del file dalla quale inizare a creare la rubrica
        rubrica = {}    #Inizializziamo un dizionario vuoto che conterrà i contatti 

        with open(nome_file, "r", encoding="utf-8") as file:   #Apriamo il file in modalità lettura 
            for riga in file:     #Scorriamo il file di partenza e... 
                parti = riga.strip().split(";")     #strip() serve per togliere gli spazi bianchi e i ritorni a capo invece split ci serve a dividere la singola riga ogni volta che trovo ; creando una lista 

                nome = parti[0]   #Il primo della lista riferita alla riga è il nome 

                #Creiamo un dizionario chiamato rubrica dove la chiave è il nome e il valore è un altro dizionario fatto da tutti i dati del singolo utente estratti dalla lista della singola riga del file 

                rubrica[nome] = {
                    "giorno": int(parti[1]),
                    "mese": parti[2],
                    "anno": int(parti[3]),
                    "età": int(parti[4]),
                    "sesso": parti[5],
                    "mail": parti[6]
                }

        return cls(rubrica)    #Ritorniamo il dizionario come una nuova istanza della classe, popolato con i dati estratti 


    #FUnzione per aggiungere un contatto: Permette di inserire un nuovo contatto nella rubrica. Se il nome inserito esiste già, ne sovrascrive i dati aggiornandolo.
    def aggiungi(self, nome, dati):     #Va a lavorare sulla singola istanza e prende in input il nome del contatto da aggiungere e i suoi dati

        if not self.aperta:   #Questo if serve per controllare se la rubrica è chiusa, se lo è allora stampa un messaggio di errore e ferma l'operazione 
            print("Prima apri una rubrica")
            return

        self.contatti[nome] = dati    #Se invece la rubrica è aperta allora aggiunge il contatto al singolo oggetto usando l'attributo .contatti applicato a self 

    #Cerca un contatto specifico tramite il suo nome e lo elimina definitivamente dalla rubrica in memoria
    def rimuovi(self, nome):   #Prende in input il singolo oggetto (la rubrica tot) è sapendo il nome del contatto da eliminare lo elimina

        if len(self.contatti) == 0:   #Controlla se l'oggetto rubrica dato in input è vuoto, se lo è manda un messaggio e esce dalla funzione 
            print("La rubrica è vuota")
            return

        if nome not in self.contatti:      #Se il nome passato in input non è all'interno della rubrica allora stampa un messaggio e esce 
            print("Il contatto", nome, "non esiste in rubrica")
            return

        del self.contatti[nome]     #Se invece non entra nei due input (quindi non è uscito dalla funzione) usa del per rimovere quella chiave (con il suo valore) dal dizionario della rubrica

    #Prende tutti i contatti attualmente in memoria e li scrive su un file nel computer per non perderli (in base all'estensione del file passato in ingresso capisce se si vuole salvare in fule json o un file testo)
    def salva(self, nome_file):         #Agisce sulla singola istanza della classe e prende in input questa istanza per salvarla 

        if len(self.contatti) == 0:    #Se la lunghezza della rubrica è zero allora ci comunica che la rubrica è vuota e quindi esce dalla funzione 
            print("La rubrica è vuota")
            return

        #A questo punto usando .endswith controlla se il nome del file finisce con .json o .txt quindi se vogliamo salvarla come file json o file testo
        if nome_file.endswith(".json"):   #Se finisce con .json 

            with open(nome_file, "w", encoding="utf-8") as file:        #Apre il file in modalità scrittura (se esiste  lo crea se no lo sovrascrive)
                json.dump(self.contatti, file, indent=4)        #Usando json.dump andiamo a convertire il dizionario self.contatti in un file json. Indent = 4 serve a inserire spazi per rendere il file ben impaginato 

        elif nome_file.endswith(".txt"):  #Altrimenti se finisce con .txt apriamo il file sempre in modalità scrittura 

            with open(nome_file, "w", encoding="utf-8") as file:

                for nome, dati in self.contatti.items():        #Scorriamo l'oggetto dato in input (dizionario) guardando le coppie chiave-valore (usando .items) e salviamo tutto in un file usando .write e la concatenazione di stringhe 

                    file.write(
                        nome + ";" +
                        str(dati["giorno"]) + ";" +
                        dati["mese"] + ";" +
                        str(dati["anno"]) + ";" +
                        str(dati["età"]) + ";" +
                        dati["sesso"] + ";" +
                        dati["mail"] + "\n"
                    )

    #Cerca un contatto specifico e stampa a schermo (sul terminale/console) tutti i suoi dettagli in modo ordinato e leggibile.
    def stampa(self, nome):    #Prendiamo in input la singola istanza (perchè c'è self) e il nome del contatto da stampare 

        if len(self.contatti) == 0:   #Di nuovo verifichiamo se la lunghezza dell'oggetto è nulla e in tal caso usciamo dalla funzione stampando un messaggio di errore 
            print("La rubrica è vuota")
            return

        if nome not in self.contatti:     #Se il nome non è all'interno della rubrica mandiamo un messaggio a video e chiudiamo la funzione 
            print("Il contatto", nome,"non esiste in rubrica")
            return

        #Se invece il nome è presente nella rubrica allora stampiamo il nome e poi tutti i relativi dati scorrendo il dizionario 

        for chiave, valore in self.contatti[nome].items():
            print(chiave, ":", valore)