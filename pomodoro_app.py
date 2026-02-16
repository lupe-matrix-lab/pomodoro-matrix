import webview
import os
import threading
import http.server
import socketserver

def start_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 8081), handler) as httpd:
        httpd.serve_forever()

if __name__ == '__main__':
    # Run server in background
    t = threading.Thread(target=start_server, daemon=True)
    t.start()

    # Open window
    webview.create_window('Pomodoro Matrix - Lupe Edition', 'http://localhost:8081/pomodoro.html', 
                          width=450, height=650, resizable=False)
    webview.start()
