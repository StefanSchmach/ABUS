import tkinter as ttk

TxtValue = ""
ProgrammierID = 0

def addToTxt(x):
    global TxtValue
    TxtValue = TxtValue + str(x)
    CodeTxt.set(TxtValue)
    print("def addToTxt:(", x, ") =",  TxtValue)

def Delete(x):
    global  TxtValue
    TxtValue = ""
    CodeTxt.set(TxtValue)
    print("Eingabe gelöscht", "CodeTxt Wert: ", CodeTxt, "TxtValue Wert: ",TxtValue)

def ConfirmEntrance(q):
    #Var Inport
    global TxtValue
    global NullNum
    global ProgrammierID
    #global AusgabeText

    iTxtValue= int(TxtValue)
    CodeLenght = len(TxtValue)
    print("def: ConfirmEntrance")
    NullFront = "%03d" % (iTxtValue)
    print(NullFront)
    if CodeLenght == 1 :
        if iTxtValue == 0:
            print("0 Bereich: Programmier Passwort eingeben")
            AusgabeText = "Programmier Passwort eingeben"
            Delete(1)
            print(AusgabeText)

            print(ProgrammierID)
            AusgabeText.str("Programmier Passwort eingeben")
        elif iTxtValue != 0:
            print("Error: Wrong Input")
            AusgabeText.set("Programmier Passwort eingeben")
    elif CodeLenght == 4:
        if iTxtValue == 7890:
            print("Passwort richtig")
            Delete(1)
    elif CodeLenght == 3:
        print("Menüpunkt-Code")
        Menüpunkt = iTxtValue
        if Menüpunkt == 0:
            print("Menüpunkt: 000")
            Delete(1)
        elif  iTxtValue >= 1 and iTxtValue <= 8:
            print("Menüpunkt: 001 - 008")
            Delete(x)
        elif Menüpunkt == 20:
            print("Menüpunkt: 020")
            Delete(x)
        elif Menüpunkt == 21:
            print("Menüpunkt: 021")
            Delete(x)
        elif Menüpunkt == 22:
            print("Menüpunkt: 022")
            Delete(x)
        elif Menüpunkt == 23:
            print("Menüpunkt: 023")
            Delete(x)
        elif Menüpunkt == 24:
            print("Menüpunkt: 024")
            Delete(x)
        elif Menüpunkt == 25:
            print("Menüpunkt: 025")
            Delete(x)
        elif Menüpunkt == 26:
            print("Menüpunkt: 026")
            Delete(x)
        elif Menüpunkt == 27:
            print("Menüpunkt: 027")
            Delete(x)
        elif Menüpunkt == 28:
            print("Menüpunkt: 028")
            Delete(x)
        elif Menüpunkt == 29:
            print("Menüpunkt: 029")
            Delete(x)
        elif Menüpunkt == 30:
            print("Menüpunkt: 030")
            Delete(x)
        elif Menüpunkt == 31:
            print("Menüpunkt: 031")
            Delete(x)
        elif Menüpunkt == 32:
            print("Menüpunkt: 032")
            Delete(x)
        elif Menüpunkt == 33:
            print("Menüpunkt: 033")
            Delete(x)
        elif Menüpunkt == 34:
            print("Menüpunkt: 034")
            Delete(x)
        elif Menüpunkt == 35:
            print("Menüpunkt: 035")
            Delete(x)
        elif Menüpunkt == 36:
            print("Menüpunkt: 036")
            Delete(x)
        elif Menüpunkt == 37:
            print("Menüpunkt: 037")
            Delete(x)
        elif Menüpunkt == 38:
            print("Menüpunkt: 038")
            Delete(x)
        elif Menüpunkt == 39:
            print("Menüpunkt: 039")
            Delete(x)
        elif Menüpunkt == 40:
            print("Menüpunkt: 040")
            Delete(x)
        elif Menüpunkt == 41:
            print("Menüpunkt: 041")
            Delete(x)
        elif Menüpunkt == 42:
            print("Menüpunkt: 042")
            Delete(x)
        elif Menüpunkt == 43:
            print("Menüpunkt: 043")
            Delete(x)
        elif Menüpunkt == 44:
            print("Menüpunkt: 044")
            Delete(x)
        elif Menüpunkt == 45:
            print("Menüpunkt: 045")
            Delete(x)
        elif Menüpunkt == 46:
            print("Menüpunkt: 046")
            Delete(x)
        elif Menüpunkt == 47:
            print("Menüpunkt: 047")
            Delete(x)
        elif Menüpunkt == 48:
            print("Menüpunkt: 048")
            Delete(x)
        elif Menüpunkt == 50:
            print("Menüpunkt: 050")
            Delete(x)

win = ttk.Tk()
win.title('Terxon Simulator')
win.geometry('400x500')

#row 1
CodeTxt = ttk.StringVar()
datafield = ttk.Entry(win, textvariable = CodeTxt, font="Serif 15", bg="grey", fg="black")
datafield.grid(row=0, columnspan=4, ipadx=80, ipady=15)

#row 2
AButton = ttk.Button(win, text="A", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("A"))
AButton.grid(row=2, column=0,padx=2, pady=3)

BButton = ttk.Button(win, text="B", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("B"))
BButton.grid(row=2, column=1,padx=2, pady=3)

CButton = ttk.Button(win, text="C", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("C"))
CButton.grid(row=2, column=2,padx=2, pady=3)

DButton = ttk.Button(win, text="D", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("D"))
DButton.grid(row=2, column=3,padx=2, pady=3)

#row 3
oneButton = ttk.Button(win, text="1", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("1"))
oneButton.grid(row=3, column=0,padx=2, pady=3)

twoButton = ttk.Button(win, text="2", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("2"))
twoButton.grid(row=3, column=1,padx=2, pady=3)

twoButton = ttk.Button(win, text="3", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("3"))
twoButton.grid(row=3, column=2,padx=2, pady=3)

hakenButton = ttk.Button(win, text="√", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("√"))
hakenButton.grid(row=3, column=3,padx=2, pady=3)

#row 4
fourButton = ttk.Button(win, text="4", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("4"))
fourButton.grid(row=4, column=0,padx=2, pady=3)

fiveButton = ttk.Button(win, text="5", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("5"))
fiveButton.grid(row=4, column=1,padx=2, pady=3)

fiveButton = ttk.Button(win, text="6", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("6"))
fiveButton.grid(row=4, column=2,padx=2, pady=3)

kreuzButton = ttk.Button(win, text="X", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: addToTxt("X"))
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

AusgabeText = ""
Ausgabe= ttk.Label(win, textvariable = AusgabeText, pady=10, padx=120, font="Serif 15", bg="white", fg="black")
Ausgabe.grid(row=7, column=0, columnspan=5 ,padx=2, pady=3)

win.mainloop()

