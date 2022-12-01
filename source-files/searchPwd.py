import hashlib
import re

def search_pwd(searched_pwd):
    pom_file = open('passwds.txt', 'r')
    for line in pom_file:
        buff = pom_file.readline()
        if(searched_pwd.__eq__(buff)): break
        else: return print(searched_pwd + "   |   " + buff)


