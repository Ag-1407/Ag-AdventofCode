#!/usr/bin/python3
import itertools
import numpy as np

def lesen():
    datei = open("2_day.txt", "r")
    daten = [""]
    for line in datei:
        daten += [line.rstrip()]
    daten.pop(0)
    datei.close()
    return daten

def search(bestandteil):
    pass

def check(daten):
    global match
    for i in range(len(daten)):
        array = daten[i].split(" ")
        array[1] = array[1].replace(":", "")
        vorkommen = len(list(itertools.chain.from_iterable(np.where(np.array(list(array[2])) == array[1]))))
        prüfnummer = array[0].split("-")
        if(vorkommen >= int(prüfnummer[0]) and vorkommen <= int(prüfnummer[1])):
            match = match + 1
        i = i + 1
    

match = 0
check(lesen())
print("--------------------------------------------------")
print("Ergebnis von Tag 2:")
print(match, " gültige Passwörter!")
print("--------------------------------------------------")