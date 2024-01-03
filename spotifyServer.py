import http.server
import socketserver
import json
import random


listas ={
    "Mix_2023": random.uniform(10, 300),
    "Daily_music": random.uniform(100, 300),
    "Liked_songs": random.uniform(20, 300),
    "Daily_mix_1": random.uniform(100, 800),
    "Daily_mix_2": random.uniform(100, 3000),
    "Pa_trapear": random.uniform(10, 300),
}
# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/songs/'):
            lista = self.path[7:]
            print(lista);
            if lista in listas:
                data = {"listas": listas[lista]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("Lista no encontrada.".encode())  # Codificar la cadena a bytes
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090")
    httpd.serve_forever()