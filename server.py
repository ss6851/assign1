import socket
import parser
import codes

#subprocess.Popen("releaseport.py")

def server():
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	port = 8080
	s.bind(('', port))
	s.listen(1)

	while True: #To keep hold of the connection
		c, addr = s.accept()
		data_received = c.recv(1024)
		print data_received
		http_method = (parser.parser(data_received)).split()[0]
		#print http_method

		if http_method == "GET":
			file_requested = (parser.parser(data_received)).split()[1]
			#print file_requested

			try:
				#print file_requested.split("/")[1]
				file = open(file_requested.split("/")[1], "r")
				file_contents = file.read()
				file.close
				c.send("HTTP/1.1 200 OK\n"+"Content-Type: text/html\n"+"\n")
				codes.code_200(c, "200 OK")
				

			except:
				codes.code_404(c, "Error 404 page not found")
				#c.send("HTTP/1.1 404 Not Found\n") 
		else: 
			print "not working"


server()
