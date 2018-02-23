import socket
import parse
import codes
import datetime
import os
import os.path 
import subprocess
#import configFile as cfg
#import configLangFile as cflg

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
				print "Client IP address: "+h
				break;

			data_received = c.recv(1024)#makes it multi-threaded, but better used the threading lib
			print "data_received:" +data_received
			http_content = (parse.parse(data_received))
			print "http_content: "+http_content
			http_method = http_content.split()[0]
			print "HTTP METHOD: "+http_method

			http_version = http_content.split()[2].split("/")[1]	
			print "http_version: "+http_version		

			common_log_1= h + " - " + " - " + str(datetime.datetime.now())+" "+str(http_content)
			error_common_log_1 = str(datetime.datetime.now()) + " [error] " + h

			var = 100
			
			
			if http_version in ['0.9', '1.0', '1.1', '2.0']:
				#print "check 1"				

				if http_method=="CONNECT":
					print "Executing CONNECT..."
					#file_size = ""
			
				else:
					#print "http_version: "+http_version
					file_requested = http_content.split()[1].split("/")[1]#[1]
					print "file_requested: "+file_requested
					if os.path.isfile(file_requested):
						file_size = os.stat(file_requested).st_size
						print file_size
						perm = os.access(file_requested, os.R_OK)
						perm = str(perm)
						print "perm: "+perm
						var = 0
						var = os.system("php-cgi "+file_requested)
						#print "var "+var

					else:
						file_size = 0


				if not var == 65280:#equivalent to: php-cgi did not crash, wasn't 403 either
					if var == 0:#php-cgi worked!
						if http_method == "GET":
							try:
								file = open(file_requested, "r")
								file_contents = file.read()
								file.close

								if(str(file_requested) == "401.txt"):
									print "****"
									auth = data_received.split("\n")[3].split(":")[0]
									#print auth
									#if data_received.split("\n")[3].split()[2].contains("="):
									#	creds = data_received.split("\n")[3].split()[2]
									#print "creds: "+creds
									if auth =="Authorization":
										creds = data_received.split("\n")[3].split()[2]

										if creds == "c2luZ2g6c2luZ2g=":
											c.send("HTTP/1.1 200 OK\n"+"Content-Type: text/html\n"+"\n")
											codes.code_200(c, "200 OK")
											c.send(file_contents)											

										else:
											codes.code_401(c, "401 Unauthorized")
											c.send("HTTP/1.1 401 Unauthorized\n")
											access_log = open("access_log.log", "a")
											#common_log_1= h + " - " + " - " + str(datetime.datetime.now())+" "+str(http_content)
											common_log = common_log_1.strip()+" 401 "+str(file_size)
											access_log.write(common_log+"\n")
											access_log.close()
									else:
										codes.code_401(c, "401 Unauthorized")
										c.send("HTTP/1.1 401 Unauthorized\n")
										access_log = open("access_log.log", "a")
										#common_log_1= h + " - " + " - " + str(datetime.datetime.now())+" "+str(http_content)
										common_log = common_log_1.strip()+" 401 "+str(file_size)
										access_log.write(common_log+"\n")
										access_log.close()

								else:
									c.send("HTTP/1.1 200 OK\n"+"Content-Type: text/html\n"+"\n")
									codes.code_200(c, "200 OK")
									c.send(file_contents)

									access_log = open("access_log.log", "a")
									common_log = common_log_1.strip()+" 200 "+str(file_size)
									access_log.write(common_log+"\n")
									access_log.close()

								
							except:
								codes.code_404(c, "Error 404 File not found")
								c.send("HTTP/1.1 404 Not Found\n")
								access_log = open("access_log.log", "a")
								#common_log_1= h + " - " + " - " + str(datetime.datetime.now())+" "+str(http_content)
								common_log = common_log_1.strip()+" 404 "+str(file_size)
								access_log.write(common_log+"\n")
								access_log.close()

						elif http_method == "POST":
							#print http_method
							print "\n...............................................................\n"
							con_len =  data_received.split("\n")[3].split(":")[0]
							#print "len:"+data_received.split("\r\n")[0]
							#for i in range(0,20):#len(data_received.split("\r\n")):
								#print data_received.split("\r\n")[i]
							#print con_len
							#'''
							if con_len =="Content-Length":
								_POST = parse.get_input(data_received.split("\r\n\r\n")[1])#\r\n\r\n is the HTTP version of saying end of line. imp to tell browser end of metadata and start of data.
								#print _POST
								#for i in _POST:
								#	print _POST.values(i)
								
								post_contents = open("post_input.txt","w")
								post_contents.write("p\n")
								post_contents.close()
								post_contents = open("post_input.txt","a")

								for v,k in _POST.items():
									#print 
									#post_contents = open("post_input.txt","w")
									post_contents.write(v+": "+k+"\n")
								post_contents.close()

								#c.send(_POST)
								#for i in len(user_input):
								#	c.send(user_input[i])
								access_log = open("access_log.log", "a")
								common_log = common_log_1.strip()+" 200 "+str(file_size)
								access_log.write(common_log+"\n")
								access_log.close()
							else:
								c.send("HTTP/1.1 411 Length required\n" + "Content-Type: text/html\n" + "\n")
								codes.code_411(c, "411 Length required")
								error_log = open("error_log.log", "a")
								#print "before flag"
								error_common_log = error_common_log_1.strip()+" 411 " 
								#print "flag"
								error_log.write(error_common_log+ "\n")
								error_log.close()
								#'''

						elif http_method == "PUT":
							cmd = "touch "+file_requested 
							output = subprocess.check_output(cmd, shell=True)
							c.send("HTTP/1.1 200 OK\n" + "Content-Type: text/html\n" + "\n")
							codes.code_200(c, "200 OK")
							access_log = open("access_log.log", "a")
							common_log = common_log_1.strip()+" 200 "+str(file_size)
							access_log.write(common_log+"\n")
							access_log.close()

							access_log = open("access_log.log", "a")
							common_log = common_log_1.strip() + " 200 " + str(flie_size)
							access.log.write(common_log + "\n")
							access_log.close()

						elif http_method == "DELETE":
							c.send("HTTP/1.1 200 OK\n" + "Content-Type: text/html\n" + "\n")
							codes.code_200(c, "200 OK")
							os.remove(file_requested)
							access_log = open("access_log.log", "a")
							common_log = common_log_1.strip() + " 200 " + str(file_size)
							access_log.write(common_log + "\n")
							access_log.close()

						elif http_method == "CONNECT":	
							file_requested = data_received.split()[1]
							print "file_requested: "+file_requested
							host = file_requested.split(":")[0]
							#print host 
							p = int(file_requested.split(":")[1])
							#print p
							request = "GET / HTTP/1.1"
							s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
							#print "check 2"
							s.connect((host, p))
							s.send(request)
							result = s.recv(2048)
							print "check 3"

							while (len(result) > 0):
								print result
								result = s.recv(2048)
							#s.close()
							s.close()
							access_log = open("access_log.log", "a")
							common_log = common_log_1.strip() + " 200 " #+ len(result)
							access_log.write(common_log + "\n")
							access_log.close()

						else:
							#print "start of else: "
							c.send("HTTP/1.1 400 Bad Request\n" + "Content-Type: text/html\n" + "\n")
							codes.code_400(c, "400 Bad Request")
							error_log = open("error_log.log", "a")
							#print "before flag"
							error_common_log = error_common_log_1.strip()+" 400 " 
							#print "flag"
							error_log.write(error_common_log+ "\n")
							error_log.close()	
					else:
						c.send("HTTP/1.1 500 Server Error\n" + "Content-Type: text/html\n" + "\n")
						codes.code_500(c, "500 Server Error")
						error_log = open("error_log.log", "a")
						#print "before flag"
						error_common_log = error_common_log_1.strip()+" 500 " 
						#print "flag"
						error_log.write(error_common_log+ "\n")
						error_log.close()
				else:
					if perm == "True":
						print "Could also mean that the file_requested did not exist"
						c.send("HTTP/1.1 500 Server Error\n" + "Content-Type: text/html\n" + "\n")
						codes.code_500(c, "500 Server Error")
						error_log = open("error_log.log", "a")
						#print "before flag"
						error_common_log = error_common_log_1.strip()+" 500 " 
						#print "flag"
						error_log.write(error_common_log+ "\n")
						error_log.close()
						
					else:
						c.send("HTTP/1.1 403 Forbidden\n" + "Content-Type: text/html\n" + "\n")
						codes.code_403(c, "403 Forbidden")
						error_log = open("error_log.log", "a")
						#print "before flag"
						error_common_log = error_common_log_1.strip()+" 403 " 
						#print "flag"
						error_log.write(error_common_log+ "\n")
						error_log.close()					
			else:
				c.send("HTTP/1.1 505 HTTP Version Not Supported\n" + "Content-Type: text/html\n" + "\n")
				codes.code_400(c, "505 HTTP Version Not Supported")
				error_log = open("error_log.log", "a")
				error_common_log = error_common_log_1.strip()+" 505 " #+ str(file_size)
				error_log.write(error_common_log+ "\n")
				error_log.close()
		except:
			s.close()#not closing a connection can lead to a potential denial of service.
server()