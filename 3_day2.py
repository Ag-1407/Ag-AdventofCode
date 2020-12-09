#!/usr/bin/python3
import itertools
import numpy as np

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
    global summ
    for i in range(len(pfad)):
        X = pfad[i][0]
        Y = pfad[i][1]
        x = 0
        y = 0
        match = 0

        for y in range(len(daten)):
            zeile = list(daten[y])
            if(x >= len(zeile)):
                x = x - len(zeile)
            if(zeile[x] == '#'):
                match +=1

            x += X
            y += Y
        print(match)
        summ *= match
        


summ = 1
pfad = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
check(lesen())
print("--------------------------------------------------")
print("Ergebnis von Tag 3:")
print("Viele Bäume werden getroffen, Ergebnis: ", summ)
print("--------------------------------------------------")