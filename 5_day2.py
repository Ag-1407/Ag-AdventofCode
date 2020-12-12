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
    global myplace
    global highscore
    places = [""]
    for i in range(len(daten)):
        id = decode(list(daten[i]))
        if(id > highscore):
            highscore = id
        places += [str(id).replace(".0", "").rstrip()]
    for i in range(int(highscore)):
        for i2 in range(len(daten)):
            found = 0
            a_J = str(places[i2])
            a_b = str(i)
            if(str(places[i2]) == str(i)):
                found = 1
                break
        if(not found):
            myplace = i
        


highscore = 0  
myplace = -1  
main(lesen())
print("--------------------------------------------------")
print("Ergebnis von Tag 5:")
print("Ihre Sitz ID beträgt ", int(myplace))
print("--------------------------------------------------")