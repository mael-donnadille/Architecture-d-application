from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class MonServeurWeb(BaseHTTPRequestHandler):
    def do_GET(self):
        file_name_without_slash = self.path.lstrip('/')

        if file_name_without_slash == '':
            file_name_without_slash = 'index.html'

        if os.path.isfile(file_name_without_slash):
            try:
                with open(file_name_without_slash, "rb") as f:
                    contenu = f.read()

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                self.wfile.write(contenu)
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                self.wfile.write(f"<html><body><h1>Erreur interne : {str(e)}</h1></body></html>".encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(f"<html><body><h1>Erreur 404 - Page {file_name_without_slash} non trouvée</h1></body></html>".encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MonServeurWeb)
    print("Serveur en cours d'exécution sur le port 8000...")
    httpd.serve_forever()
