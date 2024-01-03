import requests

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9091'

def obtener_temperatura(lista):
    url = f'{url_base}/pais/{lista}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        return f'Datos de  {lista}: {data["countries"]}'
    elif response.status_code == 404:
        return f'Lista no encontrada: {lista}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

paises = ["mex", "col", "eua"]
for pais in paises:
    resultado = obtener_temperatura(pais)
    print(resultado)
    
# import requests

# # URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
# url_base = 'http://localhost:9090'

# def obtener_temperatura(lista):
#     url = f'{url_base}/songs/{lista}'
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()

#         return f'Datos de lista {lista}: {data["listas"]} escuchantes'
#     elif response.status_code == 404:
#         return f'Lista no encontrada: {lista}'
#     else:
#         return f'Error en la solicitud: Código {response.status_code}'

# listas = ["Mix_2023",
# "Daily_music",
# "Liked_songs",
# "Daily_mix_1",
# "Daily_mix_2",
# "Pa_trapear",]
# for lista in listas:
#     resultado = obtener_temperatura(lista)
#     print(resultado)
    
    
# import requests

# # URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
# url_base = 'http://localhost:9090'

# def obtener_temperatura(pais):
#     url = f'{url_base}/countries/{pais}'
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()

#         return f'Datos de {pais}: {data["countries"]}°C'
#     elif response.status_code == 404:
#         return f'País no encontrado: {pais}'
#     else:
#         return f'Error en la solicitud: Código {response.status_code}'

# # Ejemplos de uso

# # paises = ["Argentina", "Brazil", "Chile", "Colombia", "Mexico"]
# paises = ["mex", "col", "eua"]
# for pais in paises:
#     resultado = obtener_temperatura(pais)
#     print(resultado)