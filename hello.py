from http.server import HTTPServer, BaseHTTPRequestHandler

# Define a custom HTTP request handler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send HTTP status code
        self.send_response(200)
        # Send HTTP headers
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Write the HTML content
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple Webpage</title>
        </head>
        <body>
            <h1>Welcome to My Simple Webpage</h1>
            <p>This is a basic HTML page served using Python.</p>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode("utf-8"))

# Set up and start the server
port = 8000  # You can change the port if needed
server_address = ("", port)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print(f"Serving on port {port}...")
httpd.serve_forever()
