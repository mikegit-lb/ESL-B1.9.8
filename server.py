import http.server
import socketserver
import os
import json

PORT = int(os.environ.get("PORT", 8080))
PUBLIC_DIR = os.path.dirname(os.path.abspath(__file__))

class ESLHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

    def do_GET(self):
        if self.path == "/api/curriculum":
            with open(os.path.join(PUBLIC_DIR, "curriculum_data.json"), "r", encoding="utf-8") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(data.encode("utf-8"))
            return
        elif self.path == "/api/verbs":
            with open(os.path.join(PUBLIC_DIR, "curriculum_data.json"), "r", encoding="utf-8") as f:
                parsed = json.load(f)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(parsed["verbs"], indent=2, ensure_ascii=False).encode("utf-8"))
            return
        
        # Default static file handler
        return super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), ESLHandler) as httpd:
        print(f"====================================================")
        print(f"ESL Past Perfect Python Web Service running on port {PORT}")
        print(f"Open: http://localhost:{PORT}")
        print(f"====================================================")
        httpd.serve_forever()
