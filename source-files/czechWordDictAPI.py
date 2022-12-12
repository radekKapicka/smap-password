import requests

def czechDictWord(word):
    url = "https://lexicala1.p.rapidapi.com/search?source=global&language=cs&text=" + word

    headers = {
        "X-RapidAPI-Key": "ef22f1e4efmshead036ce1da48f4p1102aejsn0be0e1efde8f",
        "X-RapidAPI-Host": "lexicala1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    response = response.text.split(',')
    response = response[0].split(':')
    response = response[1].split(" ")
    if response[1] == '0': return False
    else: return True