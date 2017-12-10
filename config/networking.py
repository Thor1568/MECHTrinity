import socket
import threading

#Variable to check who is using printing and keep it from being used twice at once

#In progress networking classes
class Server:
    def __init__(self, timeout, max_users):
        socket.setdefaulttimeout(timeout)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 6573
        self.host_name = socket.gethostname()
        self.ip = socket.gethostbyname(self.host_name)
        self.sock.bind((self.ip, 6573))
        self.sock.listen(max_users)
        self.addresses = []
        self.conns = []

    def work(self):
        #Function that will be run and maintains connections between each Client and is run by thread
        while True:
            try:
                c, addr = self.sock.accept()
                self.addresses.append(addr)
                self.conns.append(c)
            except:
                pass


    def recieve(self):
        data = self.sock.recv(1024)
        data = tuple(data.decode())
        return data

    def myInfo(self):
        return (self.addresses, (self.host_name, self.ip, self.port))

    def myConns(self):
        return self.conns



class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 6573
        self.host = socket.gethostname()
        #Two connection methods self.connect((ip, port)) or self.create_connection((ip, port))

    def make_conn(self, ip):
        self.ip_conn = ip
        self.sock.connect((ip, self.port))

    def myInfo(self):
        return (self.host, self.port)

    def work(self):
        #Function that maintains a connection with the server class and is controlled by thread
        pass

    def transmit(self, data):
        data = str((data, self.host))
        data = data.encode()
        self.sock.send(data)

    def recieve(self):
        data = self.sock.recv(1024)
        data = tuple(data.decode())
        return data


def main():
    gameServer = Server(5, 1)
    hoi = "Hello Server!"
    ip = "192.168.20.226"
    print("Server made")
    gServer_thread = threading.Thread(target=gameServer.work)
    print(gameServer.myInfo())
    gameClient = Client()
    gameClient.make_conn("192.168.20.226")
    print("connection established")
    gClient_thread = threading.Thread(target=gameClient.transmit, args=hoi)
    print(gameServer.myInfo())
    gServer_thread.start()
    print(gameServer.recieve())
    gClient_thread.start()



if __name__ == "__main__":
    main()
