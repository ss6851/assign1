Hi @everyone! I have been trying to simulate GET request and have written few lines of code. Following is the function of each python file.

server.py – acts as our main server which will respond to every request.
parse.py – parses the request and returns HTTP method and file requested (for now)
codes.py – responds with the appropriate HTTP code. 

Python code for other HTTP requests can be added in server.py when we all collaborate. I suggest we divide subactivities of activity 1 so that everybody can get to learn.

I am using this approach because I think it is modular and scalable, but I might be wrong. Please feel free to suggest any changes.


To execute GET: 

run server.py on one terminal and open browser to type: localhost:8080/index.html

To test POST:
run server.py on terminal and open browser to type: localhost:8080/postit.html



----->Handy Command for testing purposes: `sudo kill -9 `ps aux|grep "python server.py"| head -n 1|awk '{print $2}'``

P.S. Please name the commit appropriately to specify changes.

To make sure server side scripting works (assuming you don't already have php installed): 
On MAC: 
brew tap homebrew/dupes
brew tap homebrew/versions
brew tap homebrew/homebrew-php

brew install php54
