'''
File: E2.py 

Author: Simone Zuppa 

Date: 2026/07/12 

Version: 1.0 

Description: Analisi testuale, manipolazione di stringhe e calcolo delle occorrenze su un estratto di una poesia. 
''' 

#Ricordo: per vedere i metodi di un certo oggetto si usa help(tipo dell'oggetto). Ad esempio help(str)

testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

#Prima parte: conto il numero di righe 

testo.split('\n')       #Divido la stringa in sottostringhe ogni volta che vai a capo, ovvero quando incontri \n
lista_righe = testo.split ('\n')   #Faccio una lista dove ogni elemento è una sottostringa del risultato della divisione fatta prima

contatore_righe = 0

#Tramite un for scorrò le righe del testo e per ogni riga non nulla aumento il contatore di uno

for riga in lista_righe: 
    if (len(riga) > 0): 
        contatore_righe = contatore_righe + 1

print (f"Il numero di righe nel testo è {contatore_righe}")

#Seconda parte: contare il numero di parole 

testo.split ()        #Divido la stringa ogni volta che si incontra uno spazio 
lista_parole = testo.split ()     #Creo una lista dove ogni elemento sarà una parola 
contatore_parole = 0 

#Anche in questo caso scorrò tramite un for ma sulle parole del testo e aumento di uno il contatore se la parola esiste, ovvero se la stringa chiamata parola non è vuota 
#Questo controllo in realtà non è così necessario in quanto usando testo.split() vado già a escludere caratteri di spaziatura, ma è un controllo di sicurezza
#Nota) la punteggiatura non viene contata perchè quando uso split la punteggiatura è assorbita nelle parole

for parole in lista_parole: 
    if (len(parole) > 0): 
        contatore_parole = contatore_parole + 1

print(f"Il numero di parole nel testo è {contatore_parole}")

#Terza parte: contare i caratteri alfanumerici

#L'idea è creare una stringa con all'interno tutti i caratteri alfanumerici (creata con concatenazione)
#Successivamente scorrere nel testo carattere per carattere e ogni volta che trovo un carattere appartenente 
#ad alfanumerici aumento il conatore di 1 

alfabeto_minuscolo = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_maiuscolo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeri = '0123456789'
alfanumerici = alfabeto_minuscolo + alfabeto_maiuscolo + numeri

contatore_alfanumerici = 0
for char in testo:
    if char in alfanumerici:
        contatore_alfanumerici = contatore_alfanumerici + 1
print(f"Il numero di caratteri alfanumerici nel testo è {contatore_alfanumerici}")

#Quarta parte: Chiedere all’utente una lettera e contate quante volte compare nel testo

#Qua l'idea è chiedere all'utente una lettera e scorrere il testo carattere per carattere e ogni volta 
#che troviamo quella lettera amentare il contatore di uno

lettera_utente = input("Inserisci una lettera: ")
contatore_lettera = 0
for char in testo:
    if char == lettera_utente:
        contatore_lettera = contatore_lettera + 1
print(f"Il numero di volte che compare la lettera scelta nel testo è {contatore_lettera}")

#Quinta parte: Sostituite tutte le parole day, water e about con la parola PYTHON in tutti i versi

#L'idea in questo caso è usare il meotodo .replace (in sostanza questo va a sostituire la prima
#parola indicata nelle parentesi con la seconda)
#Quindi elencando quelle che sono le parole da sostituire (escluse della virgola perchè il 
#metodo .replace sostituisce solo le lettere d-a-y) scorrò queste parole e ogni volta vado a 
#riscrivere il testo sostituendo alla parola considerata PYTHON 

# Partiamo dal testo originale completo
testo_sostituito = testo

parole_da_sostituire = ["day", "Day", "water", "Water", "about", "About"]

# Sostituiamo ogni parola dell'elenco con "PYTHON"
for parola in parole_da_sostituire:
    testo_sostituito = testo_sostituito.replace(parola, "PYTHON")

