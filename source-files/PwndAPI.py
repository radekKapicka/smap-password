import requests
import hashlib

def findPasswd(password):

    sha_passwd = hashlib.sha1(password.encode()).hexdigest()
    sha_pre = sha_passwd[0:5]
    sha_post = sha_passwd[5:].upper()

    url = "https://api.pwnedpasswords.com/range/" + sha_pre

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    pwnd_dict = {}

    filtered_list = response.text.split("\r\n")
    for pwnd_pass in filtered_list:
        pwnd_hash = pwnd_pass.split(":")
        pwnd_dict[pwnd_hash[0]] = pwnd_hash[1]

    if sha_post in pwnd_dict.keys():
        return pwnd_dict[sha_post]
    else:
        return False