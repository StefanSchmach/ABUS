import tkinter as ttk
import os
import json
import functools
from datetime import datetime



UsernameWindows = os.getlogin()
FolderPathLocal = "C:/Users/" + UsernameWindows + "/AppData/Local"
FolderPathLocalTerxon = FolderPathLocal + "/TerxonSimulation"
CreateFile = FolderPathLocalTerxon + "/TerxonConfig.json"
ConfigPath = CreateFile

#def LoadConfig(x):
   # globals().update(locals())
with open(ConfigPath, 'r') as ConfigFile:
    data = json.load(ConfigFile)
    LaenderEinstellung = data["LaenderEinstellung"]  # Einstellung 000
    ZonenEinstellungenDef = data["ZonenEinstellungenDef"]  # Einstellung 001 - 016
    ZonenEinstellungenFunkDef = data["ZonenEinstellungenFunkDef"]  # Einstellung X17 - X32
    Programmiercode = data["Programmiercode"]  # Einstellung 020
    ZonenAbschlussNummer = data["ZonenAbschlussNummer"]  # Einstellung 021
    InterVolumeNummer = data["InterVolumeNummer"]  # Einstellung 022
    FernReset = data["FernReset"]  # Einstellung 023
    Kundenname = data["Kundenname"]  # Einstellung 024
    InternerAlarm = data["InternerAlarm"]  # Einstellung 025
    AlarmbeiAktivierung = data["AlarmbeiAktivierung"]  # Einstellung 027
    StatusAnzeigeAusblenden = data["StatusAnzeigeAusblenden"]  # Einstellung 028
    ExternAlarmVerzoegerung = data["ExternAlarmVerzoegerung"]  # Einstellung 029
    Ueberfallalarm = data["Ueberfallalarm"]  # Einstellung 030
    ZonenSabotageReset = data["ZonenSabotageReset"]  # Einstellung 031
    BedienteileundPartitionen = data["BedienteileundPartitionen"]  # Einstellung 032
    SystemReset = data["SystemReset"]  # Einstellung 033
    UeberfallReset = data["UeberfallReset"]  # Einstellung 034
    ErstmelderAlarmausblenden = data['ErstmelderAlarmausblenden']  # Einstellung 035
    AlarmAbbruch = data['AlarmAbbruch']  # Einstellung 036
    SabotageReportdeaktiv = data['SabotageReportdeaktiv']  # Einstellung 037
    SystemsabotageReset = data['SystemsabotageReset']  # Einstellung 038
    AusgangsmodusBereichA = data['AusgangsmodusBereichA']  # Einstellung 039
    SystemAutoAktivnachAlarm = data['SystemAutoAktivnachAlarm']  # Einstellung 040
    SirenenVerzögerung = data['SirenenVerzögerung']  # Einstellung 041
    Sirenendauer = data['Sirenendauer']  # Einstellung 042
    AusgangszeitGesamtbereich = data['AusgangszeitGesamtbereich']  # Einstellung 044
    EinAusgagsverzögerungVolumen = data['EinAusgagsverzögerungVolumen']  # Einstellung 045
    SabotagealarmReaktion = data['SabotagealarmReaktion']  # Einstellung 046
    PartionAAlarmReaktion = data['PartionAAlarmReaktion']  # Einstellung 047
    Bedienteilsperre = data['Bedienteilsperre']  # Einstellung 048
    DatumundUhrzeit = data['DatumundUhrzeit']  # Einstellung 051
    ZonenundSabotageSperren = data['ZonenundSabotageSperren']  # Einstellung 052
    AbbruchReset = data['AbbruchReset']  # Einstellung 053
    SupervisionFunkmelder = data['SupervisionFunkmelder']  # Einstellung 054
    LaengeZugangscode = data['LaengeZugangscode']  # Einstellung 056
    BatterieTest = data['BatterieTest']  # Einstellung 057
    SupervisionSabotageReset = data['SupervisionSabotageReset']  # Einstellung 058
    SabotageSirene = data['SabotageSirene']  # Einstellung 059
    ZonenverhaltenInternB = 'ZonenverhaltenInternB'  # Einstellung 060
    ZonenverhaltenInternBEins = data['ZonenverhaltenInternBEins']  # Einstellung 061
    AusgangsmodusInternB = data['AusgangsmodusInternB']  # Einstellung 062
    AlarmverhaltenInternB = data['AlarmverhaltenInternB']  # Einstellung 063
    AlarmverhaltenInternBEins = data['AlarmverhaltenInternBEins']  # Einstellung 064
    AusgangszeitInternB = data['AusgangszeitInternB']  # Einstellung 065
    ForbikoblerKorrekt = data['ForbikoblerKorrekt']  # Einstellung 067
    ForbikoblerEintrittszeiten = data['ForbikoblerEintrittszeiten']  # Einstellung 068
    ForbikoblerTuersperre = data['ForbikoblerTuersperre']  # Einstellung 069
    ZonenverhaltenEFInternC = data['ZonenverhaltenEFInternC']  # Einstellung 070
    ZonenverhaltenEAInternC = data['ZonenverhaltenEAInternC']  # Einstellung 071
    AusgangsmodusInternC = data['AusgangsmodusInternC']  # Einstellung 072
    AlarmverhaltenInternC = data['AlarmverhaltenInternC']  # Einstellung 073
    AusgangszeitbeiInternC = data['AusgangszeitbeiInternC']  # Einstellung 075
    AusgangsmodusInternD = data['AusgangsmodusInternD']  # Einstellung 076
    AlarmverhaltenInternD = data['AlarmverhaltenInternD']  # Einstellung 077
    AusgangszeitInternD = data['AusgangszeitInternD']  # Einstellung 079
    ForbikoblerTuerklingel = data['ForbikoblerTuerklingel']  # Einstellung 080
    VerhaltenRelaisausgangEins = data['VerhaltenRelaisausgangEins']  # Einstellung 081
    VerhaltenRelaisausgangZwei = data['VerhaltenRelaisausgangZwei']  # Einstellung 082
    VerhaltenTransistoraugangEins = data['VerhaltenTransistoraugangEins']  # Einstellung 083
    VerhaltenAusgaengeEinbruchalarm = ['VerhaltenAusgaengeEinbruchalarm']  # Einstellung 085
    ZusaetlicheEingangsversoegerung = data['ZusaetlicheEingangsversoegerung']  # Einstellung 086
    Bedienteilalarm = data['Bedienteilalarm']  # Einstellung 087
    AlarmBestaetigung = data['AlarmBestaetigung']  # Einstellung 089
    Ereignisspeicher = ['Ereignisspeicher']  # Einstellung 090
    AusgangEinsTest = data['AusgangEinsTest']  # Einstellung 091
    AusgangZweiTest = data['AusgangZweiTest']  # Einstellung 092
    AusgangDreiTest = data['AusgangDreiTest']  # Einstellung 093
    InternLautsprecherTest = data['InternLautsprecherTest']  # Einstellung 094
    SireneBedienteilTest = data['SireneBedienteilTest']  # Einstellung 095
    Gehtest = data['Gehtest']  # Einstellung 097
    WerkseinstellungWiedherstellen = data['WerkseinstellungWiedherstellen']  # Einstellung 098
    ProgrammiermenuVerlassen = data['ProgrammiermenuVerlassen']  # Einstellung 099
    RufmodusTWG = data['RufmodusTWG']  # Einstellung 101
    FormatReport = data['FormatReport']  # Einstellung 103
    Testanruf = data['Testanruf']  # Einstellung 105
    Leitungsverlustmeldung = data['Leitungsverlustmeldung']  # Einstellung 106
    DynamischerTestanruf = data['DynamischerTestanruf']  # Einstellung 108
    ThreeWayCall = data['ThreeWayCall']  # Einstellung 109
    DownloadModus = data['DownloadModus']  # Einstellung 110
    RufebisAntwortDownload = ['RufebisAntwortDownload']  # Einstellung 112
    EinsRufDownload = data['EinsRufDownload']  # Einstellugn 113
    Rueckrufmodus = data['Rueckrufmodus']  # Einstellung 114
    Telefonnummer = data['Telefonnummer']  # Einstellung 115
    TelefonnummerZwei = data['TelefonnummerZwei']  # Einstellung 116
    KundenNrLeitstelle = data['KundenNrLeitstelle']  # Einstellung 117
    FernTelNr = data['FernTelNr']  # Einstellung 118
    FernTelNrZwei = data['FernTelNrZwei']  # Einstellung 119
    FernTelNrDrei = data['FernTelNrDrei']  # Einstellung 120
    CommsAcknowledge = data['CommsAcknowledge']  # Einstellung 122
    RueckstellenReport = data['RueckstellenReport']  # Einstellung 123
    OpenClose = data['OpenClose']  # Einstellung 124
    KeinSignalGeschlossen = data['KeinSignalGeschlossen']  # Einstellung 125
    SpracheinstellungOSDMenu = data['SpracheinstellungOSDMenu']  # Einstellung 126
    ExternAlarm = data['ExternAlarm']  # Einstellung 128
    ExternDeaktivieren = data['ExternDeaktivieren']  # Einstellung 129
    SIAReportModus = data['SIAReportModus']  # Einstellung 131
    SendeSaboEinbruch = data['SendeSaboEinbruch']  # Einstellung 132
    SIARst = data['SIARst']  # Einstellung 133        EIGENTLICH 132
    ContactIDReportRst = data['ContactIDReportRst']  # Einstellung 143
    VerhaltenZusaetzSchaltausgangEins = data['VerhaltenZusaetzSchaltausgangEins']  # Einstellung 151
    VerhaltenZusaetzSchaltausgangZwei = data['VerhaltenZusaetzSchaltausgangZwei']  # Einstellung 152
    VerhaltenZusaetzSchaltausgangDrei = data['VerhaltenZusaetzSchaltausgangDrei']  # Einstellung 153
    VerhaltenZusaetzSchaltausgangVier = data['VerhaltenZusaetzSchaltausgangVier']  # Einstellung 154
    VerhaltenZusaetzSchaltausgangFuenf = data['VerhaltenZusaetzSchaltausgangFuenf']  # Einstellung 155
    VerhaltenZusaetzSchaltausgangSechs = data['VerhaltenZusaetzSchaltausgangSechs']  # Einstellung 156
    VerhaltenZusaetzSchaltausgangSieben = data['VerhaltenZusaetzSchaltausgangSieben']  # Einstellung 157
    VerhaltenZusaetzSchaltausgangAcht = data['VerhaltenZusaetzSchaltausgangAcht']  # Einstellung 158
    InversionZusaetzSchaltausgang = data['InversionZusaetzSchaltausgang']  # Einstellung 159
    ZeitbestaetigterAlarm = data['ZeitbestaetigterAlarm']  # Einstellung 160
    BestaetigenInternerLautsprecher = data['BestaetigenInternerLautsprecher']  # Einstellung 161
    BestaetigenExterneSirene = data['BestaetigenExterneSirene']  # Einstellung 162
    BestaetigenAlarmEintritt = data['BestaetigenAlarmEintritt']  # Einstellung 163
    BenutzerResetnachAlarm = data['BenutzerResetnachAlarm']  # Einstellung 164
    DauerAktivImpulsEinsBisVier = data['DauerAktivImpulsEinsBisVier']  # Einstellung 170
    Schaltausgangaktivstabil = data['Schaltausgangaktivstabil']  # Einstellung 171
    DauerDeaktivImpulsEIns = data['DauerDeaktivImpulsEIns']  # Einstellung 172
    Schaltausgangdeaktivstabil = data['Schaltausgangdeaktivstabil']  # Einstellung 173
    SchaltausgangFeuer = data['SchaltausgangFeuer']  # Einstellung 174
    SchaltausgangUeberfall = data['SchaltausgangUeberfall']  # Eisntellung 175
    WachtCode = data['WachtCode']  # Einstellung 181
    LetzerAusgangSettlingZeit = data['LetzerAusgangSettlingZeit']  # Einstellung 182
    DisplayZeileAendern = data['DisplayZeileaendern']  # Einstellung 183
    FeuerSignalgeber = data['FeuerSignalgeber']  # Einstellung 184
    SchluesselschalterAutoReset = data['SchluesselschalterAutoReset']  # Einstellung 185
    AnzahlHomeBeepRuf = data['AnzahlHomeBeepRuf']  # Einstellung 186
    FastFormatKanalEins = data['FastFormatKanalEins']  # Einstellung 191
    FastFormatKanalZwei = data['FastFormatKanalZwei']  # Einstellung 192
    FastFormatKanalDrei = data['FastFormatKanalDrei']  # Einstellung 193
    FastFormatKanalVier = data['FastFormatKanalVier']  # Einstellung 194
    FastFormatKanalFuenf = data['FastFormatKanalFuenf']  # Einstellung 195
    FastFormatKanalSechs = data['FastFormatKanalSechs']  # Einstellung 196
    FastFormatKanalSieben = data['FastFormatKanalSieben']  # Einstellung 197
    FastFormatKanalAcht = data['FastFormatKanalAcht']  # Einstellung 198
    AnzeigeZonenwiederstand = data['AnzeigeZonenwiederstand']  # Einstellung 199
    FobikoblerEintrittzeit = data['FobikoblerEintrittzeit']  # Einstellung 200
    EingangsverzoegerungGruppeEins = data['EingangsverzoegerungGruppeEins']  # Einstellung 201
    PartioniertenSystem = data["PartioniertenSystem"]  # Allgemeine Einstellung

    ConfigFile.close()

