from app import app
from wsgiref.simple_server import make_server

HOST = "localhost"
PORT = 80

with make_server(HOST, PORT, app) as httpd_server:
    print(f"Started server at {HOST}, {PORT}")
    httpd_server.serve_forever()
