import socket
import parse
import codes
import datetime
import os
import os.path 
import subprocess
import configFile as cfg
import configLangFile as cflg
#import trycon

def server():
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	port = cfg.serSetup['PORT']
	s.bind(('', port))
	s.listen(10)


	while True: #To keep hold of the connection
		try:

			#print "before EVERything"
			c, addr = s.accept()#accept the connection, syn/ack, blocking call
			
			for index in addr:
				h = index # Client (host) IP address
				print "Client IP address: "+h
				break;

			data_received = c.recv(1024)#makes it multi-threaded, but better used the threading lib
			http_content = (parse.parse(data_received))
			http_method = http_content.split()[0]
			print "HTTP METHOD: ", http_method
			
			if not http_method=="CONNECT":
				file_requested = http_content.split()[1].split("/")[1]

				os.system("php-cgi " + file_requested)

				if os.path.isfile(file_requested):
					file_size = os.stat(file_requested).st_size
					common_log_1= h + " - " + " - " + str(datetime.datetime.now())+" "+str(http_content)
				
				else:
					file_size = 0
			else:
				if http_method == "GET":
					try:
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

					except:
						codes.code_404(c, "Error 404 File not found")
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

				elif http_method == "PUT":
					cmd = "touch "+file_requested 
					output = subprocess.check_output(cmd, shell=True)
					print output

					file_requested.close()

					access_log = open("access_log.log", "a")
					common_log = common_log_1.strip() + " 200 " + str(flie_size)
					access.log.write(common_log + "\n")
					access_log.close()

				elif http_method == "CONNECT":	
					file_requested = data_received.split()[1]
					host = file_requested.split(":")[0]
					p = int(file_requested.split(":")[1])
					request = "GET / HTTP/1.1"
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.connect((host, p))
					s.send(request)
					result = s.recv(2048)
					while (len(result) > 0):
						print result
						result = s.recv(2048)
					s.close()


				elif http_method == "DELETE":
					c.send("HTTP/1.1 200 OK\n" + "Content-Type: text/html\n" + "\n")
					codes.code_200(c, "200 OK")
					os.remove(file_requested)
					access_log = open("access_log.log", "a")
					common_log = common_log_1.strip() + " 200 " + str(file_size)
					access_log.write(common_log + "\n")
					access_log.close()	

				else: 
					codes.code_404(c, "Error 404 METHOD not found")
					c.send("HTTP/1.1 404 METHOD Not Found\n")

		except:
			s.close()#not closing a connection can lead to a potential denial of service.

server()
