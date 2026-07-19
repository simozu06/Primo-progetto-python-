'''
File: E4.py   

Author: Simone Zuppa   

Date: 2026/07/14 

Version: 1.0   

Description: Esportazione e importazione di dati di una rubrica di contatti. Il programma 
gestisce il salvataggio dei dati sia in un file di testo piano (.txt) formattato con valori 
separati da virgole, sia in un file strutturato (.json) tramite l'omonimo modulo, includendo 
la successiva rilettura e visualizzazione formattata a schermo del file JSON generato. 
'''
#Importiamo il modulo json (insieme di righe di codice già scritto) necessario per questo esercizio per salvare e leggere dati in formato json
   
import json 

rubrica = {
    'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 89, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
    'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 43, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
    'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona@email.com'},
    'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka@email.com'}
}

#Punto 1: Partendo dall’esercizio 3, aggiungete una opzione al programma per generare un file di testo 
#rubrica.txt contenente tutti gli elmenti della rubrica, uno per linea, con tutte le informazioni separate da virgole. 

#Apriamo (in questo caso lo creiamo anche perchè non esiste) il file rubrica.txt in modalità scrittura (w = write) e 
#lo chiamiamo file_txt. Il with serve a chiudere automaticamente il file alla fine

with open("rubrica.txt", "w") as file_txt:
    for nome, dati in rubrica.items():    #Scorriamo tutti gli elementi del dizionario rubrica 
        file_txt.write(                   #Serve a scrivere una riga nel file. Questa riga verrà scritta come è stato richiesto con tutte le informazioni relative a un utente separate da virgola 
            f"{nome}, "                     
            f"{dati['giorno']}, "         #Per estrarre un valore di una chiave di un dizionario si usa la sintassi dati['nome della chiave']
            f"{dati['mese']}, "
            f"{dati['anno']}, "
            f"{dati['età']}, "
            f"{dati['sesso']}, "
            f"{dati['mail']}\n"      #Qua è presente il carattere \n per andare a capo 
        )

#Punto 2: Create un file JSON che contiene la rubrica con la stessa struttura del dizionario interno al programma
#In maniera analoga a prima apriamo un file rubrica.json in mmodalità scrittura perchè vogliamo scriverci all'interno
with open("rubrica.json", "w") as file_json:
    #tramite .dump salviamo l'oggetto rubrica (ovvero un dizionario) nell'oggetto file_json (file json). Questo salvataggio viene fatto esattamente nel formato del dizionario (come richiesto)
    json.dump(rubrica, file_json)

#Punto 3: Leggete la rubrica salvata in un file formato JSON e visualizzate tutto il contenuto
#Nel punto 2 è stato aperto il file_json per scriverci sopra e poi è stato chiuso perchè c'è with 
#Poi riapriamo lo stesso file json ma sta volta in modalità lettura ('r'). 

with open("rubrica.json", "r") as file_json:
    #tramite la funzione .load leggiamo il file_json e lo trasformiamo nuovamente in un dizionario python (tutto ciò viene salavato in rubrica_letta)
    rubrica_letta = json.load(file_json)

#A questo punto abbiamo il dizionario chiamato rubrica_letta é quello che facciamo e scorriamo il dizionario 
#tramite due cicli. Uno esterno che gira sul dizionario esterno (dove il nome é la chiave e il valore della chiave è un altro dizionario)
#uno interno che gira sui dati relativi al nome, ovvero il dizionario interno, (e stampa la chiave e affianco il valore della chiave)
for nome, dati in rubrica_letta.items():
    print(nome)

    for chiave, valore in dati.items():
        print(f"{chiave}: {valore}")
        
    print()    #Questo print serve a lasciare una riga vuota tra un nome e l'altro