#Standard Start Funktionen
def StartConfigurationFile(x):
    if os.path.exists(FolderPathLocalTerxon):
        print("Ordner existiert!")
        if os.path.exists(ConfigPath):
            print("File existiert!")
        else:
            json_obj = {
                'LaenderEinstellung' : 'D - Deutschland'                #Einstellung 000
                ,'ZonenEinstellungenDef' : ' NV - Nicht verwendet'      #Einstellung 001 -016
                ,'ZonenEinstellungenFunkDef' : ' NV - Nicht verwendet'  #Einstellung Funk 001
                ,'Programmiercode' : '1111'                             #Einstellung 020
                ,'ZonenAbschlussNummer' : 0                             #Einstellung 021
                ,'InterVolumeNummer' : "5"                              #Einstellung 022
                ,'FernReset' : "0"                                      #Einstellung 023
                ,'Kundenname' : UsernameWindows                         #Einstellung 024
                ,'InternerAlarm' : 1                                    #Einstellung 025
                ,'AlarmbeiAktivierung' : 0                              #Einstellung 027
                ,'StatusAnzeigeAusblenden' : 0                          #Einstellung 028
                ,'ExternAlarmVerzoegerung' : 0                          #Einstellung 029
                ,'Ueberfallalarm' : 0                                   #Einstellung 030
                ,'ZonenSabotageReset' : 0                               #Einstellung 031
                ,'BedienteileundPartitionen' : 1                        #Einstellung 032
                ,'SystemReset' : 0                                      #Einstellung 033
                ,'UeberfallReset' : 0                                   #Einstellung 034
                ,'ErstmelderAlarmausblenden' : 0                        #Einstellung 035
                ,'AlarmAbbruch' : 0                                     #Einstellung 036
                ,'SabotageReportdeaktiv' : 0                            #Einstellung 037
                ,'SystemsabotageReset' : 0                              #Einstellung 038
                ,'AusgangsmodusBereichA' : 0                            #Einstellung 039
                ,'SystemAutoAktivnachAlarm' : 0                         #Einstellung 040
                ,'SirenenVerzögerung' : 0                               #Einstellung 041
                ,'Sirenendauer' : 1                                     #Einstellung 042
                ,'AusgangszeitGesamtbereich' :1                         #Einstellung 044
                ,'EinAusgagsverzögerungVolumen' : 0                     #Einstellung 045
                ,'SabotagealarmReaktion' : 0                            #Einstellung 046
                ,'PartionAAlarmReaktion' : 0                            #Einstellung 047
                ,'Bedienteilsperre' : 0                                 #Einstellung 048
                ,'DatumundUhrzeit' : 'Comming Soon'                     #Einstellung 051
                ,'ZonenundSabotageSperren' : 0                          #Einstellung 052
                ,'AbbruchReset' : 0                                     #Einstellung 053
                ,'SupervisionFunkmelder' : 0                            #Einstellung 054
                ,'LaengeZugangscode' : 0                                #Einstellung 056
                ,'BatterieTest' : 0                                     #Einstellung 057
                ,'SupervisionSabotageReset' : 0                         #Einstellung 058
                ,'SabotageSirene' : 0                                   #Einstellung 059
                ,'ZonenverhaltenInternB' : 0                            #Einstellung 060
                ,'ZonenverhaltenInternBEins' : 0                        #Einstellung 061
                ,'AusgangsmodusInternB' : 0                             #Einstellung 062
                ,'AlarmverhaltenInternB' : 0                            #Einstellung 063
                ,'AlarmverhaltenInternBEins' : 0                        #Einstellung 064
                ,'AusgangszeitInternB' : 0                              #Einstellung 065
                ,'ForbikoblerKorrekt' : 1                               #Einstellung 067
                ,'ForbikoblerEintrittszeiten' : 0                       #Einstellung 068
                ,'ForbikoblerTuersperre' : 0                            #Einstellung 069
                ,'ZonenverhaltenEFInternC' : 0                          #Einstellung 070
                ,'ZonenverhaltenEAInternC': 0                           #Einstellung 071
                ,'AusgangsmodusInternC' : 0                             #Einstellung 072
                ,'AlarmverhaltenInternC' : 0                            #Einstellung 073
                ,'AusgangszeitbeiInternC' : 1                           #Einstellung 075
                ,'AusgangsmodusInternD' : 0                             #Einstellung 076
                ,'AlarmverhaltenInternD' : 0                            #Einstellung 077
                ,'AusgangszeitInternD' : 1                              #Einstellung 079
                ,'ForbikoblerTuerklingel' : 0                           #Einstellung 080
                ,'VerhaltenRelaisausgangEins' : 00                      #Einstellung 081
                ,'VerhaltenRelaisausgangZwei' : 00                      #Einstellung 082
                ,'VerhaltenTransistoraugangEins' : 00                   #Einstellung 083
                ,'VerhaltenAusgaengeEinbruchalarm' : 0                  #Einstellung 085
                ,'ZusaetlicheEingangsversoegerung' : 0                  #Einstellung 086
                ,'Bedienteilalarm' : 0                                  #Einstellung 087
                ,'AlarmBestaetigung' : 0                                #Einstellung 089
                ,'Ereignisspeicher' : 0                                 #Einstellung 090
                ,'AusgangEinsTest' : 0                                  #Einstellung 091
                ,'AusgangZweiTest' : 0                                  #Einstellung 092
                ,'AusgangDreiTest' : 0                                  #Einstellung 093
                ,'InternLautsprecherTest' : 0                           #Einstellung 094
                ,'SireneBedienteilTest' : 0                             #Einstellung 095
                ,'Gehtest' : 0                                          #Einstellung 097
                ,'WerkseinstellungWiedherstellen' : 0                   #Einstellung 098
                ,'ProgrammiermenuVerlassen' : 0                         #Einstellung 099
                ,'RufmodusTWG' : 0                                      #Einstellung 101
                ,'FormatReport' : 0                                     #Einstellung 103
                ,'Testanruf' : 00                                       #Einstellung 105
                ,'Leitungsverlustmeldung' : 0                           #Einstellung 106
                ,'DynamischerTestanruf' : 0                             #Einstellung 108
                ,'ThreeWayCall' :  0                                    #Einstellung 109
                ,'DownloadModus' : 0                                    #Einstellung 110
                ,'RufebisAntwortDownload' : 0                           #Einstellung 112
                ,'EinsRufDownload' : 0                                  #Einstellugn 113
                ,'Rueckrufmodus' :  0                                   #Einstellung 114
                ,'Telefonnummer' : 0                                    #Einstellung 115
                ,'TelefonnummerZwei' : 0                                #Einstellung 116
                ,'KundenNrLeitstelle' :  0                              #Einstellung 117
                ,'FernTelNr' : 0                                        #Einstellung 118
                ,'FernTelNrZwei' : 0                                    #Einstellung 119
                ,'FernTelNrDrei' : 0                                    #Einstellung 120
                ,'CommsAcknowledge' : 0                                 #Einstellung 122
                ,'RueckstellenReport'  : 0                              #Einstellung 123
                ,'OpenClose' : 0                                        #Einstellung 124
                ,'KeinSignalGeschlossen' : 0                            #Einstellung 125
                ,'SpracheinstellungOSDMenu' : 6                         #Einstellung 126
                ,'ExternAlarm' : 0                                      #Einstellung 128
                ,'ExternDeaktivieren' : 0                               #Einstellung 129
                ,'SIAReportModus' : 0                                   #Einstellung 131
                ,'SendeSaboEinbruch' : 0                                #Einstellung 132
                ,'SIARst' : 0                                           #Einstellung 133        EIGENTLICH 132
                ,'ContactIDReportRst' : 0                               #EInstellung 143
                ,'VerhaltenZusaetzSchaltausgangEins' : 0                #Einstellung 151
                ,'VerhaltenZusaetzSchaltausgangZwei' : 0                #Einstellung 152
                ,'VerhaltenZusaetzSchaltausgangDrei': 0                 #Einstellung 153
                ,'VerhaltenZusaetzSchaltausgangVier': 0                 #Einstellung 154
                ,'VerhaltenZusaetzSchaltausgangFuenf': 0                #Einstellung 155
                ,'VerhaltenZusaetzSchaltausgangSechs': 0                #Einstellung 156
                ,'VerhaltenZusaetzSchaltausgangSieben': 0               #Einstellung 157
                ,'VerhaltenZusaetzSchaltausgangAcht': 0                 #Einstellung 158
                ,'InversionZusaetzSchaltausgang' : 0                    #Einstellung 159
                ,'ZeitbestaetigterAlarm' : 0                            #Einstellung 160
                ,'BestaetigenInternerLautsprecher' : 0                  #Einstellung 161
                ,'BestaetigenExterneSirene' : 0                         #Einstellung 162
                ,'BestaetigenAlarmEintritt' : 0                         #Einstellung 163
                ,'BenutzerResetnachAlarm' : 0                           #Einstellung 164
                ,'DauerAktivImpulsEinsBisVier' : 0                      #Einstellung 170
                ,'Schaltausgangaktivstabil' : 0                         #Einstellung 171
                ,'DauerDeaktivImpulsEIns' : 0                           #Einstellung 172
                ,'Schaltausgangdeaktivstabil' : 0                       #Einstellung 173
                ,'SchaltausgangFeuer' : 0                               #Einstellung 174
                ,'SchaltausgangUeberfall' : 0                           #Eisntellung 175
                ,'WachtCode' : 0                                        #Einstellung 181
                ,'LetzerAusgangSettlingZeit' : 7                        #Einstellung 182
                ,'DisplayZeileaendern' : 0                               #Einstellung 183
                ,'FeuerSignalgeber' : 0                                 #Einstellung 184
                ,'SchluesselschalterAutoReset' : 0                      #Einstellung 185
                ,'AnzahlHomeBeepRuf' : 00                               #Einstellung 186
                ,'FastFormatKanalEins' : 00                             #Einstellung 191
                ,'FastFormatKanalZwei':  00                             #Einstellung 192
                ,'FastFormatKanalDrei' : 00                             #Eisntellung 193
                ,'FastFormatKanalVier' : 00                             #Einstellung 194
                ,'FastFormatKanalFuenf': 00                             #Einstellung 195
                ,'FastFormatKanalSechs': 00                             #Einstellung 196
                ,'FastFormatKanalSieben': 00                            #Eisntellung 197
                ,'FastFormatKanalAcht': 00                              #Einstellung 198
                ,'AnzeigeZonenwiederstand' : 0                          #Einstellung 199
                ,'FobikoblerEintrittzeit' : 1                           #Einstellung 200
                ,'EingangsverzoegerungGruppeEins' : 1                   #Einstellung 201
                ,'PartioniertenSystem' : 0                              #Allgemeine Einstellung
            }
            with open(CreateFile, 'w') as ConfigFile:
                json.dump(json_obj, ConfigFile)
            print("File wurde erstellt!")
            ConfigFile.close()
    else:
        os.mkdir(FolderPathLocalTerxon)
        print("Ordner wurde erstellt!")
        StartConfigurationFile(2)

