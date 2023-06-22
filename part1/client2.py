import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(100)

try:
    client_socket.connect(("127.0.0.1", 8888))

    while True:
        question = client_socket.recv(1024).decode()
        print(question)
        answer = input("write your answer here")
        client_socket.sendall(answer.encode())

except socket.error as err:
    print(err)

finally:
    client_socket.close()