print(testo_sostituito)

#Sesta parte: Riscrivete il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo

# Inizializzo una stringa vuota che conterrà tutto il testo finale modificato
testo_dispari_maiuscolo = ""

# Ciclo principale: scorro la poesia riga per riga
for riga in lista_righe:
    
    # Divido la singola riga in una lista di parole usando gli spazi come separatori
    parole_riga = riga.split()
    
    # Inizializzo una stringa vuota per ricostruire la riga corrente
    nuova_riga = ""
    
    # Calcolo quante parole ci sono nella riga per poter scorrere i loro indici
    lunghezza_riga = len(parole_riga)
    
    # Ciclo interno: scorro gli indici numerici da 0 fino alla lunghezza della riga
    for i in range(lunghezza_riga):
        
        # Controllo se l'indice corrente è dispari (resto della divisione per 2 diverso da 0)
        if i % 2 != 0:
            # Se è dispari: accedo alla parola, la converto in maiuscolo e aggiungo uno spazio
            nuova_riga = nuova_riga + parole_riga[i].upper() + " "
        else:
            # Se è pari: prendo la parola originale così com'è e aggiungo uno spazio
            nuova_riga = nuova_riga + parole_riga[i] + " "
            
    # Finita la riga, la concateno al testo finale aggiungendo un ritorno a capo (\n)
    testo_dispari_maiuscolo = testo_dispari_maiuscolo + nuova_riga + "\n"

# Stampo il risultato finale
print(testo_dispari_maiuscolo)

#Settima parte: Riscrivere il testo invertendo l’ordine delle frasi dal basso all’alto.

#L'idea in questo caso è presa la riga i-esima del testo trovare la posizione corrispondente nella 
#quale va stampata (ovvero la posizione indice_inverso). A questo punto calcolata tale posizione 
#ristampo la riga ì-esima in questa posizione 


# Calcolo il numero totale di righe presenti nella lista creata all'inizio
lunghezza_righe = len(lista_righe)

# Uso un ciclo for per generare una sequenza di numeri (i) da 0 fino alla lunghezza totale
for i in range(lunghezza_righe):
    
    # Calcolo l'indice inverso:
    # 'lunghezza_righe - 1' è l'indice dell'ultimissima riga.
    # Sottraendo 'i', mi sposto progressivamente verso l'inizio della lista ad ogni giro.
    indice_inverso = lunghezza_righe - 1 - i
    
    # Controllo di sicurezza: verifico che la riga non sia completamente vuota
    # (per evitare di stampare spazi bianchi inutili)
    if len(lista_righe[indice_inverso]) > 0:
        
        # Stampo la riga corrispondente all'indice calcolato
        print(lista_righe[indice_inverso])

#Ottava parte: Riscrivete il testo in modo che il secondo verso di ogni strofa sia scritto a specchio 
#(cioè al contrario carattere per carattere: Ad esempio, questa frase’ –> ‘esarf atseuq ,oipmese dA’)

#L'idea qua è di scorrere riga per riga il nostro testo e tramite un contatore tener traccia del 
#verso in cui siamo. Se siamo nel secondo verso esattamente come abbiamo fatto prima per invertire 
#l'ordine delle righe invertiamo l'ordine dei caratteri andando a creare una stringa vuota e 
#concatenando a questa stringa prima l'ultimo carattere, poi il penultimo e via dicendo 

# Inizializzo un contatore per tenere traccia di quale verso stiamo leggendo all'interno della strofa
contatore_verso = 0

