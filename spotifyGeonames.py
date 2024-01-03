import http.server
import socketserver
import json


paises = {
    "mex": {
        "countryCode": "MEX",
        "countryName": "Mexico",
        "numPostalCodes": 7,
        "minPostalCode": 1010,
        "maxPostalCode": 2020,
        "lists": [
            "daily mix",
            "daily mix 2",
            "liked songs",
            "luismiguel"
        ]
    },
    "eua": {
        "countryCode": "EUA",
        "countryName": "Estados unidos",
        "numPostalCodes": 79,
        "minPostalCode": 3010,
        "maxPostalCode": 10020,
        "lists": [
            "daily mix",
            "daily mix 2",
            "liked songs",
            "juan gabriel"
        ]
    },
    "col": {
        "countryCode": "COL",
        "countryName": "Colombia",
        "numPostalCodes": 9,
        "minPostalCode": 1010,
        "maxPostalCode": 10020,
        "lists": [
            "daily mix",
            "daily mix 2",
            "perreke",
            "luismiguel"
        ]
    }

}
# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/pais/'):
            pais = self.path[6:]
            print(pais)
            if pais in paises:
                data = {"countries": paises[pais]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())  # Codificar la cadena a bytes
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9091), MyHandler) as httpd:
    print("Servidor web en el puerto 9090")
    httpd.serve_forever()