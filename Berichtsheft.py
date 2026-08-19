import datetime
import locale
import tkinter as tk
import os
import customtkinter as ctk


try:
    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8') #Setzt die Wochentage auf Deutsch
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'de_DE')

heute = datetime.datetime.now() #Das heutige Datum wird ausgelesen
weekday = heute.strftime("%u") #Der Wochentag als Zahl zum Vergleichen


def Generator(heute1,Abteilung):
    f=open("output.txt","w")# öffne neue txt und w = write (überschreiben)
    KW = heute1.isocalendar()[1] #Für die Kalenderwoche 
    
    if Abteilung == 1:
        abteilungname = "Infrastruktur"
    elif Abteilung == 2:
        abteilungname = "Schule"
    elif Abteilung == 3:
        abteilungname = "Infrastruktur"
    elif Abteilung == 4:
        abteilungname = "ELIT"
            

    a = f"{heute1.strftime("%B")} {heute1.year} KW {KW}\n" #Erste Zeile mit dem Monat, Jahr und die Kalenderwoche


    print(a, file=f)
    print(f"Abteilung: {abteilungname}\n", file=f)

    i=0
    if Abteilung == 1 or Abteilung == 4:
        while i < 5:
            Tag = heute1 + datetime.timedelta(days=i) # heutige Datum + x Tage
            print(Tag.strftime("%a"), Tag.strftime("%d.%m.%Y"), file=f)# Erst die Abkürzung vom Wochentag; dann den Tag,Monat und das Jahr von dem jeweiligen Tag; print in eine neue txt
            print(">", file=f)

            i=i+1
    elif Abteilung ==2:
        with open("VorlageSchule.txt") as Datei:

            while i < 5:
                for Zeile in Datei:
                    Tag = heute1 + datetime.timedelta(days=i) # heutige Datum + x Tage
                    print(Tag.strftime("%a"), Tag.strftime("%d.%m.%Y"), file=f)# Erst die Abkürzung vom Wochentag; dann den Tag,Monat und das Jahr von dem jeweiligen Tag; print in eine neue txt
                

                    if  Zeile == "Mo.\n":
                        for Zeile in Datei:

                            if Zeile == "Di.\n":
                                i = i + 1
                                break
                            print(Zeile,file=f)
                        break
                    
                    if i == 1:
                        for Zeile in Datei:
                            if Zeile == "Mi.\n":
                                i = i + 1
                                break
                            print(Zeile,file=f)
                        break
                    if i == 2:
                        for y in Datei:

                            if y == "Do.\n":
                                i = i + 1
                                break
                            print(y,file=f)
                        break
                    if i == 3:
                        for Zeile in Datei:

                            if Zeile == "Fr.\n":
                                i = i + 1
                                break
                            print(Zeile,file=f)
                        break
                    if i == 4:
                        for Zeile in Datei:
                            if Zeile == "End":
                                i = i + 1
                                break
                            print(Zeile,file=f)
                            
                
    else:
        while i < 5:
            Tag = heute1 + datetime.timedelta(days=i) # heutige Datum + x Tage
            print(Tag.strftime("%a"), Tag.strftime("%d.%m.%Y"), file=f)# Erst die Abkürzung vom Wochentag; dann den Tag,Monat und das Jahr von dem jeweiligen Tag; print in eine neue txt
            print("> Urlaub", file=f)

            i=i+1
        

    print("\n", file=f)

    f.close()

    os.startfile("output.txt")






k = int(weekday)-1 #in K kommt die Zahl vom Wochentag minus 1
Montag = heute - datetime.timedelta(days=k)#heutige Datum minus die anzahl der Tage von k

weekday = 1

#Nur style mit KI erstellt weil hatte kein bock

# Erscheinungsbild
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# Hauptfenster
Berichtsheft = ctk.CTk()
Berichtsheft.title("Berichtsheft Generator")
Berichtsheft.geometry("420x600")
Berichtsheft.resizable(False, False)


# Überschrift
Titel = ctk.CTkLabel(
    Berichtsheft,
    text="Berichtsheft Generator",
    font=("Arial", 26, "bold")
)
Titel.pack(pady=(30, 5))


Untertitel = ctk.CTkLabel(
    Berichtsheft,
    text="Erstelle dein Berichtsheft für die aktuelle Woche",
    font=("Arial", 14)
)
Untertitel.pack(pady=(0, 25))


# Informationen zur aktuellen Woche
KW = Montag.isocalendar()[1]
Freitag = Montag + datetime.timedelta(days=4)

WochenInfo = ctk.CTkFrame(Berichtsheft)
WochenInfo.pack(padx=30, pady=10, fill="x")

KWLabel = ctk.CTkLabel(
    WochenInfo,
    text=f"Kalenderwoche {KW}",
    font=("Arial", 18, "bold")
)
KWLabel.pack(pady=(15, 3))

DatumLabel = ctk.CTkLabel(
    WochenInfo,
    text=f"{Montag.strftime('%d.%m.%Y')} – {Freitag.strftime('%d.%m.%Y')}",
    font=("Arial", 14)
)
DatumLabel.pack(pady=(0, 15))


# Abteilung
AbteilungLabel = ctk.CTkLabel(
    Berichtsheft,
    text="Abteilung auswählen:",
    font=("Arial", 16, "bold")
)
AbteilungLabel.pack(pady=(20, 10))


v = ctk.IntVar(value=0)


Infra = ctk.CTkRadioButton(
    Berichtsheft,
    text="Infrastruktur",
    variable=v,
    value=1
)
Infra.pack(anchor="w", padx=80, pady=4)


Schule = ctk.CTkRadioButton(
    Berichtsheft,
    text="Schule",
    variable=v,
    value=2
)
Schule.pack(anchor="w", padx=80, pady=4)


Urlaub = ctk.CTkRadioButton(
    Berichtsheft,
    text="Urlaub",
    variable=v,
    value=3
)
Urlaub.pack(anchor="w", padx=80, pady=4)


ELIT = ctk.CTkRadioButton(
    Berichtsheft,
    text="ELIT",
    variable=v,
    value=4
)
ELIT.pack(anchor="w", padx=80, pady=4)


# Statusmeldung
Status = ctk.CTkLabel(
    Berichtsheft,
    text="",
    font=("Arial", 13)
)
Status.pack(pady=(15, 5))


# Erstellen
def Erstellen():

    Abteilung = v.get()

    if Abteilung == 0:
        Status.configure(
            text="⚠ Bitte zuerst eine Abteilung auswählen."
        )
        return

    Generator(Montag, Abteilung)

    Status.configure(
        text="✓ Berichtsheft erfolgreich erstellt."
    )

    os.startfile("output.txt")


Button = ctk.CTkButton(
    Berichtsheft,
    text="Berichtsheft erstellen",
    width=250,
    height=45,
    font=("Arial", 15, "bold"),
    command=Erstellen
)
Button.pack(pady=(15, 20))


Berichtsheft.mainloop()
