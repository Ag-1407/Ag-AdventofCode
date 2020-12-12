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

def proofvalue(data, searchfor):
    if(len(list(itertools.chain.from_iterable(np.where(np.array(data.split(":")[0]) == searchfor)))) == False):
        return False

    value = data.split(":")[1]
    listvalue = list(value)
    length = len(listvalue)
    if(searchfor == "byr"):
        if(length != 4):
            return False
        if(int(value) < 1920 or int(value) > 2002):
            return False
    if(searchfor == "iyr"):
        if(length != 4):
            return False
        if(int(value) < 2010 or int(value) > 2020):
            return False
    if(searchfor == "eyr"):
        if(length != 4):
            return False
        if(int(value) < 2020 or int(value) > 2030):
            return False
    if(searchfor == "hgt"):
        if(length == 4):#inch
            if(listvalue[2] == 'i' and listvalue[3] == 'n'):
                integer = int(listvalue[0])*10 + int(listvalue[1])
                if(integer < 59 or integer > 76):
                    return False
            else:
                return False
        elif(length == 5):#cm
            if(listvalue[3] == 'c' and listvalue[4] == 'm'):
                integer = int(listvalue[0])*100 + int(listvalue[1])*10 + int(listvalue[2])
                if(integer < 150 or integer > 193):
                    return False
            else:
                return False
        else:
            return False
    if(searchfor == "hcl"):
        if(length != 7):
            return False
        if(listvalue[0] != '#'):
            return False
        for i in range(length):
            if(i):
                if(listvalue[i] == '0' or listvalue[i] == '1' or listvalue[i] == '2' or listvalue[i] == '3' or listvalue[i] == '4' or listvalue[i] == '5' or listvalue[i] == '6' or listvalue[i] == '7' or listvalue[i] == '8' or listvalue[i] == '9' or listvalue[i] == '0' or listvalue[i] == 'a' or listvalue[i] == 'b' or listvalue[i] == 'c' or listvalue[i] == 'd' or listvalue[i] == 'e' or listvalue[i] == 'f'):
                    pass
                else:
                    return False
    if(searchfor == "ecl"):
        if(value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth"):
            pass
        else:
            return False
    if(searchfor == "pid"):
        #if(listvalue[0] != '0'):
        #    return False
        if(length != 9):
            return False
    
    return True

    


def proofpass(dataorig):
    global valid
    searchfor = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    checked = [False, False, False, False, False, False, False]
    data = dataorig.split()
    if(len(data) < 7):
        return False
    for i in range(len(searchfor)):
        for i2 in range(len(data)):
            if(proofvalue(data[i2], searchfor[i])):
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
        if(proofpass(data)):
            valid += 1
        if(rx > len(daten)):
            break
valid = 0    
main(lesen())
print("--------------------------------------------------")
print("Ergebnis von Tag 4:")
print(valid, " gültige Pässe!")
print("--------------------------------------------------")