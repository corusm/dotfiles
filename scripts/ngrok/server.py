#!/usr/bin/env python3
import http.server, os, subprocess

class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        path = 'test.sh'

        # Make path absolute
        if path[0] != '/':
            path = os.getcwd() + '/' + path

        # If file exists, execute it and return output
        if os.path.isfile(path):
            if os.access(path, os.X_OK):
                p = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = p.communicate()
                content = stdout.decode('UTF-8')
            else:
                content = path + ' is not executable'

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode('UTF-8'))

        else:
            self.send_header('Content-type', 'text/html')
            self.send_response(404, 'File Not Found')
            self.end_headers()

PORT = 8000
handler_class = HTTPRequestHandler
httpd = http.server.HTTPServer(('', PORT), handler_class)

print('Listening at port', PORT)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print('Server stopped')
