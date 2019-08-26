from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_open = open(self.path[1:],).read()
            self.send_response(2000)
        except:
            file_open = "Sorry men but don´t found the page"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_open,'utf-8'))

httpd = HTTPServer(('localhost',8080),Serv)
httpd.serve_forever()