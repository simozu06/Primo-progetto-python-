
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

for riga in lista_righe: 
    if (len(riga) > 0): 
        contatore_righe = contatore_righe + 1

print (contatore_righe)

#Seconda parte: contare il numero di parole 

testo.split ()        #Divido la stringa ogni volta che si incontra uno spazio 
lista_parole = testo.split ()     #Creo una lista dove ogni elemento sarà una parola 
contatore_parole = 0 

for parole in lista_parole: 
    if (len(parole) > 0): 
        contatore_parole = contatore_parole + 1

print(contatore_parole)

#Terza parte: contare i caratteri alfanumerici

testo_lista = list(testo)
print (testo_lista)

alfanumerici='abcdef'
carattere = 'a'
carattere in alfanumerici #vedere se c'è a nella lista alafnumerici 
