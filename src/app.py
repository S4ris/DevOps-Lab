from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            with open('/home/vagrant/app/index.html', 'rb') as file:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Page not found')

    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))

            name = data.get('name', [''])[0]
            email = data.get('email', [''])[0]
            message = data.get('message', [''])[0]

            print(f"Received form submission: {name}, {email}, {message}")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Thank you for your feedback!')
        else:
            self.send_response(404)
            self.end_headers()

server_address = ('', 8080)
httpd = HTTPServer(server_address, MyHandler)
print("Server running on port 8080...")
httpd.serve_forever()
