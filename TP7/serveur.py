from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import xml.etree.ElementTree as ET
import os

tree = ET.parse('personnel.xml')
root = tree.getroot()

annuaire = {
    ('CAMMAS', 'Rachel'): '0601020304',
    ('PITIOT', 'Paul'): '0602030405',
    ('RIGAILL', 'Pierre'): '0603040506',
    ('ROUSSILLE', 'Philippe'): '0604050607',
    ('CASTELLA', 'Fabien'): '0605060708',
    ('FABIE', 'Sophie'): '0606070809'
}

class ServeurXML(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if parsed_url.path == '/' and 'nom' in query_params and 'prenom' in query_params:
            nom = query_params.get('nom', [''])[0].upper()
            prenom = query_params.get('prenom', [''])[0].capitalize()

            phone = annuaire.get((nom, prenom), None)

            if phone:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"<html><body><h2>Numero de {prenom} {nom} : {phone}</h2></body></html>".encode())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"<html><body><h2>Erreur : numero introuvable pour {prenom} {nom}.</h2></body></html>".encode())
        elif parsed_url.path == '/':
            try:
                with open('formulaire.html', 'rb') as f:
                    contenu = f.read()

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(contenu)
            except:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Erreur lors de l'ouverture du formulaire.")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Page non trouvee.")

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, ServeurXML)
    print("Serveur en cours sur le port 8000...")
    httpd.serve_forever()
