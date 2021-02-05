#!/usr/bin/python3

def lesen():
    datei = open("6_day.txt", "r")
    daten = [""]
    for line in datei:
        daten += [line.rstrip()]
    datei.close()
    daten.append("")
    return daten

# gibt die Anzahl der Vorkommnisse von searchin in searchfor zurück


def search(searchfor, searchin):
    try:
        toreturn = searchin.index(searchfor)+1
    except ValueError:
        toreturn = 0
    return toreturn


def splitintogroups(daten):
    local = [""]
    gruppen = [""]
    i2 = 0
    for i in range(len(daten)):
        if(daten[i] != ""):
            local.append(daten[i])
            local.append("|")  # Zeilenumbruchsymbol
        else:
            del local[0]
            # local.append("#")
            localstr = ""
            for i in range(len(local)):
                localstr += local[i]
            gruppen.append(localstr)
            local = [""]
    del gruppen[0]
    del gruppen[0]
    return gruppen


def main(daten):
    global summ
    gruppen = splitintogroups(daten)
    for i in range(len(gruppen)):
        gruppe = gruppen[i].split("|")
        del gruppe[-1]
        erstes = gruppe[0]
        found = True
        for i2 in range(len(erstes)):
            for i3 in range(len(gruppe)):
                if(not search(erstes[i2], gruppe[i3])):
                    found = False
            if(found):
                summ += 1
            else:
                found = True


summ = 0
main(lesen())
print("--------------------------------------------------")
print("Ergebnis von Tag 6 Teil 2:")
print("Die gesuchte Zahl ist ", summ)
print("--------------------------------------------------")
