import socket
from threading import Thread

from lesson09.server.classes import Student

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)


def client_work(conn, addr):
    with conn:
        students = []
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            answer = str(data, "utf-8")
            if not data:
                break
            conn.sendall(data)
            if answer == "exit":
                continue
            params = answer.split(";")
            students.append(Student(params[0], params[1]))
        print("close client ", addr)
        print(students)


if __name__ == '__main__':

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
    #    students = []
        while True:
            print("wait for client")
            conn, addr = s.accept()
            Thread(target=client_work, args=(conn, addr)).start()