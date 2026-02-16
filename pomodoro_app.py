import webview
import os
import sys
import threading
import http.server
import socketserver

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # If not in PyInstaller, use the directory of the script
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def start_server():
    path = resource_path("")
    os.chdir(path)
    handler = http.server.SimpleHTTPRequestHandler
    # Use 0 to let OS pick an available port if 8081 is busy
    with socketserver.TCPServer(("", 0), handler) as httpd:
        port = httpd.server_address[1]
        print(f"Serving at port {port}")
        threading.current_thread().port = port
        httpd.serve_forever()

if __name__ == '__main__':
    # Run server in background
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Wait for port to be assigned (briefly)
    import time
    time.sleep(0.5)
    port = getattr(server_thread, 'port', 8081)

    # Open window
    window = webview.create_window('Pomodoro Matrix - Lupe Edition', f'http://localhost:{port}/pomodoro.html', 
                          width=450, height=650, resizable=False)
    
    webview.start()
