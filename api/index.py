from http.server import BaseHTTPRequestHandler
from 'src/oai_agent' import main

class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        main()
        self.send_response(200)
        # self.send_header('Content-type','text/plain')
        # self.end_headers()
        # self.wfile.write('Test Application For Chima'.encode('utf-8'))