StartConfigurationFile(1)

def ReloadConfig(x):
         with open(ConfigPath, 'r') as ConfigFile:
            data = json.load(ConfigFile)


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
ZonenNummer = ""                                    #Einstellung 001
sZonenNummer =  ""                                  #Einstellung 001
ZonenEinstellungen = "Zone "                        #Einstellung 001
ZonenEinstellungenFunk = "Funk Zone "               #Einstellung Funk X17-X32

#Terxon Config load



BereichID = 1000
ModusName = ""
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
    print (internCode)

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
    internCode = internCode + str(x) +  "#"
    TxtValue = TxtValue + str(x)
    CodeTxt.set(TxtValue)
    XID = 1
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
    global internCode
    internCode = ""
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
    HID = 0
    XID = 0
    AID = 0
    BID = 0
    CID = 0
    DID = 0
    XID = 0
    AusgabeEins.config(text=str(""))
    AusgabeZwei.config(text=str(""))
    Code = ""
    TxtValue = ""
    CodeTxt.set(TxtValue)
    print("Eingabe gelöscht", "CodeTxt Wert: ", CodeTxt, "TxtValue Wert: ",TxtValue)

def VarNull(x):
    global XID
    global HID
    global AID
    global BID
    global CID
    global DID
    AID = 0
    BID = 0
    CID = 0
    DID = 0
    XID = 0
    HID = 0

def ConfirmEntrance(q):
    global TxtValue
    global BereichID
    global AusgabeText
    global sZonenNummer
    global XID
    global HID
    global AID
    global BID
    global CID
    global DID
    global internCode
    print(AID)
    if XID == 1:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        XID = 2
        lTxtValue = len(TxtValue)
        if lTxtValue == 0: TxtValue = "0"
    elif HID == 1:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        HID = 2
        lTxtValue = len(TxtValue)
        if lTxtValue == 0: TxtValue = "0"
    elif AID == 1:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        AID = 2
        lTxtValue = len(TxtValue)
        if lTxtValue == 0: TxtValue = "0"
    elif BID == 1:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        BID = 2
        lTxtValue = len(TxtValue)
        if lTxtValue == 0: TxtValue = "0"
        print(TxtValue)
    elif CID == 1:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        CID = 2
        lTxtValue = len(TxtValue)
        if lTxtValue == 0: TxtValue = "0"
    elif DID == 1:
        ohneX = internCode.split("#")
        TxtValue = ohneX[1]
        DID = 2
        lTxtValue = len(TxtValue)
        if lTxtValue == 0: TxtValue = "0"


    iTxtValue= int(TxtValue)
    CodeLenght = len(TxtValue)
    print("def: ConfirmEntrance")
    NullFront = "%03d" % (iTxtValue)
    print(NullFront)
    NullCodeLenght = len(NullFront)
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
            AusgabeEins.config(text=str("Programmiermodus"))
            AusgabeZwei.config(text=str("Passwort richtig"))
            Delete(1)
            BereichID = 7890
            print("BereichID: ", BereichID)
    elif BereichID == 7890:
        print("Menüpunkt-Code")
        MenüPunkte(iTxtValue)
    elif BereichID < 250:
        print("<250")
        EinstellungsPunkte(iTxtValue, CodeLenght, sZonenNummer)
    if TxtValue == "" and XID == 2 or AID == 2 or BID == 2 or CID == 2 or DID == 2:
        print("XABCD")

