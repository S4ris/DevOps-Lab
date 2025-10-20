from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from your DevOps Lab machine!")

server_address = ('', 8080)
httpd = HTTPServer(server_address, MyHandler)
print("Server running on port 8080...")
httpd.serve_forever()
