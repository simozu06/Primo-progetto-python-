#Nota generale) in questo esercizio bisogna stare molto attenti alla formattazione delle stringhe 
#per garantire che vangano stampate nel modo corretto (con tutti gli apici e le virgole corrette)
#Nota generale 2) per attivare uno dei punti nel terminale si scrive python E3.py --punto 1 (per attivare il punto 1)


#Stiamo dicendo a Python di portare dentro gli attrezzi necessari per leggere i comandi 
#dal terminale.
import argparse

# Definizione del dizionario fornito
rubrica = {
    'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
    'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
    'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
    'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

# Impostiamo subito argparse per gestire tutti i punti dell'esercizio tramite opzioni
parser = argparse.ArgumentParser()       #creiamo l'oggetto che ascolterà ciò che viene scritto nel terminale 
parser.add_argument('--punto1', action='store_true', help="Esegue il punto 1")
parser.add_argument('--lista_ordinata', action='store_true', help="Esegue il punto 2")
parser.add_argument('--punto3', action='store_true', help="Esegue il punto 3")
parser.add_argument('--punto4', action='store_true', help="Esegue il punto 4")
parser.add_argument('--chiave', type=str, help="Esegue il punto 5 (inserire la chiave)")
parser.add_argument('--nome', type=str, help="Esegue il punto 6 (inserire il nome)")

#Spiegazione: stiamo andando a definire all'interno del modulo vuoto parser vari argomenti 
#Per i punti 1/2/3/4 usiamo action='store_true'. Questo significa che si comportano come 
#interruttori della luce: se scrivi --punto1 nel terminale, il suo valore diventa True (Acceso), e quindi viene eseguito
#Per i punti 5/6 usiamo type=str perchè ci aspettiamo che l'utente ci scriva anche una parola vicino
#Vi è poi per ogni parapetro la riga help, questo contiene la descrizione del parametro che stai creando.


#Questa riga legge tutto quello che l'utente ha scritto nel terminale e lo salva nella
#variabile args.
args = parser.parse_args()

#Punto 1: visualizzate il contenuto del dizionario stampando a schermo delle stringhe 
#formattate che contengano la chiave ed il valor di ognuno degli elementi
#(Esempio: ‘Paolino Paperino’, ‘giorno’ 9, ‘mese’ ‘giugno’, …)
if args.punto1:            #Se l'utente dal terminale ha attivato l'interruttore --punto1...

#tramite un for scorriamo il dizionario della rubrica e usando il metodo .items estraiama sia
#la chiave principale (quella in .nome) sia il suo valore (che in questo caso è un altro dizionario)
    for nome, dati in rubrica.items(): 
        stringa_finale = f"'{nome}'"        #Creiamo una stringa (con al formattazione f-string) inserendoci subito il nome
        for k, v in dati.items():           #Adesso scorriamo sul dizionario dei valori legati al nome sempre usando .items, k sarà la chiave (es.giorno) e v il valore (es.9)
            if type(v) == str:              #Questo if serve a vedere se il tipo del valore v è una stringa per in caso aggiungerla alla stringa finale con gli apici (se è un numero non avrà gli apici)
                stringa_finale = stringa_finale +  f", '{k}' '{v}'"    #Usiamo la concatenazione per aggiungere la coppia chiave-valore alla stringa 
            else:
                stringa_finale = stringa_finale +  f", '{k}' {v}"      #Altrimenti lo concateniamo ma senza apici sul valore (es. quando abbiamo un intero tipo 9)

        print(stringa_finale)     #Stampala stringa finale completa con tutto (nome, data, ecc.)


#Punto 2: A partire dalla rubrica, costruire la lista delle età, ordinata in ordine 
#crescente e visualizzate i nomi in ordine crescente di età

if args.lista_ordinata:       #Se l'utente nel terminale ha attivato lista_ordinata eseguiamo il punto 2
     
    #Prima di tutto estraiamo tutte le età dal dizionario principale e le mettiamo in una lista vuota 
    lista_eta = []
    for nome, dati in rubrica.items():
        #estraiamo dal singolo dizionarietto della persona il valore sotto la chiave dell'età usando appunto l'estrazione di un valore da un dizionario 
        #in questo caso dati è il dizionario e eta è la chiave del valore che vogliamo estrarre
        lista_eta.append(dati['età'])      #.append è un metodo delle liste per agganciare un valore 
    
    lista_eta.sort()    #Usiamo il metodo .sort delle liste che ordina dal più piccolo al più grande

    lista_nomi = []   #Questa sarà la lista dei nomi in modo che i nomi siano messi nell'ordine corretot in base alle età 
    for eta_cercata in lista_eta:        #Cerchiamo il nome corrispondente allìetà scorrendo la lista delle età già messa in ordine crescente 
        #Scorriamo il dizionario principale un nome alla volta e se il valore eta corrisponde con quella che 
        #stiamo cercando allora agganciamo il nome alla lista dei nomi
        for nome, dati in rubrica.items():
            if dati['età'] == eta_cercata:
                lista_nomi.append(nome)

    #stampiamo l'età e i nomi in maniera crescente e con i nomi messi in ordine corretto 
    print(f"Età ordinate: {lista_eta}")
    print(f"Nomi ordinati per età: {lista_nomi}")

#Punto3: Invertire l’ordine della lista precedentemente costruita e visualizzatela

if args.punto3:        #Se nel terminale viene digitato --punto 3 allora viene eseguita l'inversione delle liste
    #L'idea è creare la stessa lista ordinata in maniera crescente delle età e poi 
    #usare il metodo .reverse per invertire gli elementi di una lista

    #Prima di tutto estraiamo tutte le età dal dizionario principale e le mettiamo in una lista vuota 
    lista_eta = []
    for nome, dati in rubrica.items():
        #estraiamo dal singolo dizionarietto della persona il valore sotto la chiave dell'età usando appunto l'estrazione di un valore da un dizionario 
        #in questo caso dati è il dizionario e eta è la chiave del valore che vogliamo estrarre
        lista_eta.append(dati['età'])      #.append è un metodo delle liste per agganciare un valore 
    lista_eta.sort()
    lista_eta.reverse()
    print(f"Lista età invertita: {lista_eta}")

#Punto 4: Utilizzare la rubrica e scrivere su schermo per OGNI membro della rubrica, il seguente messaggio:
#Car[o/a] [Nome],
#sei nat[o/a] il [giorno] di [mese] del [anno] e quindi a breve compirai [età] anni.
#Ti manderemo gli auguri a [mail]'''
#dove [o/a] deve essere adattato all’attributo [M/F]

if args.punto4: 
    #In questo caso l'unico problema è la desinenza. Per risolvere tale problema andiamo a definire 
    #una stringa e in base al valore relativo alla chiave sesso del dizionario interno le attribuiamo o oppure a

    for nome, dati in rubrica.items():
        if dati['sesso'] == 'M':
            desinenza = 'o'
        else:
            desinenza = 'a'
            
        #Usiamo la formattazione f-string dove a variare sono tutte le cose tra parentesi graffe 
        #Ricordo: dire per esempio dati['anno'] vuol dire estrarre il valore corrispondnete alla chiave anno nel dizionario dati
        print(f"Car{desinenza} {nome},")
        print(f"sei nat{desinenza} il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni.")
        print(f"Ti manderemo gli auguri a {dati['mail']}\n")

#Punto 5: Utilizzando args passate in input al vostro programma una chiave [giorno, mese, anno, età, sesso,
#mail] e visualizzate tutto il contenuto della rubrica (valori) che corrispondono a questa chiave

##In questo caso per come abbiamo definito l'argomento chiave in argparse (essendo una stringa), nel
#terminale dopo --chiave ci si aspetta una stringa che va a indicare la chiave che vogliamo visualizzare
if args.chiave:     
    for nome, dati in rubrica.items():      #scorriamo la coppia chiave-valore(dizionarietto) nel dizionario principale
        #Questo if non è necessario ma semplicemente serve a verificare se la chiave inserita effettivamente è presente tra le chiavi del dizionario 
        if args.chiave in dati:
            print(f"{nome}: {dati[args.chiave]}")   #Se la chiave è presente stampiamo il nome della persona che stiamo visualizzando e affianco il valore della chiave scelta
        else:
            print(f"La chiave '{args.chiave}' non esiste per {nome}.")     #Altrimenti diciamo che la chiave non esiste per quella persona 


#Punto 6: Utilizzando argparse visualizzate la stringa al punto 4 SOLO per il nome fornito come opzione al vostro programma
#Anche in questo caso per come abbiamo definito --nome mi aspetterò una stringa dopo che corrisponderà al nome di cui stampare la stringa del punto 4 
#Nota generale sul punto 6) Nel terminale quando chiami questo if ricordati le doppie virgolette sul nome: esempio: python E3.py --nome "Paolino Paperino"
if args.nome:
    for nome, dati in rubrica.items():     #Scorriamo la coppia chiave-valore nel dizionario principale e 
        # Controlliamo se il nome corrisponde esattamente a quello inserito
        if nome == args.nome:
            if dati['sesso'] == 'M':       #dopo essere entrato nel primo if quindi aver trovato il nome cercato devo associare la desinenza o/a corretta 
                desinenza = 'o'
            else:
                desinenza = 'a'
                
            #Usiamo la formattazione f-string in maniera analoga al punto 4
            print(f"Car{desinenza} {nome},")
            print(f"sei nat{desinenza} il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni.")
            print(f"Ti manderemo gli auguri a {dati['mail']}\n")