# Scorro la lista di tutte le righe del testo
for riga in lista_righe:
    
    # Se la riga è vuota (lunghezza 0), significa che c'è uno spazio tra due strofe
    if len(riga) == 0:
        # Azzero il contatore perché la strofa precedente è finita
        contatore_verso = 0
        
    else:
        # Se la riga contiene del testo, aumento il contatore dei versi di 1
        contatore_verso = contatore_verso + 1
        
        # Controllo se mi trovo esattamente sul secondo verso della strofa corrente
        if contatore_verso == 2:
            
            # Inizializzo una stringa vuota che conterrà il verso scritto al contrario
            riga_specchio = ""
            
            # Calcolo di quanti caratteri è composta la stringa
            lunghezza_verso = len(riga)
            
            # Ciclo for per scorrere gli indici numerici dei caratteri
            for i in range(lunghezza_verso):
                # Calcolo l'indice inverso e concateno il carattere alla nuova stringa.
                # Parto dall'ultimo carattere (lunghezza_verso - 1) e vado a ritroso sottraendo 'i'
                riga_specchio = riga_specchio + riga[lunghezza_verso - 1 - i]
                
            # Stampo il verso capovolto
            print(riga_specchio)
            
        else:
            # Se non è il secondo verso (è il 1°, 3°, 4° ecc.), lo stampo normalmente così com'è
            print(riga)

#Nona parte: Trovate eventuali parole che compaiono in tutte le strofe

#L'idea generale è creare una variabile booleana, inizializzata a true, e scorrendo le parole della 
#prima strofa verificare se la parola è presente anche in utte le altre, se è presente la variabile
#bolleana rimarrà a ture quindi inserirò la mia parola nella lista 

#Divido l'intero testo in strofe usando il doppio ritorno a capo come separatore
strofe = testo.split('\n\n')
#Quindi avremo che strofe [0] è la prima strofa, strofe [1] è la seconda e via dicendo 

# Inizializzo una LISTA vuota che conterrà le parole presenti in tutte le strofe
lista_parole_comuni = []

#Divido la prima strofa parola per parola usando lo spazio come separatore 
#Queste faranno da "campione": se una parola è in tutte le strofe, DEVE essere anche nella prima.
parole_prima_strofa = strofe[0].split()
    
#Scorro una per una le parole della prima strofa
for parola in parole_prima_strofa:
        
    # Inizializzo la variabile booleana (il nostro flag).
    # Parto dal presupposto (ottimistico) che la parola sia presente ovunque.
    presente_ovunque = True
        
    #Scorro le ALTRE strofe (partendo dall'indice 1 fino alla lunghezza totale)
    for i in range(1, len(strofe)):
            
        # Divido anche la strofa corrente in parole (per evitare falsi positivi,
        # ad esempio cercare "in" e trovarlo nascosto dentro la parola "shrink")
        parole_altra_strofa = strofe[i].split()        #strofe[i] è l'i-esima strofa del testo
            
        #Verifico se la parola NON è presente in questa strofa
        if parola not in parole_altra_strofa:
            # Se non c'è, la mia ipotesi ottimistica crolla: la variabile booleana diventa false
            presente_ovunque = False
                
    #Fuori dal ciclo interno, controllo lo stato finale della variabile di controllo.
    #Se è rimasta True 
    #E se la parola NON è già stata aggiunta alla lista finale (per evitare doppioni)
    #Allora la devo inserire nelle parole presenti in tutte le strofe
    if presente_ovunque == True and parola not in lista_parole_comuni:
        lista_parole_comuni.append(parola)

# Se la lista ha almeno un elemento (quindi non è vuota)
if len(lista_parole_comuni) > 0:
    print(f"Le parole presenti in tutte le strofe sono: {lista_parole_comuni}")
# Altrimenti (la lista è vuota)
else:
    print("Non ci sono parole comuni in tutte le strofe.")


#Decimo punto: Create la lista univoca di tutte le parole che compaiono nel testo, ordinatela per lunghezza delle parole e visualizzatela

#L'idea è partire dalla lista di parole del testo già precedentemente creata con il metodo .split
#A questo punto creo un set dove i suoi elementi sono le parole del testo, quindi lo creo a partire 
#dalla lista. Questo lo faccio in modo che elementi duplicati non compaiono due volte perchè il 
#set accetta solo elementi unici, quindi, i doppioni vengono eliminati automaticamente.

