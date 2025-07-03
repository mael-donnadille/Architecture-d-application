from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class MonServeurWeb(BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path
        parsed_url = urlparse(self.path)
        target = parsed_url.path.lstrip('/') 

        query_params = parse_qs(parsed_url.query)
        nom = query_params.get("nom", ["inconnu"])[0]
        prenom = query_params.get("prenom", ["inconnu"])[0]

        if target == "index.html" or target == "":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            html = f"""
            <!DOCTYPE html>
            <html>
            <head><title>Serveur Web Python</title></head>
            <body>
                <h2>Vous avez sollicite la page : {target}</h2>
                <p>Nom : {nom}</p>
                <p>Prenom : {prenom}</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        else:
            # erreur 404
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            html = f"""
            <!DOCTYPE html>
            <html>
            <head><title>Erreur 404</title></head>
            <body>
                <h2>Erreur 404 - Page {target} non trouvee</h2>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

if __name__ == '__main__':
    server_address = ('', 8000)  # Serveur localhost:8000
    httpd = HTTPServer(server_address, MonServeurWeb)
    print("Serveur en cours d'exécution sur le port 8000...")
    httpd.serve_forever()
