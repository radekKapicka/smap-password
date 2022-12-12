import hashlib
import pathlib
import re
import sys
import pyminizip
from PwndAPI import *
from strengthCheck import *
from wordDictAPI import *


specCharInPw = False
numInPw = False
smallCharInPw = False
bigCharInPw = False
numOfPass = 0
original_stdout = sys.stdout
scanner = input("Zadej svoje heslo");

with open('outputFiles/userPass.txt', 'w') as f:
    #sys.stdout = f
    print("-------------------------------------------------------------------------------------")
    print("Analýza hesla, zda se nenachází celé heslo či jeho část v databázi prolomených hesel")
    print("-------------------------------------------------------------------------------------")
    if numOfPass == 0:
        numOf = findPasswd(scanner)
        if numOf is False: print("✅ heslo jako celek se v DB nenechazi")
        else: print("❌ Počet výskytů tvého hesla jako celku: " + numOf)
        numOfPass = 1
    print(" ")
    if numOfPass == 1:
        res = list(re.findall('(\d+|[@_!#$%^&*()<>?/\|}{~:]|[A-Za-z]+)', scanner));
        for passwd_piece in res:
            if len(passwd_piece) >= 3:
                numOf = findPasswd(passwd_piece)
                if numOf is False: print("✅ Část hesla: " + passwd_piece + " se v DB nenechází")
                else: print("❌ Počet výskytů části tvého hesla: " + passwd_piece + " je: " + numOf +
                            "  -> Doporučujeme tuto část hesla změnit/upravit")

                isInDict = dictWord(passwd_piece)
                if isInDict is False: print("✅ Část hesla: " + passwd_piece + " se nenachází v anglickém slovníku")
                else: print("❌ Část tvého hesla: " + passwd_piece + " je slovo nacházející se v anglickém slovníku")
                print(" ")

    print(" ")
    print("-------------------------------------------------------------------------------------")
    print("Analýza hesla na základě slovníku sestaveného z prolomených hesel")
    print("-------------------------------------------------------------------------------------")
    strCheck = passStrength(scanner)
    if strCheck == 0: print('❌ Heslo je velmi slabé')
    if strCheck == 1: print('🟠 Heslo je tředně silné')
    if strCheck == 2: print('✅ Heslo je silné')

    print(" ")
    print("-------------------------------------------------------------------------------------")
    print("Analýza hesla, zda obsahuje velká/malá písmena, čísla a speciální znaky")
    print("-------------------------------------------------------------------------------------")

    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (regex.search(scanner) == None): print('❌ Heslo neobsahuje speciální znaky')
    else:
        specCharInPw = True
        print('✅ Heslo obsahuje speciální znaky')

    regex = re.compile('[a-z]')
    if (regex.search(scanner) == None): print('❌ Heslo neobsahuje malá písmena')
    else:
        smallCharInPw = True
        print('✅ Heslo obsahuje malá písmena')

    regex = re.compile('[A-Z]')
    if (regex.search(scanner) == None): print('❌ Heslo neobsahuje velká písmena')
    else:
        bigCharInPw = True
        print('✅ Heslo obsahuje velká písmena')

    regex = re.compile('[0-9]')
    if (regex.search(scanner) == None): print('❌ Heslo neobsahuje čísla')
    else:
        numInPw = True
        print('✅ Heslo osahuje čísla')

    sys.stdout = original_stdout

pyminizip.compress('outputFiles/userPass.txt', None, 'outputFiles/userPass.zip', scanner, 5)

with open('outputFiles/userPass.txt', 'w') as f:
    sys.stdout = f
    print(' ')
    sys.stdout = original_stdout