import tkinter as ttk

TxtValue = ""
AusgabeText = ""
internCode = ""
#ID
HID = 0
XID = 0
AID = 0
BID = 0
CID = 0
DID = 0

#Standard Menü Einstellungen
LänderEinstellung = "D - Deutschland"
ZonenEinstellungen = "Zone XY: "

BereichID = 1000
#1000 = Start
#999 = 0 Bereich
#7890 = Programmier Bereich
# x>250 = Menüpunkte Programmierbereich

def HakenaddToTxt(x):
    global TxtValue
    global HID
    global internCode
    HID = 1
    internCode = internCode + str(x) + "#"
    TxtValue = TxtValue + str(x)
    CodeTxt.set(TxtValue)
    print("def addToTxt:(", x, ") =", TxtValue)

def AaddToTxt(x):
    global TxtValue
    global AID
    global internCode
    AID = 1
    internCode = internCode + str(x) + "#"
    TxtValue = TxtValue + str(x)
    CodeTxt.set(TxtValue)
    print("def addToTxt:(", x, ") =", TxtValue)

def BaddToTxt(x):
    global TxtValue
    global BID
    global internCode
    BID = 1
    internCode = internCode + str(x) + "#"
    TxtValue = TxtValue + str(x)
    CodeTxt.set(TxtValue)
    print("def addToTxt:(", x, ") =", TxtValue)

def CaddToTxt(x):
    global TxtValue
    global CID
    global internCode
    CID = 1
    internCode = internCode + str(x) + "#"
    TxtValue = TxtValue + str(x)
    CodeTxt.set(TxtValue)
    print("def addToTxt:(", x, ") =", TxtValue)

def DaddToTxt(x):
    global TxtValue
    global DID
    global internCode
    DID = 1
    internCode = internCode + str(x) + "#"
    TxtValue = TxtValue + str(x)
    CodeTxt.set(TxtValue)
    print("def addToTxt:(", x, ") =", TxtValue)

def XaddToTxt(x):
    global TxtValue
    global XID
    global internCode
    XID = 1
    internCode = internCode + str(x) +  "#"
    TxtValue = TxtValue + str(x)
    CodeTxt.set(TxtValue)
    print("def addToTxt:(", x, ") =", TxtValue)

def addToTxt(x):
    global TxtValue
    global internCode
    TxtValue = TxtValue + str(x)
    internCode = internCode + str(x)
    CodeTxt.set(TxtValue)
    print("def addToTxt:(", x, ") =",  TxtValue)

def Delete(x):
    global  TxtValue
    global Code
    global XID
    global HID
    global BereichID
    XID = 0
    HakenID = 0
    Code = ""
    TxtValue = ""
    CodeTxt.set(TxtValue)
    print("Eingabe gelöscht", "CodeTxt Wert: ", CodeTxt, "TxtValue Wert: ",TxtValue)

def DeleteAll(x):
    global  TxtValue
    global Code
    global XID
    global HID
    global AID
    global BID
    global CID
    global DID
    global BereichID
    HID = 0
    XID = 0
    AID = 0
    BID = 0
    CID = 0
    DID = 0
    XID = 0
    BereichID = 1000
    AusgabeEins.config(text=str(""))
    AusgabeZwei.config(text=str(""))
    Code = ""
    TxtValue = ""
    CodeTxt.set(TxtValue)
    print("Eingabe gelöscht", "CodeTxt Wert: ", CodeTxt, "TxtValue Wert: ",TxtValue)

def ConfirmEntrance(q):
    global TxtValue
    global BereichID
    global AusgabeText
    global XID
    global HID
    global AID
    global BID
    global CID
    global DID
    global internCode

    if XID != 0:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        XID = 2
    elif HID != 0:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        HID = 2
    elif AID != 0:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        AID = 2
    elif BID != 0:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        BID = 2
    elif CID != 0:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        CID = 2
    elif DID != 0:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        DID = 2

    iTxtValue= int(TxtValue)
    CodeLenght = len(TxtValue)
    print("def: ConfirmEntrance")
    NullFront = "%03d" % (iTxtValue)
    print(NullFront)
    if iTxtValue == 0 and BereichID == 1000 and  CodeLenght == 1:
        print("0 Bereich: Programmier Passwort eingeben")
        AusgabeEins.config(text=str("Programmier-Passwort eingeben"))
        print(AusgabeText)
        Delete(1)
        BereichID = 999
        print(BereichID)
    elif CodeLenght == 4 and BereichID == 999:
        if iTxtValue == 7890:
            print("Passwort richtig")
            AusgabeEins.config(text=str("Passwort richtig - Programmiermodus"))
            Delete(1)
            BereichID = 7890
            print("BereichID: ", BereichID)
    elif CodeLenght == 3 and BereichID == 7890:
        print("Menüpunkt-Code")
        MenüPunkte(iTxtValue)
    elif BereichID < 250:
        print("<250")
        EinstellungsPunkte(iTxtValue, CodeLenght)

