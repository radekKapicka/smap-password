import hashlib
import re
import sys
from PwndAPI import *
from strengthCheck import *

numOfPass = 0
scanner = input("Zadej svoje heslo");

if numOfPass == 0:
    numOf = findPasswd(scanner)
    if numOf is False: print("heslo jako celek se v DB nenechazi")
    else: print("Počet výskytů tvého hesla jako celku: " + numOf)
    numOfPass = 1

if numOfPass == 1:
    res = list(re.findall('(\d+|[@_!#$%^&*()<>?/\|}{~:]|[A-Za-z]+)', scanner));
    for passwd_piece in res:
        numOf = findPasswd(passwd_piece)
        if numOf is False: print("Část hesla: " + passwd_piece + " se v DB nenechází")
        else: print("Počet výskytů části tvého hesla: " + passwd_piece + " je: " + numOf)

strCheck = passStrength(scanner)
if strCheck == 0: print('Heslo je velmi slabé')
if strCheck == 1: print('Heslo je tředně silné')
if strCheck == 2: print('Heslo je silné')
