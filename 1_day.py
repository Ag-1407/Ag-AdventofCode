#!/usr/bin/python3

def read():
    datei = open("1_day.txt", "r")
    daten = [""]
    for line in datei:
        daten += [line.rstrip()]
    daten.pop(0)
    datei.close()
    return daten

def product(one, two, three):
    return int(one) * int(two) * int(three)

def add(one, two, three):
    return int(one) + int(two) + int(three)

def search(daten):
    while True:
        for i in range(len(daten)):
            for i2 in range(len(daten)):
                for i3 in range(len(daten)):
                    if(add(daten[i], daten[i2], daten[i3]) == 2020):
                        print("--------------------------------------------------")
                        print("Ergebnis von Tag 1:")
                        print(daten[i], ", ", daten[i2], " und ", daten[i3], " ergeben ", product(daten[i], daten[i2], daten[i3]))
                        print("--------------------------------------------------")
                        exit()
                    i3 += 1
                i2 += 1
            i += 1
        print("ERROR: no match")
        exit()

search(read())

                
