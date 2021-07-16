#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer

served = 0

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def send_reply(self, code, mime, contents=None, filename=None):
        if filename is not None:
            assert(contents is None)
            with open(filename, 'rb') as f:
                contents = f.read()
        if mime.startswith('text/'):
            contents = bytes(contents, 'utf8')
        self.send_response(code)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', len(contents))
        self.end_headers()
        self.wfile.write(contents)

    def do_GET(self):
        global served
        served = served + 1
        if self.path == '/':
            self.send_reply(200, 'text/html; charset=UTF-8', """<html>
<head>
  <title>This is my web page</title>
</head>
<body>
  <h1>This is my web page</h1>
  <p>Do you like it?</p>
  <p><a href="/served">How many pages have been served so far?</a></p>
</body>
</html>""")
        elif self.path == '/served':
            self.send_reply(200, 'text/html; charset=UTF-8', f"""<html>
<head>
  <title>{served} pages served so far</title>
</head>
<body>
  <h1>{served} pages served so far</h1>
  <p>And they are getting more and more!</p>
  <p><a href="/">Back to the roots</a></p>
</body>
</html>""")
        elif self.path == '/favicon.ico':
            self.send_reply(200, 'image/png', filename='www/favicon.png')
        else:
            self.send_reply(404, 'text/html; charset=UTF-8', """<html>
<head>
  <title>404 File Not Found</title>
</head>
<body>
  <h1>404 File Not Found</h1>
  <p>The URL that you requested was not found by this server. Sorry!</p>
  <p><a href="/">Go to the main site</a></p>
</body>
</html>""")


if __name__ == '__main__':
    httpd = HTTPServer(('', 8000), MyHTTPRequestHandler)
    httpd.serve_forever()