def MenüPunkte(Menüpunkt):
    global TxtValue
    global BereichID
    global LänderEinstellung

    if Menüpunkt == 0:
        print("Menüpunkt: 000")
        AusgabeEins.config(text=str("Menüpunkt: 000"))
        AusgabeZwei.config(text=str(LänderEinstellung))
        BereichID = 0
        Delete(1)
    elif Menüpunkt >= 1 and Menüpunkt <= 16:
        print("Menüpunkt: 001 - 008")
        AusgabeEins.config(text=str("Menüpunkt: 001 -016"))
        AusgabeZwei.config(text=str(ZonenEinstellungen))
        BereichID = 1
        Delete(1)
    elif Menüpunkt == 20:
        print("Menüpunkt: 020")
        Ausgabe.config(text=str("Menüpunkt: 020"))
        BereichID = 20
        Delete(1)
    elif Menüpunkt == 21:
        print("Menüpunkt: 021")
        Ausgabe.config(text=str("Menüpunkt: 021"))
        BereichID = 21
        Delete(1)
    elif Menüpunkt == 22:
        print("Menüpunkt: 022")
        Ausgabe.config(text=str("Menüpunkt: 022"))
        BereichID = 22
        Delete(1)
    elif Menüpunkt == 23:
        print("Menüpunkt: 023")
        Ausgabe.config(text=str("Menüpunkt: 023"))
        BereichID = 23
        Delete(1)
    elif Menüpunkt == 24:
        print("Menüpunkt: 024")
        Ausgabe.config(text=str("Menüpunkt: 024"))
        BereichID = 24
        Delete(1)
    elif Menüpunkt == 25:
        print("Menüpunkt: 025")
        Ausgabe.config(text=str("Menüpunkt: 025"))
        BereichID = 25
        Delete(1)
    elif Menüpunkt == 26:
        print("Menüpunkt: 026")  #
        Ausgabe.config(text=str("Menüpunkt: 026"))
        BereichID = 26
        Delete(1)
    elif Menüpunkt == 27:
        print("Menüpunkt: 027")
        Ausgabe.config(text=str("Menüpunkt: 027"))
        BereichID = 27
        Delete(1)
    elif Menüpunkt == 28:
        print("Menüpunkt: 028")
        Ausgabe.config(text=str("Menüpunkt: 028"))
        BereichID = 28
        Delete(1)
    elif Menüpunkt == 29:
        print("Menüpunkt: 029")
        Ausgabe.config(text=str("Menüpunkt: 029"))
        BereichID = 29
        Delete(1)
    elif Menüpunkt == 30:
        print("Menüpunkt: 030")
        Ausgabe.config(text=str("Menüpunkt: 030"))
        BereichID = 30
        Delete(1)
    elif Menüpunkt == 31:
        print("Menüpunkt: 031")
        Ausgabe.config(text=str("Menüpunkt: 031"))
        BereichID = 31
        Delete(1)
    elif Menüpunkt == 32:
        print("Menüpunkt: 032")
        Ausgabe.config(text=str("Menüpunkt: 032"))
        BereichID = 32
        Delete(1)
    elif Menüpunkt == 33:
        print("Menüpunkt: 033")
        Ausgabe.config(text=str("Menüpunkt: 033"))
        BereichID = 33
        Delete(1)
    elif Menüpunkt == 34:
        print("Menüpunkt: 034")
        Ausgabe.config(text=str("Menüpunkt: 034"))
        BereichID = 34
        Delete(1)
    elif Menüpunkt == 35:
        print("Menüpunkt: 035")
        Ausgabe.config(text=str("Menüpunkt: 035"))
        BereichID = 35
        Delete(1)
    elif Menüpunkt == 36:
        print("Menüpunkt: 036")
        Ausgabe.config(text=str("Menüpunkt: 036"))
        BereichID = 36
        Delete(1)
    elif Menüpunkt == 37:
        print("Menüpunkt: 037")
        Ausgabe.config(text=str("Menüpunkt: 037"))
        BereichID = 37
        Delete(1)
    elif Menüpunkt == 38:
        print("Menüpunkt: 038")
        Ausgabe.config(text=str("Menüpunkt: 038"))
        BereichID = 38
        Delete(1)
    elif Menüpunkt == 39:
        print("Menüpunkt: 039")
        Ausgabe.config(text=str("Menüpunkt: 039"))
        BereichID = 39
        Delete(1)
    elif Menüpunkt == 40:
        print("Menüpunkt: 040")
        Ausgabe.config(text=str("Menüpunkt: 040"))
        BereichID = 40
        Delete(1)
    elif Menüpunkt == 41:
        print("Menüpunkt: 041")
        Ausgabe.config(text=str("Menüpunkt: 041"))
        BereichID = 41
        Delete(1)
    elif Menüpunkt == 42:
        print("Menüpunkt: 042")
        Ausgabe.config(text=str("Menüpunkt: 042"))
        BereichID = 42
        Delete(1)
    elif Menüpunkt == 43:
        print("Menüpunkt: 043")
        Ausgabe.config(text=str("Menüpunkt: 043"))
        BereichID = 43
        Delete(1)
    elif Menüpunkt == 44:
        print("Menüpunkt: 044")
        Ausgabe.config(text=str("Menüpunkt: 044"))
        BereichID = 44
        Delete(1)
    elif Menüpunkt == 45:
        print("Menüpunkt: 045")
        Ausgabe.config(text=str("Menüpunkt: 045"))
        BereichID = 45
        Delete(1)
    elif Menüpunkt == 46:
        print("Menüpunkt: 046")
        Ausgabe.config(text=str("Menüpunkt: 046"))
        BereichID = 46
        Delete(1)
    elif Menüpunkt == 47:
        print("Menüpunkt: 047")
        Ausgabe.config(text=str("Menüpunkt: 047"))
        BereichID = 47
        Delete(1)
    elif Menüpunkt == 48:
        print("Menüpunkt: 048")
        Ausgabe.config(text=str("Menüpunkt: 048"))
        BereichID = 48
        Delete(1)
    elif Menüpunkt == 50:
        print("Menüpunkt: 050")
        Ausgabe.config(text=str("Menüpunkt: 050"))
        BereichID = 50
        Delete(1)

