#!/usr/bin/python3

def lesen():
    datei = open("5_day.txt", "r")
    daten = [""]
    for line in datei:
        daten += [line.rstrip()]
    daten.pop(0)
    datei.close()
    return daten

def decode(zeile):
    row = 0
    column = 0
    low = 0
    high = 127
    for i in range(7):
        if(zeile[i] == 'F'):
            high = (high + 1 - low) / 2 - 1 + low
        elif(zeile[i] == 'B'):
            low = low + (high + 1 - low) / 2
    row = high
    low = 0
    high = 7
    for i in range(7,10):
        if(zeile[i] == 'L'):
            high = (high + 1 - low) / 2 - 1 + low
        elif(zeile[i] == 'R'):
            low = low + (high + 1 - low) / 2
    column = high
    t = row * 8 + column
    return t

            


def main(daten):
    global highscore
    for i in range(len(daten)):
        id = decode(list(daten[i]))
        if(id > highscore):
            highscore = id

highscore = 0    
main(lesen())
print("--------------------------------------------------")
print("Ergebnis von Tag 5:")
print("Die höchste seat ID beträgt ", int(highscore))
print("--------------------------------------------------")