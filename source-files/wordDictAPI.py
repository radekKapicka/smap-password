import requests


def dictWord(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200: return True
    else: return False