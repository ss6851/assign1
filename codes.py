
def code_404(s, text):
	msg = "HTTP/1.1 404 Not Found\nConnection: close\nContent-Type: text/html\n\n<html><h1>"+text+"</h1></html>\n"
	s.send(msg)

def code_200(s, text):
	msg = "HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\n<html><h1>"+text+"</h1></html>\n"
	s.send(msg)
