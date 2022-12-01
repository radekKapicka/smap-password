import hashlib
import re
import sys
from searchPwd import *

print("Zadej svoje heslo");
scanner = sys.stdin.readline();
print(scanner);
pom = 0;

search_pwd(scanner)

res = list(re.findall('(\d+|[@_!#$%^&*()<>?/\|}{~:]|[A-Za-z]+)', scanner));


for x in res:
    search_pwd(scanner[pom])
    pom += 1
