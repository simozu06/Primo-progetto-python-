#La prima cosa che facciamo è importare i moduli necessari 
import random       #Importa il modulo per generare numeri casuali
import sympy as sp      #Carica la libreria per il calcolo simbolico. Inoltre usando 'as' usiamo un acronimo di sympy per ridurre il codice 
import time     #Modulo necessario per gestire il tempo e contare i 20 secondi 

#Definiamo la funzione per generare in maniera casuale un quiz su una domanda aritmetica, un calcolo di una derivivata o un calcolo di un integrale da risolvere 
def generatore_domande():   #volta per volta questo genererà casualmente una domanda aritmetica, sulla derivata o sugli integrali
    simboli = sp.symbols('x y')  # Restituisce la tupla (x, y). Nota) La funzione symbols permette di definire più simboli contemporaneamente passandoli come una singola stringa separata da spazi
    x = simboli[0]               # Estrae il primo elemento
    y = simboli[1]               # Estrae il secondo elemento
    tipi_domanda = ['aritmetica', 'derivata', 'integrale']    #Abbiamo una lista dove all'interno ci sono delle stringhe che decidono in maniera poi casuale il tipo di domanda
    operatori = ['+', '-', '*']     #Definisce gli operatori che si possono usare nell'operazione
    
    while True:     #Avviamo un loop infinito che finisce solo se vi è il break 

        # Scegliamo a caso che tipo di domanda fare a questo giro
        tipo = random.choice(tipi_domanda)
        
        #costruiamo la domanda in base al tipo di domanda che è stato generato

        if tipo == 'aritmetica':        #domanda aritmetica
            #Generiamo in maniera casuale l'operatore (+, - o *) e due numeri interi tra 1 e 10 (.randint) che saranno i moltiplicatori di x e y usando l'oggetto random con i metodi .choice (estrae casualmente da una lista) e .randint
            op = random.choice(operatori)       
            coeff_x = random.randint(1, 10)
            coeff_y = random.randint(1, 10)
        
            #A questo punto in base all'operatore vado a definire un espressione diversa 
            if op == '+':
                expr = coeff_x * x + coeff_y * y
            elif op == '-':
                expr = coeff_x * x - coeff_y * y
            else:
                expr = coeff_x * x * coeff_y * y
        
            #A questo punto generiamo altri due valori casuali da 1 a 5 sempre usando random.randint
            #Questi numeri saranno i valori della x e della y da sostituire nell'espressione creata precedentemente 
            val_x = random.randint(1, 5)
            val_y = random.randint(1, 5)
        
            #A questo punto usando il dizionario {x: val_x, y: val_y} usiamo il metodo .subs() che sostituisce i valori della x e della y generati casualmenye nell'espressione (expr)
            risultato_esatto = expr.subs({x: val_x, y: val_y})      #Sostituendo i valori esatti di x e y troveremo il risultato corretto dell'espressione e lo salviamo in una variabile 
        
            #Facciamo la domanda e chiediamo all'utente di calcolare il valore dell'espressione 
            testo_domanda = f"Calcola il valore di '{expr}' sapendo che x={val_x} e y={val_y}: "
            yield testo_domanda, int(risultato_esatto)      #A questo punto usiamo yield perchè vogliamo bloccare la funzione dopo una domanda e passare alla successiva solo dopo che l'utente ha risposto 
            #Quello che ci restituisce la funzione volta per volta: la domanda generata e il risultato della domanda convertito in intero 

        elif tipo == 'derivata':        #il tipo di domanda fa una domanda sul calcolo di una derivata in un punto
            # Creiamo un polinomio semplice: a*x**2 + b*x
            coeff_a = random.randint(1, 5)      #Generiamo in maniera casuale il coefficente a da 1 a 5 di a x^2
            coeff_b = random.randint(1, 10)     #Generiamo il coefficente b per il termine lineare x
            expr = coeff_a * (x**2) + coeff_b * x       #Scriviamo l'espressione dopo aver generato casualmente i coefficenti
            
            # Calcoliamo la derivata prima rispetto a x con sp.diff(). Questo è un metodo della libreria sympy che calcola la derivata prima di un espressione rispetto alla variabile x
            derivata = sp.diff(expr, x)
            
            # Scegliamo un punto x in maniera casuale di dove calcolare la derivata 
            val_x = random.randint(1, 5) 
            
            # Sostituiamo il valore di x nella derivata (che sarà un'altra espressione diversa dall'originale) e troviamo il risultato_esatto
            risultato_esatto = derivata.subs({x: val_x})    #sostituiamo sempre usando .subs
            
            testo_domanda = f"Calcola il valore della DERIVATA di '{expr}' nel punto x={val_x}: "       #Scriviamo il testo della domanda per chiedere la derivata di un espressione in un certo valore x 
            yield testo_domanda, int(risultato_esatto)      #Restituiamo come prima il testo della domanda e il suo risultato 

        elif tipo == 'integrale':       #l'ultimo tipo di domanda è l'integrale 
            #Generiamo in maniera casuale il coefficente della nostra espressione polinomiale
            coeff_a = random.randint(1, 5)
            #L'espressione di cui chiederemo l'integrale è a * x (tuttavia aggiungiamo un per 2 così da evitare frazioni quando calcoliamo l'integrale di x)
            expr = (coeff_a * 2) * x
            # Estremi di integrazione da 0 a val_b (generati casualmente)
            val_b = random.randint(1, 3)
            
            # Integriamo l'espressione rispetto a x, da val_a a val_b con sp.integrate()
            risultato_esatto = sp.integrate(expr, (x, 0, val_b))
            
            testo_domanda = f"Calcola l'INTEGRALE definito di '{expr}' tra 0 e {val_b}: "       #Generiamo il testo della domanda
            yield testo_domanda, int(risultato_esatto)      #restituiamo come tutte le altre il testo della domanda e il suo risultato

