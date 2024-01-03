import http.server
import socketserver
import json


paises = {
    "mex": {
        "countryCode": "MEX",
        "countryName": "Mexico",
        "numPostalCodes": 7,
        "minPostalCode": 1010,
        "maxPostalCode": 2020
    },
    "eua": {
        "countryCode": "EUA",
        "countryName": "Estados unidos",
        "numPostalCodes": 79,
        "minPostalCode": 3010,
        "maxPostalCode": 10020
    },
    "col": {
        "countryCode": "COL",
        "countryName": "Colombia",
        "numPostalCodes": 9,
        "minPostalCode": 1010,
        "maxPostalCode": 10020
    }

}
# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/countries/'):
            pais = self.path[11:]
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
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090")
    httpd.serve_forever()