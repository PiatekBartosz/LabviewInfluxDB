import http.server
import socketserver
import json

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/write_api":
            content_length = int(self.headers['Content-Length'])  # Get the size of the data
            post_data = self.rfile.read(content_length)  # Read the data
            print("Received POST request:")
            print(f"Path: {self.path}")
            print(f"Headers:\n{self.headers}")
            print(f"Body:\n{post_data.decode('utf-8')}")
            
            # Send a 200 OK response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "success"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            # Handle any other endpoints
            self.send_response(404)
            self.end_headers()

def run(server_class=http.server.HTTPServer, handler_class=MyHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    try:
        run(port=80)  # Change this to 8080 if you don't have permission to use port 80
    except Exception as e:
        print(f"Failed to start server: {e}")
