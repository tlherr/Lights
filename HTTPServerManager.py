import BaseHTTPServer
from HTTPHandler import HTTPHandler
import time


class HTTPServerManager:

    # Variables
    HTTP_HOST = "0.0.0.0"
    HTTP_PORT = 8000
    server = None

    def __init__(self, coin_machine):
        self.server = BaseHTTPServer.HTTPServer((self.HTTP_HOST, self.HTTP_PORT), HTTPHandler(coin_machine))

    def start_server(self):
        print time.asctime(), ">> HTTP Server Started - %s:%s <<" % (self.HTTP_HOST, self.HTTP_PORT)
        self.server.serve_forever()
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            self.start_server()

    def stop_server(self):
        self.server.server_close()
        print time.asctime(), ">> HTTP Server Stopped - %s:%s <<" % (self.HTTP_HOST, self.HTTP_PORT)
