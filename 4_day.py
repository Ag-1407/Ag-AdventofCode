#!/usr/bin/python3

import numpy as np
import itertools

def lesen():
    datei = open("4_day.txt", "r")
    daten = [""]
    for line in datei:
        daten += [line.rstrip()]
    daten.pop(0)
    datei.close()
    return daten

def search(data, searchfor):
    return len(list(itertools.chain.from_iterable(np.where(np.array(data.split(":")[0]) == searchfor))))


def proof(dataorig):
    searchfor = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    checked = [False, False, False, False, False, False, False]
    data = dataorig.split()
    if(len(data) < 7):
        return False
    for i in range(len(searchfor)):
        for i2 in range(len(data)):
            if(search(data[i2], searchfor[i])):
                checked[i] = True
                break
        if(checked[i] == False):
            return False
    return True

def main(daten):
    global valid
    rx = 0
    for ix in range(len(daten)):
        i2 = rx
        block = [""]
        for ix in range(10):
            if(i2 >= len(daten)):
                break
            if(daten[i2] == ""):
                break
            else:
                add = " " + daten[i2]
                block += [add.rstrip()]
                i2 += 1
        rx += len(block)

        data = ""
        for i in range(len(block)):
            if(i > 0):
                data += block[i]
        if(proof(data)):
            valid += 1
        if(rx > len(daten)):
            break
valid = 0    
main(lesen())
print("--------------------------------------------------")
print("Ergebnis von Tag 4:")
print(valid, " gültige Pässe!")
print("--------------------------------------------------")