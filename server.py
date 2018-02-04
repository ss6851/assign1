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
		#print data_received
		http_content = (parser.parser(data_received))
		http_method = http_content.split()[0]
		print http_method
		#print data_received.split("\r\n\r")[1]

		#print parser.get_input( print data_received.split("\r\n\r")[1])
		

		if http_method == "GET":
			file_requested = http_content.split()[1].split("/")[1]
			#print file_requested

			try:
				#print file_requested.split("/")[1]
				file = open(file_requested, "r")
				file_contents = file.read()
				file.close
				c.send("HTTP/1.1 200 OK\n"+"Content-Type: text/html\n"+"\n")
				codes.code_200(c, "200 OK")
				c.send(file_contents)

			except:
				codes.code_404(c, "Error 404 Page not found")
				#c.send("HTTP/1.1 404 Not Found\n") 

		elif http_method == "POST":
			#file = data_received.split("/")[1].split()[0]
			#print parser.get_input(data_received.split("\r\n\r")[1])
			#print data_received
			#print data_received.split("\r\n\r\n")[0]
			#print data_received.split("\r\n\r\n")[1]
			#print data_received.split("\r\n\r\n")[]

			user_input = parser.get_input(data_received.split("\r\n\r\n")[1])
			print user_input
			#print data_received.split()[1]		
			
		else: 
			codes.code_404(c, "Error 404 METHOD not found")
			c.close()


server()
