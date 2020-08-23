# Programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# Adam Mirza
# 19/10 - 2017
# Programmet skapar en dikt på fyra inlästa meningar användaren skriver in och ska följa en viss struktur


def display():
    print('DIKTAUTOMATEN\n') #Rubrikstext för att få användaren att veta vad för program han/hon kör
    print('Skriv in fyra meningar och få ut en rondelet\n')  #Förklaring på vad användaren ska göra


def poem(sentence): #Denna funktions syfte är att skapa fyra meningar användaren skriver in,
    n = 0           # Funktionen körs tills användaren har skrivit fyra meningar
    while n < 4 :   # Såväl antal meningar är mindre än fyra
        sentence[n] = input('skriv mening nr ' + str(n+1) + ' : ')
        n += 1      #Meningarna ökar alltid med +1 tills totalsumman blir 4. Då kan användaren inte skriva fler meningar
    return sentence #Vi kommer vilja fortsätta använda attributen "sentence" till resterande funktioner


def big(sentence):  #Denna funktion kommer använda dom fyra första orden på den första meningen och göra dom i stora
    header = sentence[0].split()
    print('\n')
    for word in header[:4]:
        header = print("".join(word.upper()), end=" ")
    return header   #Vi vill använda attributen "header" för resterande funktioner

#Denna funktion kommer att skriva ut hela dikten efter uppgiftsbeskrivningens regler
#Huvudsyftet med denna funktion är att lagra meningarna one, two, three och four för att senare använda dom systematiskt efter uppgiftsreglern


def structure(sentence):
    one = sentence[0].split()
    two = sentence[1].split()
    three = sentence[2].split()
    four = sentence[3].split()
    for word in one[:4]:
        print("".join(word), end=" ")
    print('')

    # Ifall mening nr ett (one) inte har tillräckligt många ord beordrar denna funktion att inte skriva tomma rader
    if len(one) > 4:
        for word in one[4:]:
            print("".join(word), end=" ")
        print('')
    for word in one[:4]:
        print("".join(word), end=" ")
    print('')
    # Samma sak som funktionen ovan bara att vi vill sätta regelsatsen i mening 2 (two), 3 (three) och 4 four
    if len(two) > 0:
        print(" ".join(two))
    if len(three) > 0:
        print(" ".join(three))
    if len(four) > 0:
        print(" ".join(four))
    for word in one[:4]: #Detta kommando behövs för att ordna dom fyra första orden sist i "poem"/dikt listan också
        print("".join(word), end=" ")
    print('')
    return one, two, three, four

# Detta är själva mainprogram som ska köra samtliga program.
# Eftersom vi vill köra alla funktioner i ett kommando, det vill säga main()


def main():
    sentence = 4*[None]
    display()
    poem(sentence)
    big(sentence)
    print('\n')
    structure(sentence)

#Här utförs kommandot "main" som ska köra alla funktioner i ett kommando
#Eftersom dom är kumpade ihop till funktionsatsen main()
main()
















