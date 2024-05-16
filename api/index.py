from http.server import BaseHTTPRequestHandler
from src.oai_agent.oai_agent import main

class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        # This is the function that gets the data from the Open API
        # main()
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Open API quota is over - please try later'.encode('utf-8'))
