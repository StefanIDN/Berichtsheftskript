import datetime
import locale

try:
    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8') #Setzt die Wochentage auf Deutsch
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'de_DE')

heute = datetime.datetime.now() #Das heutige Datum wird ausgelesen
weekday = heute.strftime("%u") #Der Wochentag als Zahl zum Vergleichen


def Generator(heute1):
    KW = heute1.isocalendar()[1] #Für die Kalenderwoche 
    Abteilung = int(input("Welche Abteilung?\n 1 = Infra\n 2 = Schule\n 3 = ELIT\n")) #Abfrage welche Abteilung
    if Abteilung == 1:
        abteilungname = "Infrastruktur"
    elif Abteilung == 2:
        abteilungname = "Schule"
    else:
        abteilungname = "ELIT"

    a = f"{heute1.strftime("%B")} {heute1.year} KW {KW}\n" #Erste Zeile mit dem Monat, Jahr und die Kalenderwoche

    f=open("output.txt","a")# öffne neue txt und a = append (einfügen)

    print(a, file=f)
    print(f"Abteilung: {abteilungname}\n", file=f)
    
    i=0

    while i < 5:
        Tag = heute1 + datetime.timedelta(days=i) # heutige Datum + x Tage
        print(Tag.strftime("%a"), Tag.strftime("%d.%m.%Y"), file=f)# Erst die Abkürzung vom Wochentag; dann den Tag,Monat und das Jahr von dem jeweiligen Tag; print in eine neue txt
        print(">", file=f)

        i=i+1
        

    print("\n", file=f)

    f.close()






k = int(weekday)-1 #in K kommt die Zahl vom Wochentag minus 1
Montag = heute - datetime.timedelta(days=k)#heutige Datum minus die anzahl der Tage von k
Generator(Montag)
weekday = 1






