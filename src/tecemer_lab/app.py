import requests

try:
    respuesta = requests.get(
        "https://official-joke-api.appspot.com/random_ten", timeout=5
    )
    respuesta.raise_for_status()
    datos = respuesta.json()
    for jokes in datos:
        print(f"{jokes['setup']} - {jokes['punchline']}")
except requests.RequestException as error:
    print(f"No se pudo obtener el chiste: {error}")
