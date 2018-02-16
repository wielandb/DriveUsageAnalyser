import os

import sys
import time
def status(s):
    sys.stdout.write(s + " " * (78 - len(s)) + "\r")

allsize = 0 

import os, sys, math, random
def creategui(arglist,clear=False,backbone=False):
    if clear == True:
        for i in range(100):
            print("")
    
    masterlaenge = 0
    for i in range(len(arglist)):
                   roflkopter = "|[" + str(i) + "] - " + arglist[i]
                   rofllaenge = len(roflkopter)
                   if rofllaenge > masterlaenge:
                       masterlaenge = rofllaenge
    print(str(masterlaenge))
    rouven = ""               
    #print("+---------------------+")
    print("+" + "-"*(masterlaenge - 1) + "+")
    for i in range(len(arglist)):
        # Jedem das an lnge geben, was ihm zum lngsten fehlt
        whattoprinta = "|[" + str(i+1) + "] - " + arglist[i]
        howmuchrouven = masterlaenge - len(whattoprinta)
        whattoprintb = whattoprinta + " "*howmuchrouven + "|"
        print(whattoprintb)
    if backbone == True:
        whattoprinta = "|[0] - << Back <<" 
        howmuchrouven = masterlaenge - len(whattoprinta)
        whattoprintb = whattoprinta + " "*howmuchrouven + "|"
        print(whattoprintb)
    print("+" + "-"*(masterlaenge - 1) + "+")

    lool = 99999999
    while lool > len(arglist):
        lool = int(input("[?]>"))
        if lool > len(arglist):
            print("FEHLER: Ungueltie eingabe. Erneut versuchen")
    return lool
    
        


def convert_bytes(num):
    for x in ['b', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def FolderSize(name):
    size = 0
    errors = 0
    global allsize
    for d,r,f in os.walk(name):
        status(str(convert_bytes(allsize)))
        for a in f:
            j = 0
            #print(str(d) + "\\" + str(a))
            try:
                statinfo = os.stat(str(d) + "\\" + str(a))
                size += statinfo.st_size
                allsize += statinfo.st_size
            except WindowsError:
                errors += 1
            finally:
                h = 1
    return size

from glob import glob
grandparent = raw_input("Ordner angeben:")

while True:
    d = glob(grandparent + "\\*\\")
    fsizesbyte = []
    for t in d:
        nsd = FolderSize(t)
        if (nsd < 1020):
           nsd = 0
        fsizesbyte.append(nsd)
    folderview = []
    foldercmplte = 0
    for i in fsizesbyte:
        foldercmplte += i
    print("Groesse des Ordners: " + str(convert_bytes(foldercmplte)))
    print("[0] - Einen Order zurueck")
    for w in range(len(d)):
        prozent = ((fsizesbyte[w]*1.00)/(foldercmplte*1.00))*100
        folderview.append(str(convert_bytes(fsizesbyte[w])) + "       \t" + str(prozent)[:5] + "%       \t" + str(d[w]))
    ttt = creategui(folderview)
    grandparent = str(d[ttt - 1])
    
