#!/usr/bin/python3

def lesen():
    datei = open("6_day.txt", "r")
    daten = [""]
    for line in datei:
        daten += [line.rstrip()]
    daten.pop(0)
    datei.close()
    return daten

def main(daten):
    global summ
    local = [""]
    for i in range(len(daten)):
        zeile = daten[i]
        if(zeile != ""):
            local += zeile
        else:
            del local[0]
            localonlyonetime = local.copy()
            i2del = 0
            for i in range(len(local)):
                i2 = 0
                if(i >= len(localonlyonetime)):
                    break
                for ix in range(len(local)):
                    if(not i == i2):
                        if(i2 >= len(localonlyonetime)):
                            break
                        if(localonlyonetime[i] == localonlyonetime[i2]):
                            del localonlyonetime[i2]
                            i2 -= 1
                    i2 += 1
            summ += len(localonlyonetime)
            local = [""]




summ = 0
main(lesen())
print("--------------------------------------------------")
print("Ergebnis von Tag 6:")
print("Die gesuchte Zahl ist ", summ)
print("--------------------------------------------------")