@functools.lru_cache(maxsize=None)
def MenüPunkte(Menüpunkt):
    global TxtValue
    global BereichID
    global ZonenNummer
    #global sZoneNummer
    global XID
    global AID
    global HID
    global BID
    global CID
    global DID

    #ReloadConfig(1)
    if Menüpunkt == 0:
        print("Menüpunkt: 000")
        AusgabeEins.config(text=str("Menüpunkt: 000"))
        AusgabeZwei.config(text=str(LänderEinstellung))
        BereichID = 0
        Delete(1)
    elif Menüpunkt >= 1 and Menüpunkt <= 16:
        print("Menüpunkt: 001 - 016")
        ZonenNummer = Menüpunkt
        sZonenNummer = str(Menüpunkt)
        AusgabeEins.config(text=str("Menüpunkt: 001 -016 | Draht-Zoneneinstellung"))
        AusgabeZwei.config(text=str(ZonenEinstellungen + sZonenNummer + ZonenEinstellungenDef))
        BereichID = 1
        Delete(1)
    elif Menüpunkt >=17 and Menüpunkt <= 32 and XID == 2:
        ZonenNummer = Menüpunkt
        sZonenNummer = str(Menüpunkt)
        AusgabeEins.config(text=str("Menüpunkt: 001 -016 | Funk-Zoneneinstellung"))
        AusgabeZwei.config(text=str(ZonenEinstellungen + sZonenNummer + ZonenEinstellungenFunkDef))
        BereichID = 17
        Delete(1)
        XID = 0
    elif Menüpunkt == 20:
        text = str(Programmiercode)
        print("Menüpunkt: 020")
        AusgabeEins.config(text=str("Menüpunkt: 020 | Programmiercode"))
        AusgabeZwei.config(text=str("Programmiercode: "+ text))
        BereichID = 20
        Delete(1)
    elif Menüpunkt == 21:
        print("Menüpunkt: 021")
        AusgabeEins.config(text=str("Menüpunkt: 021 | Zonenabschluss"))
        text = str(ZonenAbschlussNummer)
        if ZonenAbschlussNummer == 0:
            AusgabeZwei.config(text=str(text + " - Kein Widerstand NC"))
        elif ZonenAbschlussNummer == 1:
            AusgabeZwei.config(text=str(text + " - Zwei Widerstände DEOL"))
        BereichID = 21
        Delete(1)
    elif Menüpunkt == 22:
        print("Menüpunkt: 022")
        AusgabeEins.config(text=str("Menüpunkt: 022 | Intern Volume"))
        if InterVolumeNummer == 0:
            AusgabeZwei.config(text=str("Volumen ist: aus"))
        else:
            AusgabeZwei.config(text=str("Volumen ist: " + InterVolumeNummer))
        BereichID = 22
        Delete(1)
    elif Menüpunkt == 23:
        print("Menüpunkt: 023")
        AusgabeEins.config(text=str("Menüpunkt: 023 | Fern Reset"))
        if FernReset == 0:
            AusgabeZwei.config(text=str(FernReset + " AUS"))
        else:
            AusgabeZwei.config(text=str(FernReset + " EIN"))
        BereichID = 23
        Delete(1)
    elif Menüpunkt == 24:
        print("Menüpunkt: 024")
        AusgabeEins.config(text=str("Menüpunkt: 024 | Anzeige Kundename"))
        AusgabeZwei.config(text=str(Kundenname))
        BereichID = 24
        Delete(1)
    elif Menüpunkt == 25:
        print("Menüpunkt: 025")
        Text = str(InternerAlarm)
        AusgabeEins.config(text=str("Menüpunkt: 025 | Interner Alarm"))
        if InternerAlarm == 1:
            AusgabeZwei.config(text=str(Text + " Bis deaktivieren"))
        elif InternerAlarm == 0:
            AusgabeZwei.config(text=str(Text + " Lokal Alarm folgend"))
        BereichID = 25
        Delete(1)
    elif Menüpunkt == 27:
        print("Menüpunkt: 027")
        AusgabeEins.config(text=str("Menüpunkt: 027 | Alarm bei fehlg. Aktivierung"))
        Text = str(AlarmbeiAktivierung)
        if AlarmbeiAktivierung == 0:
            AusgabeZwei.config(text=str(Text + " - Interner Alarm"))
        elif AlarmbeiAktivierung == 1:
            AusgabeZwei.config(text=str(Text + " - Lokaler Alarm"))
        BereichID = 27
        Delete(1)
    elif Menüpunkt == 28:
        print("Menüpunkt: 028")
        AusgabeEins.config(text=str("Menüpunkt: 028 | Status Anzeige ausblenden"))
        Text = str(StatusAnzeigeAusblenden)
        if StatusAnzeigeAusblenden == 0:
            AusgabeZwei.config(text=str(Text + " - Nie ausblenden"))
        elif StatusAnzeigeAusblenden == 1:
            AusgabeZwei.config(text=str(Text + " - Nach180 Sek ausblenden"))
        elif StatusAnzeigeAusblenden == 2:
            AusgabeZwei.config(text=str(Text + " - 30Sek nach Code ausblenden"))
        BereichID = 28
        Delete(1)
    elif Menüpunkt == 29:
        print("Menüpunkt: 029")
        AusgabeEins.config(text=str("Menüpunkt: 029 | Extern Alarm Verzögern"))
        Text = str(ExternAlarmVerzoegerung)
        if ExternAlarmVerzoegerung == 0:
            AusgabeZwei.config(text=str(Text + " - Aus"))
        if ExternAlarmVerzoegerung == 1:
            AusgabeZwei.config(text=str(Text + " - An"))
        BereichID = 29
        Delete(1)
    elif Menüpunkt == 30:
        print("Menüpunkt: 030")
        AusgabeEins.config(text=str("Menüpunkt: 030 | Überfallalarm"))
        Text = str(Ueberfallalarm)
        if Ueberfallalarm == 0:
            AusgabeZwei.config(text=str( Text + " - Laut"))
        elif Ueberfallalarm == 1:
            AusgabeZwei.config(text=str( Text + " - Still"))
        BereichID = 30
        Delete(1)
    elif Menüpunkt == 31:
        print("Menüpunkt: 031")
        Text = str(ZonenSabotageReset)
        AusgabeEins.config(text=str("Menüpunkt: 031 | Zonensabotage Reset"))
        if ZonenSabotageReset == 0:
            AusgabeZwei.config(text=str(Text + " - Keine Programmcode notw."))
        elif ZonenSabotageReset == 1:
            AusgabeZwei.config(text=str(Text + " - Programmiercode notw."))
        BereichID = 31
    elif Menüpunkt == 32:
        print("Menüpunkt: 032")
        Text = str(BedienteileundPartitionen)
        AusgabeEins.config(text=str("Menüpunkt: 032 | Bedienteile u. Partitionen"))
        if BedienteileundPartitionen == 1:
            AusgabeZwei.config(text=str(Text + " - Zuweisung Bedienteil zu Partition A"))
        elif BedienteileundPartitionen == 2:
            AusgabeZwei.config(text=str(Text + " - Zuweisung Bedienteil zu Partition B"))
        elif BedienteileundPartitionen == 3:
            AusgabeZwei.config(text=str(Text + " - Zuweisung Bedienteil zu Partition C"))
        elif BedienteileundPartitionen == 4:
            AusgabeZwei.config(text=str(Text + " - Zuweisung Bedienteil zu Partition D"))
        BereichID = 32
        Delete(1)
    elif Menüpunkt == 33:
        print("Menüpunkt: 033")
        Text = str(SystemReset)
        AusgabeEins.config(text=str("Menüpunkt: 033 | System Reset"))
        if SystemReset == 0:
            AusgabeZwei.config(text=str(Text + " - Keine Programmcode notw."))
        elif SystemReset == 1:
            AusgabeZwei.config(text=str(Text + " - Programmiercode notw."))
        BereichID = 33
    elif Menüpunkt == 34:
        print("Menüpunkt: 034")
        Text = str(UeberfallReset)
        AusgabeEins.config(text=str("Menüpunkt: 034 | Überfall Reset"))
        if SystemReset == 0:
            AusgabeZwei.config(text=str(Text + " - Benutzer Reset"))
        elif SystemReset == 1:
            AusgabeZwei.config(text=str(Text + " - Programmier Reset"))
        BereichID = 34
    elif Menüpunkt == 35:
        print("Menüpunkt: 035")
        Text = str(ErstmelderAlarmausblenden)
        AusgabeEins.config(text=str("Menüpunkt: 035 | Erstmelder Alarm ausblenden"))
        if ErstmelderAlarmausblenden == 0:
            AusgabeZwei.config(text=str(Text + " - Erstmelder ausblenden "))
        elif ErstmelderAlarmausblenden == 1:
            AusgabeZwei.config(text=str(Text + " - Erstmelder überwachen "))
        BereichID = 35
    elif Menüpunkt == 36:
        print("Menüpunkt: 036")
        Text = str(AlarmAbbruch)
        AusgabeEins.config(text=str("Menüpunkt: 036 | Alarm Abbruch"))
        if AlarmAbbruch == 0:
            AusgabeZwei.config(text=str(Text + " - Benutzer kann Falschalarm nicht abbrechen"))
        elif AlarmAbbruch == 1:
            AusgabeZwei.config(text=str(Text + " - Benutzer kann Falschalarm abbrechen  "))
        BereichID = 36
    elif Menüpunkt == 37:
        print("Menüpunkt: 037")
        Text = str(SabotageReportdeaktiv)
        AusgabeEins.config(text=str("Menüpunkt: 037 | Alarm Abbruch"))
        if SabotageReportdeaktiv == 0:
            AusgabeZwei.config(text=str(Text + " - Nur Intern "))
        elif SabotageReportdeaktiv == 1:
            AusgabeZwei.config(text=str(Text + " - Intern + Leitstelle   "))
        BereichID = 37
    elif Menüpunkt == 38:
        print("Menüpunkt: 038")
        Text = str(SystemsabotageReset)
        AusgabeEins.config(text=str("Menüpunkt: 038 | Alarm Abbruch"))
        if SystemsabotageReset == 0:
            AusgabeZwei.config(text=str(Text + " - Benutzer Reset  "))
        elif SystemsabotageReset == 1:
            AusgabeZwei.config(text=str(Text + " - Programmier Reset"))
        BereichID = 38
    elif Menüpunkt == 39:
        print("Menüpunkt: 039")
        Text = str(AusgangsmodusBereichA)
        AusgabeEins.config(text=str("Menüpunkt: 039 | Ausgangsmodus für Gesamtbereich A"))
        if AusgangsmodusBereichA == 0:
            AusgabeZwei.config(text=str(Text + " - Ausgangszeit"))
        elif AusgangsmodusBereichA == 1:
            AusgabeZwei.config(text=str(Text + " - Manuell "))
        if AusgangsmodusBereichA == 2:
            AusgabeZwei.config(text=str(Text + " - Letzte Tür "))
        elif AusgangsmodusBereichA == 3:
            AusgabeZwei.config(text=str(Text + " - Schlüsselschalter"))
        if AusgangsmodusBereichA == 13:
            AusgabeZwei.config(text=str(Text + " - Sofort"))
        elif AusgangsmodusBereichA == 14:
            AusgabeZwei.config(text=str(Text + " - Still "))
        elif AusgangsmodusBereichA == 15:
            AusgabeZwei.config(text=str(Text + " - Schlüsselschalter"))
        BereichID = 39
        Delete(1)
    elif Menüpunkt == 40:
        print("Menüpunkt: 040")
        Text = str(SystemAutoAktivnachAlarm)
        AusgabeEins.config(text=str("Menüpunkt: 040 | System Auto Aktiv nach Alarm"))
        if SystemAutoAktivnachAlarm == 0:
            AusgabeZwei.config(text=str(Text + " - Nie"))
        elif SystemAutoAktivnachAlarm == 1:
            AusgabeZwei.config(text=str(Text + " - Einmal"))
        if SystemAutoAktivnachAlarm == 2:
            AusgabeZwei.config(text=str(Text + " - Zweimal"))
        elif SystemAutoAktivnachAlarm == 3:
            AusgabeZwei.config(text=str(Text + " - Dreimal"))
        if SystemAutoAktivnachAlarm == 4:
            AusgabeZwei.config(text=str(Text + " - Immmer"))
        BereichID =40
        Delete(1)
    elif Menüpunkt == 41:
        print("Menüpunkt: 041")
        Text = str(SirenenVerzögerung)
        AusgabeEins.config(text=str("Menüpunkt: 041 | Sirenen Verzögerung"))
        if SirenenVerzögerung == 0:
            AusgabeZwei.config(text=str(Text + " - Keine Verzögerung"))
        elif SirenenVerzögerung == 1:
            AusgabeZwei.config(text=str(Text + " - 1,5 Min Verzögerung"))
        if SirenenVerzögerung == 2:
            AusgabeZwei.config(text=str(Text + " - 3 Min Verzögerung"))
        elif SirenenVerzögerung == 3:
            AusgabeZwei.config(text=str(Text + " - 5 Min Verzögerung"))
        if SirenenVerzögerung == 4:
            AusgabeZwei.config(text=str(Text + " - 10 Min Verzögerung "))
        elif SirenenVerzögerung == 5:
            AusgabeZwei.config(text=str(Text + " - 15 Min Verzögerung"))
        elif SirenenVerzögerung == 6:
            AusgabeZwei.config(text=str(Text + " - 20 Min Verzögerung "))
        BereichID = 41
        Delete(1)
    elif Menüpunkt == 42:
        print("Menüpunkt: 042")
        Text = str(Sirenendauer)
        AusgabeEins.config(text=str("Menüpunkt: 042 | Sirenendauer"))
        if Sirenendauer == 1:
            AusgabeZwei.config(text=str(Text + " - 1,5 Min "))
        elif Sirenendauer == 2:
            AusgabeZwei.config(text=str(Text + " - 3 Min"))
        if Sirenendauer == 3:
            AusgabeZwei.config(text=str(Text + " - 5 Min"))
        elif Sirenendauer == 4:
            AusgabeZwei.config(text=str(Text + " - 10 Min"))
        if Sirenendauer == 5:
            AusgabeZwei.config(text=str(Text + " - 15 Min"))
        elif Sirenendauer == 6:
            AusgabeZwei.config(text=str(Text + " - 20 Min "))
        BereichID = 42
        Delete(1)
    elif Menüpunkt == 44:
        print("Menüpunkt: 044")
        Text = str(AusgangszeitGesamtbereich)
        AusgabeEins.config(text=str("Menüpunkt: 044 | Ausgangszeit Gesamtbereich"))
        if AusgangszeitGesamtbereich == 1:
            AusgabeZwei.config(text=str(Text + " - 10 Sek"))
        elif AusgangszeitGesamtbereich == 2:
            AusgabeZwei.config(text=str(Text + " - 20 Sek"))
        if AusgangszeitGesamtbereich == 3:
            AusgabeZwei.config(text=str(Text + " - 30 Sek"))
        elif AusgangszeitGesamtbereich == 4:
            AusgabeZwei.config(text=str(Text + " - 45 Sek"))
        if AusgangszeitGesamtbereich == 5:
            AusgabeZwei.config(text=str(Text + " - 60 Sek"))
        elif AusgangszeitGesamtbereich == 6:
            AusgabeZwei.config(text=str(Text + " - 120 Sek "))
        BereichID = 44
        Delete(1)
    elif Menüpunkt == 45:
        print("Menüpunkt: 045")
        Text = "Lautstärke = "
        sEinAusgagsverzögerungVolumen = str(EinAusgagsverzögerungVolumen)
        AusgabeEins.config(text=str("Menüpunkt: 045 | Ein/Ausgangsverzögerung Volume "))
        if EinAusgagsverzögerungVolumen == 0:
            AusgabeZwei.config(text=str(Text + sEinAusgagsverzögerungVolumen + " Kein Signal"))
        elif EinAusgagsverzögerungVolumen >= 1 and EinAusgagsverzögerungVolumen < 10:
            AusgabeZwei.config(text=str(Text + sEinAusgagsverzögerungVolumen))
        BereichID = 45
        Delete(1)
    elif Menüpunkt == 46:
        print("Menüpunkt: 046")
        Text = str(SabotagealarmReaktion)
        AusgabeEins.config(text=str("Menüpunkt: 044 | Sabotagealarm Reaktion"))
        if SabotagealarmReaktion == 0:
            AusgabeZwei.config(text=str(Text + " Internalarm"))
        elif SabotagealarmReaktion == 1:
            AusgabeZwei.config(text=str(Text + " - Bedienteil "))
        elif SabotagealarmReaktion == 2:
            AusgabeZwei.config(text=str(Text + " - Intern + Bedienteil "))
        BereichID = 46
        Delete(1)
    elif Menüpunkt == 47:
        print("Menüpunkt: 047")
        Text = str(PartionAAlarmReaktion)
        AusgabeEins.config(text=str("Menüpunkt: 047 | Partition A Alarm Reaktion"))
        if PartionAAlarmReaktion == 0:
            AusgabeZwei.config(text=str(Text + " Bedienteilalarm "))
        elif PartionAAlarmReaktion == 1:
            AusgabeZwei.config(text=str(Text + " - Bed.-teil + Lautsprecher  "))
        elif PartionAAlarmReaktion == 2:
            AusgabeZwei.config(text=str(Text + " - Bed.-teil + LS + Wählgerät "))
        BereichID = 47
        Delete(1)
    elif Menüpunkt == 48:
        print("Menüpunkt: 048")
        Text = str(Bedienteilsperre)
        AusgabeEins.config(text=str("Menüpunkt: 048 | Partition A Alarm Reaktion"))
        if Bedienteilsperre == 0:
            AusgabeZwei.config(text=str(Text + " AUS"))
        elif Bedienteilsperre == 1:
            AusgabeZwei.config(text=str(Text + " - AN"))
        BereichID = 48
        Delete(1)
    elif Menüpunkt == 51:
        print("Menüpunkt: 051")
        AusgabeEins.config(text=str("Menüpunkt: 051 | Datum und Uhrzeit"))
        AusgabeZwei.config(text=str(datetime.today().strftime('%Y-%m-%d %H:%M')))
        BereichID = 51
        Delete(1)
    Delete(1)
    print(MenüPunkte.cache_info())

