import socket
import sys
import threading

host = '127.0.0.1'
port = 9100

sockets = {}


class Connect(threading.Thread):
  def __init__(self, sock, addr):
    self.sock = sock
    self.addr = addr
    threading.Thread.__init__(self)
  def run (self):
    wait = True
    while wait:
      buf = self.sock.recv(1024)

      if (len(sockets) == 2 and buf == "1"):
        self.sock.send(buf)

      if (buf == "2"):
        print("recieve2")
        for addr, sock in sockets.iteritems():
          if (addr != self.addr and sock != self.sock):
            sockets[addr].send(buf)
            print("send2")               

      if (len(buf) >  1):
        print("receive word")
        for addr, sock in sockets.iteritems():
          if (addr != self.addr and sock != self.sock):
            sockets[addr].send(buf)
            print("send word")
      if (buf == "4"):
        print("The End")
        wait = False
  

    self.sock.close()
        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(2)


while True:
  sock, addr = s.accept()
  sockets[addr] = sock
  Connect(sock, addr).start()

