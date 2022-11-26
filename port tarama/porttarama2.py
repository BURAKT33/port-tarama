import socket
import sys 
from pyfiglet import Figlet
from datetime import datetime

F = Figlet(font ='slant')
print(F.renderText('BT TARAYICI'))
host = "localhost"

if len(sys.argv)== 2:
	
	host = socket.gethostbyname(sys.argv[1])

print("tarama başladı.."+"  "+str(datetime.now))

try:
	for port in range(1,65500):
		
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		yanit = s.connect_ex((host,port))
		
		if yanit == 0:
			
			print("port açık {}".format(port))
		
		s.close()
except socket.error as msg:
	
	print("\n(SERVER KAPALI) Mesaj:",msg)
	
except KeyboardInterrupt :
	
	print("\nçıkış yapılıyor")
	sys.exit()
		

	
