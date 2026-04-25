#!/usr/bin/python3
"""
A simple HTTP server using the http.server module.
Handles different endpoints and returns text or JSON data.
"""
import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Custom request handler for our simple API."""

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        
        if self.path == '/':
            # Basic Hello response
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # Serving JSON data
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            # Status check endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # Info endpoint
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # Error handling for undefined endpoints
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

# Define the port
PORT = 8000

if __name__ == "__main__":
    # Initialize the server
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Server started at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            httpd.server_close()
