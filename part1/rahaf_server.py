import socket,threading
import json
file=open("D:\\project\\network programming\\homework2\\venv\\data_for_server.json",'r')
dectionary=json.load(file)
file.close()

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind(("127.0.0.1",8888))
server_socket.listen(5)

def requests(num_of_client,client_socket,client_addrese):
    print("accepting client...",num_of_client,client_addrese)
    j=len(dectionary)
    k=0
    while True:
        storing_dic={}
        score=0
        for key,value in dectionary.items():
            client_socket.send(key.encode())
            client_answer=client_socket.recv(1024).decode()
            answer=int(client_answer)
            storing_dic[key]=[answer]
            k+=1

            if answer==(dectionary[key]):
                score+=1
        if k==j:

            print("client ",num_of_client,"  his score  ",score)
            break
            
num_of_client=1

while True:
    
    print("waitting for client...")
    client_socket,client_addrese=server_socket.accept()
    client_thread=threading.Thread(target=requests,args=(num_of_client,client_socket,client_addrese))
    client_thread.start()
    num_of_client+=1