# Programmeringsteknik webbkurs KTH inlämningsuppgift 1.
# Adam Mirza
# 9/10 - 2017
# Programmet ska uifrån ett angivet fyrsiffrigt tal beräkna hur många iterationer det krävs innan processen/mitt program kommer till talet/värdet 6174


print("Vad är ditt fyrsiffriga tal?: ")
tal = int(input())                          # Användaren anger sitt fyrsiffriga tal

# (lägg till om behövs?) if ValueError:
    # print('ange ett korrektfyrsiffriga tal')
#   else:

i = 0                                        # Skapar ett tal för att ange hur många gånger kaprekar regeln genomförs
while tal != 6174:
    x = str(tal)                              #Anger värdet inuti x

    #ifall numret som har angetts i input är en siffra midre anges en nolla ex: 821 blir 0821)
    if (len(str(tal)) < 4):
        y = int(tal)
        tal = ('%04d' % y) #sätter en nolla framför det tresiffriga värdet
        x = str(tal)

    STOR = int("".join(sorted(x, reverse=True)))   #Talet som har angets av användaren gås nu igenom och sorteras
    LITEN = int("".join(sorted(x)))                 #Talet som har angets av användaren gås nu igenom och sorteras
    tal = STOR - LITEN                              #Eftersom KAPREKAR regeln vill att man tar det största talet minus det minsta.. Därefter tas summan som en del till nästa varv om inte summan har kommit till värdet 6174
    print(STOR, '-', LITEN, '=', tal)
    i += 1       # varje varv som funktionen gås igenom tills den når slutsumman 6174 gör vi genom att ange i  +1 varv
    continue

print("KAPREKAR regeln gicks igenom", i, "gånger innan värder blev", tal)