def EinstellungsPunkte(iTxtValue, CodeLenght):
    global TxtValue
    global BereichID
    global XID
    global HakenID
    global LänderEinstellung
    global ZonenEinstellungen
    if BereichID == 0 and CodeLenght > 0 and CodeLenght <= 2:
        if iTxtValue == 0 and XID == 0:
            LänderEinstellung = "UK – Großbritannien "
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 1 and XID == 0:
            LänderEinstellung = "I – Italien"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 2 and XID == 0:
            LänderEinstellung = "EE – Spanien"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 3 and XID == 0:
            LänderEinstellung = "P – Portugal"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 4 and XID == 0:
            LänderEinstellung = "NL – Niederlande"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 5 and XID == 0:
            LänderEinstellung = "FR – Frankreich"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 6 and XID == 0:
            LänderEinstellung = "B – Belgien"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 7 and XID == 0:
            LänderEinstellung = "D – Deutschland"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 8 and XID == 0:
            LänderEinstellung = "CH – Schweiz"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 9 and XID == 0:
            LänderEinstellung = "A – Österreich"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 1 and XID == 2:
            LänderEinstellung = "IRL – Irland"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 2 and XID == 2:
            LänderEinstellung = "OEM1"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 3 and XID == 2:
            LänderEinstellung = "OEM2"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 4 and XID == 2:
            LänderEinstellung = "FI – Finnland"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 5 and XID == 2:
            LänderEinstellung = "N – Norwegen"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 6 and XID == 2:
            LänderEinstellung = "DK – Dänemark"
            AusgabeZwei.config(text=str(LänderEinstellung))
        elif iTxtValue == 7 and XID == 2:
            LänderEinstellung = "S – Schweden "
            AusgabeZwei.config(text=str(LänderEinstellung))
    elif BereichID == 1 and CodeLenght > 0 and CodeLenght <= 2:
        if iTxtValue == 0 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "NV – Nicht verwendet "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 1 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "UF – Überfall "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 2 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "FE -Feuer "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 3 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "SO - Sofort "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 4 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "24 -24 Stunden "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 5 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "EA -Ein/Ausgang "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 6 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "EF -Eingang folgend "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 7 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "ES - Erschütterungssensor "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 8 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "TK - Technik "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 9 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "SK - Schlüsselkasten "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 10 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "BM - Brandmelder "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 11 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "SS - Schlüssekschalter "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 12 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "BS - Blockschloss "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 13 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "AM - Anti Mask "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 14 and XID == 0:
            ZonenEinstellungen = ZonenEinstellungen + "FB - Forbikobler Zone "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 1 and XID == 2:
            ZonenEinstellungen = ZonenEinstellungen + "C - Türgong "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 2 and XID == 2:
            ZonenEinstellungen = ZonenEinstellungen + "S - Melderset "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 3 and XID == 2:
            ZonenEinstellungen = ZonenEinstellungen + "D - Doppelauslösung "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 4 and XID == 2:
            ZonenEinstellungen = ZonenEinstellungen + "O - Zonensperren möglich "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
        elif iTxtValue == 7 and XID == 2:
            ZonenEinstellungen = ZonenEinstellungen + "1....6 Empfindlichkeit "
            AusgabeZwei.config(text=str(ZonenEinstellungen))
            Delete(1)
    #DeleteAll(1)

