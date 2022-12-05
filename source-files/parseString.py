import hashlib
import re
import sys
from PwndAPI import *

scanner = input("Zadej svoje heslo");

findPasswd(scanner)

#res = list(re.findall('(\d+|[@_!#$%^&*()<>?/\|}{~:]|[A-Za-z]+)', scanner));

