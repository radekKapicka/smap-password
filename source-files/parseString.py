import hashlib
import pathlib
import re
import sys
import pyminizip
from PwndAPI import *
from strengthCheck import *
from wordDictAPI import *
from czechWordDictAPI import *
from pwdPattern import *


specCharInPw = False
numInPw = False
smallCharInPw = False
bigCharInPw = False
patternInPw = False
isWholeInDB = False
isInCzechDictRes = False
isInEngDict = False
isPartInDB = False
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
        with open('outputFiles/patternPass.txt', 'a') as pwdFile:
            sys.stdout = pwdFile
            print(scanner)
            sys.stdout = original_stdout
        if numOf is False:
            isWholeInDB = True
            print("✅ heslo jako celek se v DB nenechazi")
        else: print("❌ Počet výskytů tvého hesla jako celku: " + numOf)
        numOfPass = 1
    print(" ")
    if numOfPass == 1:
        res = list(re.findall('(\d+|[@_!#$%^&*()<>?/\|}{~:]|[A-Za-z]+)', scanner));
        for passwd_piece in res:
            if len(passwd_piece) >= 3:
                with open('outputFiles/patternPass.txt', 'a') as pwdFile:
                    sys.stdout = pwdFile
                    print(passwd_piece)
                    sys.stdout = original_stdout
                numOf = findPasswd(passwd_piece)
                if numOf is False: print("✅ Část hesla: " + passwd_piece + " se v DB nenechází")
                else:
                    isPartInDB = True
                    print("❌ Počet výskytů části tvého hesla: " + passwd_piece + " je: " + numOf +
                            "  -> Doporučujeme tuto část hesla změnit/upravit")

                isInDict = dictWord(passwd_piece)
                if isInDict is False: print("✅ Část hesla: " + passwd_piece + " se nenachází v anglickém slovníku")
                else:
                    isInEngDict = True
                    print("❌ Část tvého hesla: " + passwd_piece + " je slovo nacházející se v anglickém slovníku")

                isInCzechDict = czechDictWord(passwd_piece)
                if isInCzechDict is False: print("✅ Část hesla: " + passwd_piece + " se nenachází v českém slovníku")
                else:
                    isInCzechDictRes = True
                    print("❌ Část tvého hesla: " + passwd_piece + " je slovo nacházející se v českém slovníku")
                print(" ")

    print(" ")
    print("-------------------------------------------------------------------------------------")
    print("Analýza hesla na základě slovníku sestaveného z prolomených hesel")
    print("-------------------------------------------------------------------------------------")
    strCheck = passStrength(scanner)
    if strCheck == 0: print('❌ Heslo je velmi slabé')
    if strCheck == 1: print('🟠 Heslo je středně silné')
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

    print(" ")
    print("-------------------------------------------------------------------------------------")
    print("Analýza hesla, zda obsahuje klávesnicové patterny")
    print("-------------------------------------------------------------------------------------")
    isPattern = testPattern()
    for keyPattern in isPattern:
        print(keyPattern)
    totalKeyPatCount = keyPattern[-1].split()[-1]
    print(' ')
    print('Počet nelezených klávesových patternů: ' + totalKeyPatCount)
    print('Více info k patternům výše ⬆')
    print(' ')
    if (totalKeyPatCount == 0): print('✅ Heslo neobsahuje žádné klávesnicové paterny')
    else:
        patternInPw = True
        print('❌ Heslo obsahuje klávesnicové patterny')

pyminizip.compress('outputFiles/userPass.txt', None, 'outputFiles/userPass.zip', scanner, 5)

with open('outputFiles/userPass.txt', 'w') as f:
    sys.stdout = f
    print(' ')
    sys.stdout = original_stdout

with open('outputFiles/patternPass.txt', 'w') as pwdFile:
    sys.stdout = pwdFile
    print(' ')
    sys.stdout = original_stdout

print(" ")
print("-------------------------------------------------------------------------------------")
print("Doporučení pro lepší heslo")
print("-------------------------------------------------------------------------------------")

if specCharInPw is False: print('❗Doporučujeme přidat do hesla speciální znaky jako např. @,#,$,_,...')
if smallCharInPw is False: print('❗Doporučujeme přidat do hesla malá písmena')
if bigCharInPw is False: print('❗Doporučujeme přidat do hesla velká písmena')
if numInPw is False: print('❗Doporučujeme přidat do hesla čísla')
if isWholeInDB is False: print('❗Heslo jako celek se nachází v DB prolomených hesel -> doporučujeme zcela změnit heslo')
if isPartInDB is True: print('❗Část vašeho hesla se nachází v DB prolomených hesel -> více informací viz. sekce výše ⬆')
if isInEngDict is True: print('❗Část vašeho hesla je slovo z anglického slovníku -> více informací viz. sekce výše ⬆')
if isInCzechDict is True: print('❗Část vašeho hesla je slovo z českého slovníku -> více informací viz. sekce výše ⬆')
if patternInPw is True: print('❗Vaše heslo obsahuje klávesnicové patterny -> doporučujeme kláv. patterny nepoužívat')


