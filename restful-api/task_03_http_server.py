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
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # Buradakı mətni testin gözlədiyi formata salırıq
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000

if __name__ == "__main__":
    # Serveri başlatmaq üçün (Allowing address reuse helps with testing)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
