import socket
import parse
import codes
import datetime
import os
import os.path 

#import re 

#subprocess.Popen("releaseport.py")

def server():
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	port = 8080
	s.bind(('', port))
	s.listen(10)

	while True: #To keep hold of the connection
		try:

			c, addr = s.accept()#accept the connection, syn/ack, blocking call
			
			for index in addr:
				h = index # Client (host) IP address
				#print "Client IP address: "+h
				break;

			data_received = c.recv(1024)#makes it multi-threaded, but better used the threading lib
			print data_received+"\n"
			http_content = (parse.parse(data_received))
			#print http_content
			http_method = http_content.split()[0]
			print http_method
			
			file_requested = http_content.split()[1].split("/")[1]

			print file_requested

			if os.path.isfile(file_requested):
				file_size = os.stat(file_requested).st_size
				common_log_1= h + " - " + " - " + str(datetime.datetime.now())+" "+str(http_content)
			else:
				file_size = 0

		
			if http_method == "GET":
				try:
					#flag = 1
					#file_requested = http_content.split()[1].split("/")[1]
					#print file_requested
					
					#print file_requested.split("/")[1]
					file = open(file_requested, "r")
					file_contents = file.read()
					file.close

					access_log = open("access_log.log", "a")
					common_log = common_log_1.strip()+" 200 "+str(file_size)
					access_log.write(common_log+"\n")
					access_log.close()

					c.send("HTTP/1.1 200 OK\n"+"Content-Type: text/html\n"+"\n")
					codes.code_200(c, "200 OK")
					c.send(file_contents)

					#print "FLAG: "+flag					
					#flag = flag+1
				
				except:
					#may have to send 404 for favicon.io request
					codes.code_404(c, "Error 404 File not found")
					#print "check 404"
					c.send("HTTP/1.1 404 Not Found\n")

					access_log = open("access_log.log", "a")
					common_log_1= h + " - " + " - " + str(datetime.datetime.now())+" "+str(http_content)
					common_log = common_log_1.strip()+" 404 "+str(file_size)
					access_log.write(common_log+"\n")
					access_log.close()


			elif http_method == "POST":
				user_input = parse.get_input(data_received.split("\r\n\r\n")[1])#\r\n\r\n is the HTTP version of saying end of line. imp to tell browser end of metadata and start of data.
				print user_input
				access_log = open("access_log.log", "a")
				common_log = common_log_1.strip()+" 200 "+str(file_size)
				access_log.write(common_log+"\n")
				access_log.close()

			else: 
				codes.code_404(c, "Error 404 METHOD not found")
				c.send("HTTP/1.1 404 METHOD Not Found\n")
			

			#flag = flag +1
				
		except:
			s.close()#not closing a connection can lead to a potential denial of service.

server()


