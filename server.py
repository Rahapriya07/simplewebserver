from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<html>
<head> <title>my first page</title>
</head>
<Body>
<table border="1" align="center" bgcolor="cyan" cellpadding="10">
    <caption>LIST OF PROTOCOLS IN TCP/IP PROTOCOL SUITE.</captio>
    <tr><th>S.No</th><th>Name of the layer</th><th>Name of the protocol</th></tr>
    <tr><td>1</td><td>Application Layer</td><td>HTTP,FTP,DNS,Telnet & SSH</td></tr>
    <tr><td>2</td><td>Transport Layer</td><td>TCP/UDP</td></tr>
    <tr><td>3</td><td>Network Layer</td><td>IPV4/IPV6</td></tr>
    <tr><td>4</td><td>Link Layer</td><td>Ethernet</td></tr>

</table>
</Body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()