win = ttk.Tk()
win.title('Terxon Simulator')
win.geometry('380x440')

#row 1
CodeTxt = ttk.StringVar()
datafield = ttk.Entry(win, textvariable = CodeTxt, font="Serif 15", bg="grey", fg="black")
datafield.grid(row=0, columnspan=4, ipadx=80, ipady=15)

#row 2
AButton = ttk.Button(win, text="A", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: AaddToTxt("A"))
AButton.grid(row=2, column=0,padx=2, pady=3)

BButton = ttk.Button(win, text="B", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: BaddToTxt("B"))
BButton.grid(row=2, column=1,padx=2, pady=3)

CButton = ttk.Button(win, text="C", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: CaddToTxt("C"))
CButton.grid(row=2, column=2,padx=2, pady=3)

DButton = ttk.Button(win, text="D", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: DaddToTxt("D"))
DButton.grid(row=2, column=3,padx=2, pady=3)

#row 3
oneButton = ttk.Button(win, text="1", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("1"))
oneButton.grid(row=3, column=0,padx=2, pady=3)

twoButton = ttk.Button(win, text="2", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("2"))
twoButton.grid(row=3, column=1,padx=2, pady=3)

twoButton = ttk.Button(win, text="3", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("3"))
twoButton.grid(row=3, column=2,padx=2, pady=3)

hakenButton = ttk.Button(win, text="√", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: HakenaddToTxt("√"))
hakenButton.grid(row=3, column=3,padx=2, pady=3)

#row 4
fourButton = ttk.Button(win, text="4", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("4"))
fourButton.grid(row=4, column=0,padx=2, pady=3)

fiveButton = ttk.Button(win, text="5", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("5"))
fiveButton.grid(row=4, column=1,padx=2, pady=3)

fiveButton = ttk.Button(win, text="6", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("6"))
fiveButton.grid(row=4, column=2,padx=2, pady=3)

kreuzButton = ttk.Button(win, text="X", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: XaddToTxt("X"))
kreuzButton.grid(row=4, column=3,padx=2, pady=3)

#row 5
sevenButton = ttk.Button(win, text="7", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("7"))
sevenButton.grid(row=5, column=0,padx=2, pady=3)

eightButton = ttk.Button(win, text="8", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("8"))
eightButton.grid(row=5, column=1,padx=2, pady=3)

nineButton = ttk.Button(win, text="9", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("9"))
nineButton.grid(row=5, column=2,padx=2, pady=3)

nullButton = ttk.Button(win, text="0", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("0"))
nullButton.grid(row=5, column=3,padx=2, pady=3)

#row 6
ConfirmButton = ttk.Button(win, text="Confirm", pady=10, padx=60, font="Serif 15", bg="black", fg="white", command=lambda: ConfirmEntrance("1"))
ConfirmButton.grid(row=6, column = 1, columnspan=6,padx=2, pady=3)

DelButton = ttk.Button(win, text="Del", pady=10, padx=50, font="Serif 15", bg="black", fg="white", command=lambda: Delete(1))
DelButton.grid(row=6, column=0, columnspan=2 ,padx=2, pady=3)

AusgabeEins = ttk.Label(win, pady=0, padx=0, font="Serif 12", bg="lime green", fg="black")
AusgabeEins.grid(row=7, column=0, columnspan=5 ,padx=2, pady=3)

AusgabeZwei = ttk.Label(win, pady=0, padx=0, font="Serif 12", bg="yellow", fg="black")
AusgabeZwei.grid(row=8, column=0, columnspan=5 ,padx=2, pady=3)

win.mainloop()

