For WEB SERVER:
	
	The web server uses following scripts/files for execution:
		server.py – acts as our main server which will respond to every request.
		parse.py – parses the request and returns HTTP method and file requested. It is also used to execute HTTP POST correctly.
		codes.py – responds with the appropriate HTTP code. 
		index.html - used with GET request to demonstrate GET's functionality.
		postit.html - used to demonstrate POST method.
		configFile.py - acts as a configuration file for the web server.
		access_log.log - used to save access logs, in `Common Log Format`, similar to Apache.
		
	
	(All the following commands/scripts/files should be present and executed in the same directory.)
	(The scripts were written in Python 2.x)
	(By default, the web server is working on port 8080, which can be modified in the configFile.py)
	
	To test GET: 
		Run `python server.py` on one terminal and open browser to type: `localhost:8080/index.html`
	
	To test POST:
		Run `python server.py` on terminal and open browser to type: `localhost:8080/postit.html`.This should open an HTML form in the browser. 
		After filling the form and hitting the `submit` button, you should see the data filled on the form in the terminal.
	
	To test PUT:
		Run `python server.py` on one terminal and `nc localhost 8080` in a second terminal. In the second terminal, type the following command:
		`PUT /new_file HTTP/1.1`. After the successful execution, you will see `new_file` in the current directory.
	
	To test DELETE: 
		Run `python server.py` on one terminal and `nc localhost 8080` in a second terminal. In the second terminal, type the following command:
		`DELETE /file_name HTTP/1.1`. This will delete `file_name`.
		
	To test CONNECT:
		Run `python server.py` in a terminal and `nc localhost 8080` in a second terminal. In the second terminal, type the following command:
		`CONNECT www.web_page:port_number HTTP/1.1`. In the first terminal, you will see the HTML code for the `web_page` requested.
	
	
	To make sure server side scripting works (assuming you don't already have php installed): 
	
	On MAC: 
		brew tap homebrew/dupes brew tap homebrew/versions
		brew tap homebrew/homebrew-php
		brew install php54
	
	On Linux (Debain base):
		sudo apt-get install php libapache2-mod-php php-mcrypt php-mysql
		sudo apt install php-cgi

For the Web App:
	After starting the web server, please navigate to a browser of your choice and type "localhost:8080/site.html" to access our main web page. Note: if you are using Chrome, you may have to remove "?" from the path as this is a bug within Chrome that appears when you navigate with html tags.
	
	From site.html, you can choose to register, login, or search. If you login, you will have the option to update your information in our database. At any point, you can also choose to logout after you successfully login.

