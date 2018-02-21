import socket

def trycon(h,p):

	request = "GET / HTTP/1.1"
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((h,p))
	s.send(request)
	result = s.recv(2048)
	#print result
	while (len(result) > 0):
		print(result)
		result = s.recv(2048)
	s.close()