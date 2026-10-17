import requests

respuesta = requests.get("https://official-joke-api.appspot.com/random_ten")
datos = respuesta.json()
for joke in datos:
    print(joke["setup"])
    print(joke["punchline"])