#A questo punto passiamo alla funzione principale che sarà quella che manderà a video la domanda e valuterà la risposta dell'utente 
def gioca_a_tempo():
     #Prima di tutto mostriamo a video le regole del gioco
    print("Benvenuto al Quiz Matematico SPEEDRUN!")
    print("Hai esattamente 60 secondi per rispondere al maggior numero di domande.")
    print("Regole: +1 punto per ogni risposta esatta, -1 punto se sbagli o inserisci lettere.")
    
    # Usiamo questa particolare espressione input() che mette in pausa il codice fino a che l'utente non preme INVIO
    input("\nPremi INVIO quando sei pronto a far partire il timer...")
    
    punteggio = 0       #Azzeriamo il punteggio 
    tempo_limite = 60       #Impostiamo il tempo limite 
    domande = generatore_domande()      #questa riga non restituisce subito i risultati, ma crea un oggetto generatore "congelato" e pronto all'uso
    
    # Facciamo partire il timer 
    inizio_timer = time.time()
    
    for domanda, risposta_corretta in domande:      #A questo punto fa girare un ciclo for. Questo serve a 'svegliare' il generatore chiedendogli il primo risultato per il primo ciclo del for, il secondo risultato per il secondo ciclo e via dicendo.
        #La tupla generata dal generatore verrà spacchettata ssegnando il testo a domanda e il numero a risposta_corretta.
        # Controllo se il tempo è scaduto prima di fare la domanda. Se è finito esco dal for 
        if time.time() - inizio_timer >= tempo_limite:
            break
            
        risposta_utente = input(domanda)        #Anche in questo caso uso input() per bloccare completamente il codice fino a che non inserisco la risposta alla domanda (la variabile domanda è il risultato del genratore che ha il testo della domanda)
        
        # Controllo se il tempo è scaduto MENTRE l'utente rispondeva (lo controllo dopo perchè con input() ho fermato il tempo, che potrebbe essere scaduto nel mentre che l'utente pensava) 
        if time.time() - inizio_timer >= tempo_limite:
            print("\nTempo scaduto! Questa risposta non viene conteggiata.")
            break
            
        # Gestione punteggio ed errori tramite EAFP (se il tempo non è ancora scaduto)
        try:        #Usiamo un try per gestire il seguente errore: l'utente non ha inserito un numero intero quindi il casting a int() genera errore e si va a expect valuerror 
            risposta_numerica = int(risposta_utente)        #Se il casting a int() della risposta data non genera errore allora si controlla se la risposta è corretta 
            
            if risposta_numerica == risposta_corretta:      #Se la risposta data coincide con il risultato (secondo output del generatore) allora il punteggio aumenta di 1 se no diminuisce
                print("Corretto! +1\n")
                punteggio += 1
            else:
                print(f"Sbagliato! La risposta corretta era {risposta_corretta}. -1\n")
                punteggio -= 1
                
        except ValueError:      #Gestiamo l'errore: se l'utente non ha inserito un numero intero allora contiamo la risposta come errata e gli togliamo un punto (ricordandogli di inserire solo numeri interi)
            print("Errore: devi inserire un numero intero! Penalità: -1\n")
            punteggio -= 1

    #A questo punto sono uscito dal for (vuol dire che il tempo è scaduto quindi è stato eseguito il break)
    # Fine del gioco e mandiamo a video il risultato finale 
    print("\n--- GIOCO TERMINATO ---")
    print(f"Il tuo punteggio finale è: {punteggio} punti.")

#Chiamiamo la funzione per giocare 
gioca_a_tempo()