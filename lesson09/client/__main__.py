import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server
if __name__ == '__main__':

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            message = input("Enter message")
            s.sendall(message.encode("utf-8"))
            data = s.recv(1024)
            if message == "exit":
                break
            print('Received', repr(data))