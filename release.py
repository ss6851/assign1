import subprocess
import server

def releaseit():
	cmd = "ps aux | grep server.py | head -n 1 |  awk '{print $2}' "
	output = subprocess.check_output(cmd, shell=True)
	print output
	cmd1 = "sudo kill -9 "+ output
	output1 = subprocess.check_output(cmd1, shell=True)
	print output1

releaseit()
#server.server()