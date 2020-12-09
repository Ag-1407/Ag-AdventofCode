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
        einzeln = list(array[2])
        prüfnummer = array[0].split("-")
        if(array[1] == einzeln[int(prüfnummer[0])-1] and array[1] != einzeln[int(prüfnummer[1])-1]):
            match = match + 1
        elif(array[1] != einzeln[int(prüfnummer[0])-1] and array[1] == einzeln[int(prüfnummer[1])-1]):
            match = match + 1
        i = i + 1
    

match = 0
check(lesen())
print("--------------------------------------------------")
print("Ergebnis von Tag 2:")
print(match, " gültige Passwörter!")
print("--------------------------------------------------")