@functools.lru_cache(maxsize=None)
def EinstellungsPunkte(iTxtValue, CodeLenght, sZonenNummer):
    global TxtValue
    global CodeTxt
    global BereichID
    global XID
    global HakenID
    #global ZonenNummer
    #global sZonenNummer
    global ModusName
    print(sZonenNummer)
    if BereichID == 0 and CodeLenght > 0 and CodeLenght <= 2:
        if iTxtValue == 0 and XID == 0:
            LaenderEinstellung = "UK – Großbritannien "
            data["LaenderEinstellung"] = "UK – Großbritannien "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 1 and XID == 0:
            LaenderEinstellung = "I – Italien"
            data["LaenderEinstellung"] = "I – Italien "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 2 and XID == 0:
            LaenderEinstellung = "EE – Spanien"
            data["LaenderEinstellung"] = "EE – Spanien "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 3 and XID == 0:
            LaenderEinstellung = "P – Portugal"
            data["LaenderEinstellung"] = "P – Portugal "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 4 and XID == 0:
            LaenderEinstellung = "NL – Niederlande"
            data["LaenderEinstellung"] = "NL – Niederlande "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 5 and XID == 0:
            LaenderEinstellung = "FR – Frankreich"
            data["LaenderEinstellung"] = "FR – Frankreich "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 6 and XID == 0:
            LaenderEinstellung = "B – Belgien"
            data["LaenderEinstellung"] = "B – Belgien "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 7 and XID == 0:
            LaenderEinstellung = "D – Deutschland"
            data["LaenderEinstellung"] = "D – Deutschland "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 8 and XID == 0:
            LaenderEinstellung = "CH – Schweiz"
            data["LaenderEinstellung"] = "CH – Schweiz "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 9 and XID == 0:
            LaenderEinstellung = "A – Österreich"
            data["LaenderEinstellung"] = "A – Österreich "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 1 and XID == 2:
            LaenderEinstellung = "IRL – Irland"
            data["LaenderEinstellung"] = "IRL – Irland "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 2 and XID == 2:
            LaenderEinstellung = "OEM1"
            data["LaenderEinstellung"] = "OEM1 "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 3 and XID == 2:
            LaenderEinstellung = "OEM2"
            data["LaenderEinstellung"] = "OEM2 "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 4 and XID == 2:
            LaenderEinstellung = "FI – Finnland"
            data["LaenderEinstellung"] = "FI – Finnland "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 5 and XID == 2:
            LaenderEinstellung = "N – Norwegen"
            data["LaenderEinstellung"] = "N – Norwegen "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 6 and XID == 2:
            LaenderEinstellung = "DK – Dänemark"
            data["LaenderEinstellung"] = "DK – Dänemark "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        elif iTxtValue == 7 and XID == 2:
            LaenderEinstellung = "S – Schweden "
            data["LaenderEinstellung"] = "S – Schweden "
            AusgabeZwei.config(text=str(LaenderEinstellung))
        Delete(1)
        BereichID = 7890
    elif BereichID == 1 and CodeLenght > 0 and CodeLenght <= 2:
        if iTxtValue == 0 and XID == 0 and BID == 0 and CID == 0 and DID == 0:
            data["ZonenEinstellungenDef"] = " NV – Nicht verwendet"
            Text = ZonenEinstellungen + sZonenNummer + " NV – Nicht verwendet"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 1 and XID == 0:
            data["ZonenEinstellungenDef"] = " UF – Überfall"
            Text = ZonenEinstellungen + sZonenNummer + " UF – Überfall"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 2 and XID == 0:
            data["ZonenEinstellungenDef"] = " FE -Feuer "
            Text = ZonenEinstellungen + sZonenNummer + " FE -Feuer "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 3 and XID == 0:
            data["ZonenEinstellungenDef"] = " SO - Sofort "
            Text = ZonenEinstellungen + sZonenNummer + " SO - Sofort "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 4 and XID == 0:
            data["ZonenEinstellungenDef"] = " 24 -24 Stunden"
            Text = ZonenEinstellungen + sZonenNummer + " 24 -24 Stunden"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 5 and XID == 0:
            data["ZonenEinstellungenDef"] = " EA -Ein/Ausgang"
            Text = ZonenEinstellungen + sZonenNummer +  " EA -Ein/Ausgang"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 6 and XID == 0:
            data["ZonenEinstellungenDef"] = " EF -Eingang folgend"
            Text = ZonenEinstellungen + sZonenNummer + " EF -Eingang folgend"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 7 and XID == 0:
            data["ZonenEinstellungenDef"] = " ES - Erschütterungssensor"
            Text = ZonenEinstellungen + sZonenNummer + " ES - Erschütterungssensor"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 8 and XID == 0:
            data["ZonenEinstellungenDef"] = " TK - Technik "
            Text = ZonenEinstellungen + sZonenNummer + ZonenEinstellungenDef
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 9 and XID == 0:
            data["ZonenEinstellungenDef"] = " SK - Schlüsselkasten "
            Text = ZonenEinstellungen + sZonenNummer + " SK - Schlüsselkasten "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 10 and XID == 0:
            data["ZonenEinstellungenDef"] = " BM - Brandmelder "
            Text = ZonenEinstellungen + sZonenNummer + " BM - Brandmelder "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 11 and XID == 0:
            data["ZonenEinstellungenDef"] = " SS - Schlüssekschalter "
            Text = ZonenEinstellungen + sZonenNummer + " SS - Schlüssekschalter "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 12 and XID == 0:
            data["ZonenEinstellungenDef"] = " BS - Blockschloss "
            Text = ZonenEinstellungen + sZonenNummer + " BS - Blockschloss "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 13 and XID == 0:
            data["ZonenEinstellungenDef"] = " AM - Anti Mask "
            Text = ZonenEinstellungen + sZonenNummer + " AM - Anti Mask "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 14 and XID == 0:
            data["ZonenEinstellungenDef"] = " FB - Forbikobler Zone "
            Text = ZonenEinstellungen + sZonenNummer + " FB - Forbikobler Zone "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 1 and XID == 2:
            data["ZonenEinstellungenDef"] = " C - Türgong "
            Text = ZonenEinstellungen + sZonenNummer + " C - Türgong "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 2 and XID == 2:
            data["ZonenEinstellungenDef"] = " S - Melderset "
            Text = ZonenEinstellungen + sZonenNummer + " S - Melderset "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 3 and XID == 2:
            data["ZonenEinstellungenDef"] = " D - Doppelauslösung "
            Text = ZonenEinstellungen + sZonenNummer + " D - Doppelauslösung "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 4 and XID == 2:
            data["ZonenEinstellungenDef"] = " EF -Eingang folgend"
            Text = ZonenEinstellungen + sZonenNummer + " EF -Eingang folgend"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 7 and XID == 2:
            data["ZonenEinstellungenDef"] = " 1....6 Empfindlichkeit "
            Text = ZonenEinstellungen + sZonenNummer + " 1....6 Empfindlichkeit "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif BID == 2:
            data["ZonenEinstellungenDef"] = " Überwacht im Bereich B "
            Text = ZonenEinstellungen + sZonenNummer + " Überwacht im Bereich B "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif CID == 2:
            data["ZonenEinstellungenDef"] = " Überwacht im Bereich C "
            Text = ZonenEinstellungen + sZonenNummer + " Überwacht im Bereich C "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif DID == 2:
            data["ZonenEinstellungenDef"] = " Überwacht im Bereich D "
            Text = ZonenEinstellungen + sZonenNummer + " Überwacht im Bereich D "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
    elif BereichID == 17 and CodeLenght > 0 and CodeLenght <= 2:
        if iTxtValue == 0 and XID == 0 and BID == 0 and CID == 0 and DID == 0:
            data["ZonenEinstellungenFunkDef"] = " NV – Nicht verwendet"
            Text = ZonenEinstellungenFunk + sZonenNummer + " NV – Nicht verwendet"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 1 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " UF – Überfall"
            Text = ZonenEinstellungenFunk + sZonenNummer + " UF – Überfall"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 2 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " FE -Feuer "
            Text = ZonenEinstellungenFunk + sZonenNummer + " FE -Feuer "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 3 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " SO - Sofort "
            Text = ZonenEinstellungenFunk + sZonenNummer + " SO - Sofort "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 4 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " 24 -24 Stunden"
            Text = ZonenEinstellungenFunk + sZonenNummer + " 24 -24 Stunden"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 5 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " EA -Ein/Ausgang"
            Text = ZonenEinstellungenFunk + sZonenNummer + " EA -Ein/Ausgang"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 6 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " EF -Eingang folgend"
            Text = ZonenEinstellungenFunk + sZonenNummer + " EF -Eingang folgend"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 7 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " ES - Erschütterungssensor"
            Text = ZonenEinstellungenFunk + sZonenNummer + " ES - Erschütterungssensor"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 8 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " TK - Technik "
            Text = ZonenEinstellungenFunk + sZonenNummer + ZonenEinstellungenDef
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 9 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " SK - Schlüsselkasten "
            Text = ZonenEinstellungenFunk + sZonenNummer + " SK - Schlüsselkasten "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 10 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " BM - Brandmelder "
            Text = ZonenEinstellungenFunk + sZonenNummer + " BM - Brandmelder "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 11 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " SS - Schlüssekschalter "
            Text = ZonenEinstellungenFunk + sZonenNummer + " SS - Schlüssekschalter "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 12 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " BS - Blockschloss "
            Text = ZonenEinstellungenFunk + sZonenNummer + " BS - Blockschloss "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 13 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " AM - Anti Mask "
            Text = ZonenEinstellungenFunk + sZonenNummer + " AM - Anti Mask "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 14 and XID == 0:
            data["ZonenEinstellungenFunkDef"] = " FB - Forbikobler Zone "
            Text = ZonenEinstellungenFunk + sZonenNummer + " FB - Forbikobler Zone "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 1 and XID == 2:
            data["ZonenEinstellungenFunkDef"] = " C - Türgong "
            Text = ZonenEinstellungenFunk + sZonenNummer + " C - Türgong "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 2 and XID == 2:
            data["ZonenEinstellungenFunkDef"] = " S - Melderset "
            Text = ZonenEinstellungenFunk + sZonenNummer + " S - Melderset "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 3 and XID == 2:
            data["ZonenEinstellungenFunkDef"] = " D - Doppelauslösung "
            Text = ZonenEinstellungenFunk + sZonenNummer + " D - Doppelauslösung "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 4 and XID == 2:
            data["ZonenEinstellungenFunkDef"] = " EF -Eingang folgend"
            Text = ZonenEinstellungenFunk + sZonenNummer + " EF -Eingang folgend"
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif iTxtValue == 7 and XID == 2:
            data["ZonenEinstellungenFunkDef"] = " 1....6 Empfindlichkeit "
            Text = ZonenEinstellungenFunk + sZonenNummer + " 1....6 Empfindlichkeit "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif BID == 2:
            data["ZonenEinstellungenFunkDef"] = " Überwacht im Bereich B "
            Text = ZonenEinstellungenFunk + sZonenNummer + " Überwacht im Bereich B "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif CID == 2:
            data["ZonenEinstellungenFunkDef"] = " Überwacht im Bereich C "
            Text = ZonenEinstellungenFunk + sZonenNummer + " Überwacht im Bereich C "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
        elif DID == 2:
            data["ZonenEinstellungenFunkDef"] = " Überwacht im Bereich D "
            Text = ZonenEinstellungenFunk + sZonenNummer + " Überwacht im Bereich D "
            AusgabeZwei.config(text=str(Text))
            Delete(1)
    elif BereichID == 20:
        Programmiercode = iTxtValue
        data["Programmiercode"] = iTxtValue
        Text = str(Programmiercode)
        print(Programmiercode)
        AusgabeZwei.config(text=str("Programmiercode gesetzt auf " + Text))
        Delete(1)
    elif BereichID == 21:
        if iTxtValue == 0:
            ZonenAbschlussNummer = 0
            data["ZonenAbschlussNummer"] = 0
            sZonenAbschlussNummer = str(ZonenAbschlussNummer)
            AusgabeZwei.config(text=str(sZonenAbschlussNummer + " = Kein Wiederstand NC"))
        elif iTxtValue == 1:
            ZonenAbschlussNummer = 1
            data["ZonenAbschlussNummer"] = 1
            sZonenAbschlussNummer = str(ZonenAbschlussNummer)
            AusgabeZwei.config(text=str(sZonenAbschlussNummer + " = Zwei Wiederstände DEOL"))
    elif BereichID == 22:
        InterVolumenNummer = iTxtValue
        SInternVolumenNummer = str(InterVolumenNummer)
        if iTxtValue == 0:
            Text = "Volumen ist Aus: " + SInternVolumenNummer
            AusgabeZwei.config(text=str(Text))
            data["InterVolumeNummer"] = iTxtValue
        else:
            Text = "Volumen ist: " + SInternVolumenNummer
            AusgabeZwei.config(text=str(Text))
            data["InterVolumeNummer"] = iTxtValue
        Delete(1)
    elif BereichID == 23:
        if iTxtValue == 0:
            FernReset = iTxtValue
            Text = str(FernReset)
            data["FernReset"] = iTxtValue
            AusgabeZwei.config(text=str(Text +  "AUS"))
        elif iTxtValue == 1:
            FernReset = iTxtValue
            Text = str(FernReset)
            data["FernReset"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " AN"))
    elif BereichID == 24 and XID == 2:
        BereichID = 7890
        AusgabeEins.config(text=str("Programmiermodus"))
    elif BereichID == 25:
        if iTxtValue == 1:
            InternerAlarm = 1
            Text = str(InternerAlarm)
            data["InternerAlarm"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " Lokal Alarm folgend"))
        elif iTxtValue == 0:
            InternerAlarm = 0
            Text = str(InternerAlarm)
            data["InternerAlarm"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " Bis deaktiviert"))
        Delete(1)
    elif BereichID == 27:
        if iTxtValue == 0:
            AlarmbeiAktivierung = 0
            Text = str(AlarmbeiAktivierung)
            data["AlarmbeiAktivierung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Intern Alarm"))
        elif iTxtValue == 1:
            AlarmbeiAktivierung = 1
            Text = str(AlarmbeiAktivierung)
            data["AlarmbeiAktivierung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Lokaler Alarm"))
    elif BereichID == 28:
        if iTxtValue == 0:
            StatusAnzeigeAusblenden = 0
            data["StatusAnzeigeAusblenden"] = iTxtValue
            Text = str(StatusAnzeigeAusblenden)
            AusgabeZwei.config(text=str(Text + " - Nie ausblenden"))
        elif iTxtValue == 1:
            StatusAnzeigeAusblenden = 1
            Text = str(StatusAnzeigeAusblenden)
            data["StatusAnzeigeAusblenden"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Nach 180 Sek ausblenden"))
        elif iTxtValue == 2:
            StatusAnzeigeAusblenden = 2
            Text = str(StatusAnzeigeAusblenden)
            data["StatusAnzeigeAusblenden"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 30Sek nach Code ausblenden"))
    elif BereichID == 29:
        if iTxtValue == 0:
            ExternAlarmVerzoegerung = 0
            Text = str(ExternAlarmVerzoegerung)
            data["ExternAlarmVerzoegerung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Aus"))
        elif iTxtValue == 1:
            ExternAlarmVerzoegerung = 1
            Text = str(ExternAlarmVerzoegerung)
            data["ExternAlarmVerzoegerung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - An"))
    elif BereichID == 30:
        if iTxtValue == 0:
            Ueberfallalarm = 0
            Text = str(Ueberfallalarm)
            data["Ueberfallalarm"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Laut"))
        elif iTxtValue == 1:
            Ueberfallalarm = 1
            Text = str(Ueberfallalarm)
            data["Ueberfallalarm"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Still"))
    elif BereichID == 31:
        if iTxtValue == 0:
            ZonenSabotageReset = 0
            Text = str(ZonenSabotageReset)
            data["ZonenSabotageReset"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Kein Program.code notw."))
        elif iTxtValue == 1:
            ZonenSabotageReset = 1
            Text = str(ZonenSabotageReset)
            data["ZonenSabotageReset"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Programmiercode notw."))
    elif BereichID == 32:
        if AID == 2:
            BedienteileundPartitionen = 1
            data["BedienteileundPartitionen"] = 1
            Text = "A"
            AusgabeZwei.config(text=str(Text + " - Zuweosimg Bedienteil zu Partition A"))
        elif BID == 2:
            BedienteileundPartitionen = 2
            data["BedienteileundPartitionen"] = 2
            Text = "B"
            AusgabeZwei.config(text=str(Text + " - Zuweosimg Bedienteil zu Partition B"))
        elif CID == 2:
            BedienteileundPartitionen = 3
            data["BedienteileundPartitionen"] = 3
            Text = "C"
            AusgabeZwei.config(text=str(Text + " - Zuweosimg Bedienteil zu Partition C"))
        elif DID == 2:
            BedienteileundPartitionen = 4
            data["BedienteileundPartitionen"] = 4
            Text = "D"
            AusgabeZwei.config(text=str(Text + " - Zuweosimg Bedienteil zu Partition D"))
    elif BereichID == 33:
        if iTxtValue == 0:
            SystemReset = 0
            Text = str(SystemReset)
            data["SystemReset"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Kein Program.code notw. "))
        elif iTxtValue == 1:
            SystemReset = 1
            Text = str(SystemReset)
            data["SystemReset"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Program.code notw. "))
    elif BereichID == 34:
        if iTxtValue == 0:
            UeberfallReset = 0
            Text = str(UeberfallReset)
            AusgabeZwei.config(text=str(Text + " - Kein Program.code notw. "))
        elif iTxtValue == 1:
            UeberfallReset = 1
            Text = str(UeberfallReset)
            AusgabeZwei.config(text=str(Text + " - Program.code notw. "))
    elif BereichID == 35:
        if iTxtValue == 0:
            ErstmelderAlarmausblenden = 0
            Text = str(ErstmelderAlarmausblenden)
            data["ErstmelderAlarmausblenden"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Erstmelder ausblenden"))
        elif iTxtValue == 1:
            ErstmelderAlarmausblenden = 1
            Text = str(ErstmelderAlarmausblenden)
            data["ErstmelderAlarmausblenden"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Erstmelder überwachen "))
    elif BereichID == 36:
        if iTxtValue == 0:
            AlarmAbbruch = 0
            Text = str(AlarmAbbruch)
            data["AlarmAbbruch"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Benutzer kann Falschalarm nicht abbrechen"))
        elif iTxtValue == 1:
            AlarmAbbruch = 1
            Text = str(AlarmAbbruch)
            data["AlarmAbbruch"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Benutzer kann Falschalarm abbrechen "))
    elif BereichID == 37:
        if iTxtValue == 0:
            SabotageReportdeaktiv = 0
            Text = str(SabotageReportdeaktiv)
            data["SabotageReportdeaktiv"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Benutzer kann Falschalarm nicht abbrechen"))
        elif iTxtValue == 1:
            SabotageReportdeaktiv = 1
            Text = str(SabotageReportdeaktiv)
            data["SabotageReportdeaktiv"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Benutzer kann Falschalarm abbrechen "))
    elif BereichID == 38:
        if iTxtValue == 0:
            SystemsabotageReset = 0
            Text = str(SystemsabotageReset)
            data["SystemsabotageReset"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Benutzer Reset"))
        elif iTxtValue == 1:
            SystemsabotageReset = 1
            Text = str(SystemsabotageReset)
            data["SystemsabotageReset"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Programmier Reset"))
    elif BereichID == 39:
        if iTxtValue == 0 and PartioniertenSystem == 0:
            AusgangsmodusBereichA = 0
            Text = str(AusgangsmodusBereichA)
            data["AusgangsmodusBereichA"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Ausgangszeit"))
        elif iTxtValue == 1 and PartioniertenSystem == 0:
            AusgangsmodusBereichA = 1
            Text = str(AusgangsmodusBereichA)
            data["AusgangsmodusBereichA"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Manuell"))
        elif iTxtValue == 2 and PartioniertenSystem == 0:
            AusgangsmodusBereichA = 2
            Text = str(AusgangsmodusBereichA)
            data["AusgangsmodusBereichA"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Letzte Tür"))
        elif iTxtValue == 3 and PartioniertenSystem == 0:
            AusgangsmodusBereichA = 3
            Text = str(AusgangsmodusBereichA)
            data["AusgangsmodusBereichA"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Sofort"))
        if iTxtValue == 3 and PartioniertenSystem == 0:
            Text = str(AusgangsmodusBereichA)
            data["AusgangsmodusBereichA"] = 13
            AusgabeZwei.config(text=str(Text + " - Still"))
        elif iTxtValue == 4 and PartioniertenSystem == 0:
            Text = str(AusgangsmodusBereichA)
            data["AusgangsmodusBereichA"] = 14
            AusgabeZwei.config(text=str(Text + " - Schlüsselschalter "))
        elif iTxtValue == 5 and PartioniertenSystem == 0:
            Text = str(AusgangsmodusBereichA)
            data["AusgangsmodusBereichA"] = 15
            AusgabeZwei.config(text=str(Text + " - Benutzer kann Falschalarm abbrechen "))
    elif BereichID == 40:
        if iTxtValue == 0:
            SystemAutoAktivnachAlarm = iTxtValue
            Text = str(SystemAutoAktivnachAlarm)
            data["SystemAutoAktivnachAlarm"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Nie"))
        elif iTxtValue == 1:
            SystemAutoAktivnachAlarm = iTxtValue
            Text = str(SystemAutoAktivnachAlarm)
            data["SystemAutoAktivnachAlarm"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Einmal"))
        if iTxtValue == 2:
            SystemAutoAktivnachAlarm = iTxtValue
            Text = str(SystemAutoAktivnachAlarm)
            data["SystemAutoAktivnachAlarm"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Zweimal"))
        elif iTxtValue == 3:
            SystemAutoAktivnachAlarm = iTxtValue
            Text = str(SystemAutoAktivnachAlarm)
            data["SystemAutoAktivnachAlarm"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Dreimal"))
        elif iTxtValue == 4:
            SystemAutoAktivnachAlarm = iTxtValue
            Text = str(SystemAutoAktivnachAlarm)
            data["SystemAutoAktivnachAlarm"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Immer"))
    elif BereichID == 41:
        if iTxtValue == 0:
            SirenenVerzögerung = iTxtValue
            Text = str(SirenenVerzögerung)
            data["SirenenVerzögerung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - Keine Verzögerung "))
        elif iTxtValue == 1:
            SirenenVerzögerung = iTxtValue
            Text = str(SirenenVerzögerung)
            data["SirenenVerzögerung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 1,5 Min Verzögerung"))
        elif iTxtValue == 2:
            SirenenVerzögerung = iTxtValue
            Text = str(SirenenVerzögerung)
            data["SirenenVerzögerung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 3 Min Verzögerung"))
        elif iTxtValue == 3:
            SirenenVerzögerung = iTxtValue
            Text = str(SirenenVerzögerung)
            data["SirenenVerzögerung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 5 Min Verzögerung "))
        elif iTxtValue == 4:
            SirenenVerzögerung = iTxtValue
            Text = str(SirenenVerzögerung)
            data["SirenenVerzögerung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 10 Min Verzögerung"))
        elif iTxtValue == 5:
            SirenenVerzögerung = iTxtValue
            Text = str(SirenenVerzögerung)
            data["SirenenVerzögerung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 15 Min Verzögerung"))
        elif iTxtValue == 6:
            SirenenVerzögerung = iTxtValue
            Text = str(SirenenVerzögerung)
            data["SirenenVerzögerung"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 20 Min Verzögerung"))
    elif BereichID == 42:
        if iTxtValue == 1:
            Sirenendauer = iTxtValue
            Text = str(Sirenendauer)
            data["Sirenendauer"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 1,5 Min"))
        elif iTxtValue == 2:
            Sirenendauer = iTxtValue
            Text = str(Sirenendauer)
            data["Sirenendauer"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 3 Min "))
        elif iTxtValue == 3:
            Sirenendauer = iTxtValue
            Text = str(Sirenendauer)
            data["Sirenendauer"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 5 Min"))
        elif iTxtValue == 4:
            Sirenendauer = iTxtValue
            Text = str(Sirenendauer)
            data["Sirenendauer"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 10 Min"))
        elif iTxtValue == 5:
            Sirenendauer = iTxtValue
            Text = str(Sirenendauer)
            data["Sirenendauer"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 15 Min"))
        elif iTxtValue == 6:
            Sirenendauer = iTxtValue
            Text = str(Sirenendauer)
            data["Sirenendauer"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 20 Min"))
    elif BereichID == 44:
        if iTxtValue == 1:
            AusgangszeitGesamtbereich = iTxtValue
            Text = str(AusgangszeitGesamtbereich)
            data["AusgangszeitGesamtbereich"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 10 Sek"))
        elif iTxtValue == 2:
            AusgangszeitGesamtbereich = iTxtValue
            Text = str(AusgangszeitGesamtbereich)
            data["AusgangszeitGesamtbereich"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 20 Sek"))
        elif iTxtValue == 3:
            AusgangszeitGesamtbereich = iTxtValue
            Text = str(AusgangszeitGesamtbereich)
            data["AusgangszeitGesamtbereich"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 30 Sek"))
        elif iTxtValue == 4:
            AusgangszeitGesamtbereich = iTxtValue
            Text = str(AusgangszeitGesamtbereich)
            data["AusgangszeitGesamtbereich"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 45 Sek "))
        elif iTxtValue == 5:
            AusgangszeitGesamtbereich = iTxtValue
            Text = str(AusgangszeitGesamtbereich)
            data["AusgangszeitGesamtbereich"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 60 Sek "))
        elif iTxtValue == 6:
            AusgangszeitGesamtbereich = iTxtValue
            Text = str(AusgangszeitGesamtbereich)
            data["AusgangszeitGesamtbereich"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " - 120 Sek"))
    elif BereichID == 45:
        sEinAusgagsverzögerungVolumen = str(iTxtValue)
        if iTxtValue == 0:
            EinAusgagsverzögerungVolumen = iTxtValue
            Text = "Lautstärke = "
            data["EinAusgagsverzögerungVolumen"] = iTxtValue
            AusgabeZwei.config(text=str(Text + sEinAusgagsverzögerungVolumen + " Aus"))
        elif iTxtValue > 0 and iTxtValue <= 9:
            EinAusgagsverzögerungVolumen = iTxtValue
            Text = "Lautstärke = "
            data["EinAusgagsverzögerungVolumen"] = iTxtValue
            AusgabeZwei.config(text=str(Text + sEinAusgagsverzögerungVolumen))
    elif BereichID == 46:
        if iTxtValue == 0:
            Text = str(iTxtValue)
            data["SabotagealarmReaktion"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " Internalarmn"))
        elif iTxtValue == 1:
            Text = str(iTxtValue)
            data["SabotagealarmReaktion"] = iTxtValue
            AusgabeZwei.config(text=str(Text + "Bedienteil"))
        elif iTxtValue == 2:
            Text = str(iTxtValue)
            data["SabotagealarmReaktion"] = iTxtValue
            AusgabeZwei.config(text=str(Text + "Intern + Bedienteil "))
    elif BereichID == 47:
        if iTxtValue == 0:
            Text = str(iTxtValue)
            data["PartionAAlarmReaktion"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " Bedienteilalarm"))
        elif iTxtValue == 1:
            Text = str(iTxtValue)
            data["PartionAAlarmReaktion"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " Bed.-teil + Lautsprecher"))
        elif iTxtValue == 2:
            Text = str(iTxtValue)
            data["PartionAAlarmReaktion"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " Bed.-teil + LS + Wählgerät"))
    elif BereichID == 48:
        if iTxtValue == 0:
            Text = str(iTxtValue)
            data["Bedienteilsperre"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " Aus"))
        elif iTxtValue == 1:
            Text = str(iTxtValue)
            data["Bedienteilsperre"] = iTxtValue
            AusgabeZwei.config(text=str(Text + " AN"))
    elif BereichID == 51:
        if XID == 1:
            BereichID = 7890



    with open(ConfigPath, 'w') as ConfigFile:
        Write = json.dump(data, ConfigFile)
    ConfigFile.close()

    Delete(1)
    BereichID = 7890
    AusgabeEins.config(text=str("Programmiermodus"))
    VarNull(1)

MenüPunkte.cache_clear()
print(EinstellungsPunkte.cache_info())
print(MenüPunkte.cache_info())

#Windows
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

hakenButton = ttk.Button(win, text="√", pady=10, padx=20, font="Serif 15", bg="black", fg="white", command=lambda: ConfirmEntrance("1"))
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
