
def code_404(s, text):
	msg = "HTTP/1.1 404 Not Found\nConnection: close\nContent-Type: text/html\n\n<html><h1>"+text+"</h1></html>\n"
	#Connection close are not required but useful to explicity tell the browser what to do.
	s.send(msg)

def code_200(s, text):
	msg = "HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\n<html><h1>"+text+"</h1></html>\n"
	s.send(msg)
	
def code_400(s, text):
	msg = "HTTP/1.1 400 Bad Request\nConnection: close\nContent-Type: text/html\n\n<html><h1>"+text+"</h1></html>\n"
	s.send(msg)
	
def code_401(s, text):
	msg = "HTTP/1.1 401 Unauthorized\nConnection: close\nContent-Type: text/html\n\n<html><h1>"+text+"</h1></html>\n"
	s.send(msg)
	
def code_403(s, text):
	msg = "HTTP/1.1 403 Forbidden\nConnection: close\nContent-Type: text/html\n\n<html><h1>"+text+"</h1></html>\n"
	s.send(msg)
	
def code_411(s, text):
	msg = "HTTP/1.1 411 Length Required\nConnection: close\nContent-Type: text/html\n\n<html><h1>"+text+"</h1></html>\n"
	s.send(msg)
	
def code_500(s, text):
	msg = "HTTP/1.1 500 Internal Server Error\nConnection: close\nContent-Type: text/html\n\n<html><h1>"+text+"</h1></html>\n"
	s.send(msg)
	
def code_505(s, text):
	"HTTP/1.1 505 HTTP Version Not Supported\nConnection: close\nContent-Type: text/html\n\n<html><h1>"+text+"</h1></html>\n"
	s.send(msg)
