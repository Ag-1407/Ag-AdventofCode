#!/usr/bin/python3

def lesen():
    datei = open("3_day.txt", "r")
    daten = [""]
    for line in datei:
        daten += [line.rstrip()]
    daten.pop(0)
    datei.close()
    return daten

def check(daten):
    global match
    x = 0
    y = 0
    for y in range(len(daten)):
        zeile = list(daten[y])
        if(x >= len(zeile)):
            x = x - len(zeile)
        if(zeile[x] == '#'):
            match +=1

        x += 3
        y += 1

match = 0
check(lesen())
print("--------------------------------------------------")
print("Ergebnis von Tag 3:")
print(match, " Bäume werden getroffen!")
print("--------------------------------------------------")