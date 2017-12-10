import socket

#In progress networking classes
port = 6573
class Server:
    def __init__(self, timeout, max_users):
        self = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setdefaulttimeout(timeout)
        self.bind((6573, ip))
        self.listen(max_users)
        self.addresses = []

    def run(self):
        #Function that will be run and maintains connections between each Client
        c, addr = self.accept()
        self.addresses.add(addr)


class Client:
    def __init__(self, ip):
        self = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Two connection methods
        self.connect((6573, ip))

    def run(self):
        #Function that maintains a connection with the server class
        pass

def main():
    pass

if __name__ == "__main__":
    main()