parole_uniche = set(lista_parole)

#Riconverto il set in una lista (solo che adesso i duplicati ci saranno solo una volta). Ciò
#lo faccio per i set non supportano i metodi di ordinamento perchè non hanno un ordine negli elementi 

lista_univoca = list(parole_uniche)

#Uso il metodo .sort che ordina gli elementi in questo caso di una lista avendo come key, ovvero, 
#la regola con cui ordinarli, la lunghezza dell'elemento, ovvero della parola
lista_univoca.sort(key=len)

print("La lista univoca ordinata per lunghezza è:")
print(lista_univoca)

#Undicesima punto: Create un dizionario che mappi OGNI carattere (chiave) con la sua occorrenza nel testo (valore) e visualizzatelo

# Inizializzo un dizionario vuoto usando le parentesi graffe. Questo contenitore ospiterà 
#i caratteri come chiavi e le frequenze/occorenze come valori.
occorrenze_caratteri = {}

# Scorro l'intera stringa del testo carattere per carattere (Nota: tutti i caratteri vengono visitati)
for char in testo:
    
    #Controllo se il carattere corrente è già presente tra le chiavi del dizionario, usando il 
    #metodo .keys() che ci fornisce l'elenco di tutte le chiavi inserite fino ad ora.
    if char in occorrenze_caratteri.keys():
        
        #Se il carattere è già una chiave, significa che lo avevamo già contato. Accedo al
        #suo valore attuale tramite le quadre e lo incremento di 1.
        occorrenze_caratteri[char] = occorrenze_caratteri[char] + 1
        
    else:
        #Se il carattere non è presente nelle chiavi, è la prima volta che lo incontriamo.
        #Creo una nuova coppia nel dizionario assegnando a questa nuova chiave il valore 1.
        occorrenze_caratteri[char] = 1

print("Mappa di tutte le occorrenze dei caratteri:")
print(occorrenze_caratteri)

#Dodicesimo punto: Create un dizionario come il precedente per i soli caratteri alfanumerici (no caratteri speciali), ignorando maiuscole e minuscole

#Partiamo dal dizionario creato al punto 11 (che contiene tutto, anche la punteggiatura)
#Inizialmente, inizializzo il nuovo dizionario pulito
occorrenze_alfanumerici = {}

#A questo punto scorro le COPPIE chiave-valore del dizionario vecchio usando il metodo .items()
#Questo metodo restituisce le coppie chiave-valore
for chiave, valore in occorrenze_caratteri.items():
    
    #FILTRO: Se la chiave è una lettera o un numero allora trasformo la chiave in minuscolo
    if chiave in alfanumerici:
        
        #Uso il metodo .lower() che trasforma i caratteri alfabetici, parliamo di stringhe, 
        #in minuscolo e non cambia i numeri 
        chiave_min = chiave.lower()
        
        #Cosa serve l'if..else? l'else crea la coppia nel dizionario la prima volta in assoluto che incontriamo una lettera,
        #mentre l'if scatta per sommare i valori solo quando troviamo la sua versione alternativa 
        #(maiuscola o minuscola) e dobbiamo fondere i due conteggi parziali sotto l'unica chiave minuscola
        #sommando le occorenze della lettera minuscola/maiuscola al valore della chiave nel primo dizionario
        #che avrà la lettera maiuscola/minuscola, nell'altra versione

        if chiave_min in occorrenze_alfanumerici.keys():
            occorrenze_alfanumerici[chiave_min] = occorrenze_alfanumerici[chiave_min] + valore
        # Se non c'è, creo la chiave e le assegno il valore
        else:
            occorrenze_alfanumerici[chiave_min] = valore
print("Mappa delle occorenze dei soli caratteri")
print(occorrenze_alfanumerici)