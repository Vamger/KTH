# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# Adam Mirza
# 29/10 - 2017
# Detta program stimulerar ett verklighetsbaserat Tivoli där användaren får skriva och därmed välja sig igenom tivolit

from random import *


class Tivoli(object): #Först måste vi skapa objekt som senare kan användas för att stimulera attraktionerna
    def __init__(self, regelsatt_langd, regelsatt_alder, val_av_attraktion, beskrivning, ak_ljudet, haveri_siffra):
        self.regelsatt_langd = regelsatt_langd  #Ett längdobjekt för att sen räkna ut om användarens längd följer attraktionens längdlimit
        self.regelsatt_alder = regelsatt_alder  #Ett ålderobjekt för att sen räkna ut om användarens ålder följer attraktionens åldersgräns
        self.val_av_attraktion = val_av_attraktion #Ett objekt som kommer användas för att hjälpa oss att navigera vilken attraktion användaren vill gå till
        self.beskrivning = beskrivning              #Ett objekt som används för att hjälpa oss att förtydliga beskrivning av attraktionerna för användaren
        self.ak_ljudet = ak_ljudet                  #Attraktionens regelsatta ålder/längdvärden, denna låter användaren åka attraktionen
        self.haveri_siffra = haveri_siffra          #Ett objekt som används när haveriet har "skapat" ett siffervärde som kommer att jämföras med attraktionens värde för att bestämma om attraktionen är ur funktion eller inte

    def haveri(self):
    # Denna funktion kommer fram till ett haverivärde, dvs en siffra som den sen jänför med attraktionens värde
    # Om haverisiffran är större än attraktionens värde går attraktionen ur funktion
    # om haverisiffran är mindre än attraktionens värde fortsätter funktionen och undersäker användarens längd och ålder
        haveriuppstar = randrange(1,11)
        if haveriuppstar <= self.haveri_siffra:
            print('Atttraktionen har gått ur funktion')
        else:
            self.vardera_langd_och_alder()

    def vardera_langd_och_alder(self):
    # Denna funktion värderar användarens ålder  och längd. Om användaren inte är i rätt ålder eller längd
    # kommer användaren att "kickas ut" från attraktionen
        anvandarens_langd = int(input('hur lång är du?: '))
        anvandarens_alder = int(input('Hur gammal är du?: '))
        if anvandarens_langd < self.regelsatt_langd:
            print('du är för kort för att åka denna attraktion')
        elif anvandarens_alder < self.regelsatt_alder:
            print('du är tyvärr för ung för att åka denna atttraktion')
        else:
            print(self.ak_ljudet)


def mainprogram():

    # Denna funktion lagrar samtliga attraktioners ålder, längd, namn på attraktionen och resterande information
    # Vi har nu skat ett objekt alla def kan jämföra sig med
    alla_attraktioner = [Tivoli(130,11,"BergOdalbanan","Allting kommer att gå så snabbt!", "Woooooosh!",3),Tivoli(110,12,"Mörka Tunneln", "Läskigt!", "Buuuuuuh!",2),Tivoli(140,14,"Katapulten", "Upp och ner!", "Whiiii!",4)]

#While True <----- försökte att lägga in kommandon för att få hela funktionen att fortsätta om användaren skriver ett nummer eller siffra som inte följer efter vårt programs valalternativ
    #try:
    ditt_val = int(input('Välj en attraktion: \n' + "1.BergOdalbanan\n" + "2.Mörka Tunneln\n" + "3.Katapulten\n" + "4.Dra hem\n"))
    if ditt_val in range (1,4):
        # Programmet körs även när användaren väljer en attraktion
        # Vi har efter denna mening nu skapat övriga alternativ när användaren väljer sig fram till en attraktion
        while ditt_val in range(1,4):
            print(alla_attraktioner[ditt_val-1].val_av_attraktion + "- Ditt nästa val?")
            ditt_val2 = int(input("1.Se besökarnas favoritcitat om attraktionen :)\n" + "2.Åk\n" + "3.Gå tillbaka\n"))
            while ditt_val2 == 1:
                print(alla_attraktioner[ditt_val-1].beskrivning + "\n")
                break
            if ditt_val2 == 2:
                # Här använder vi oss av haverifunktionen ännu en gång och därefter om användarens längd samt ålder stämmer bra
                alla_attraktioner[ditt_val-1].haveri()
            elif ditt_val2 == 3:
                ditt_val = int(input("Välj din attraktion: \n" + "1.BergOdalbanan\n" + "2.Mörka Tunneln\n" + "3.Slänggungan\n" + "4.Dra hem\n"))
                if ditt_val == 4:
                    print("Ha en fantastisk fortsättning!")
                    break
        #Except ValueError:
        #print("Ange ett korrekt kommando")
        #break? <--------- fick inte detta att fungera :(. ville strukturera programmet på detta sätt istället för att valalternativen dyker upp igen om användaren skriver ett inkorrekt alternativ

    # Om användaren vill dra hem kommer nedståended print text att skrivas ut och programmet kommer därefter att stängas av
    else:
        print("Ha en fin fortsättning!")


# Kommandot som används för att köra vårt mainprogram som använder sig utav haveri samt vardera längd och ålder funktionerna
mainprogram()


