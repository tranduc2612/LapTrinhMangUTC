import random
import socket
import threading
host = 'localhost'
port = 9050

def create_socket(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((host, port))
    sk.listen(5)
    return sk

def create_data(data):
    data = data + '\0'
    data = data.encode('utf-8')
    return data

def send_data(sk, data):
    arr = data.split(' ')
    if arr[0] == "loto":
        datanew = ""
        for i in range( int(arr[1])):
            datanew += str(random.randint(1, 99)) + " "
        data1 = create_data(datanew)
        sk.sendall(data1)
    else :
        data1 = create_data("Khong dung cu phap")
        sk.sendall(data1)
    
def recv_data(sk):
    data = bytearray()
    msg = ''
    while not msg:
        data1 = sk.recv(1024)
        if not data1:
            raise ConnectionError()
        data = data + data1
        if b'\0' in data1:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg
         
# Chữa bài
def process_client(client_sk, addr):
    try:
        data = recv_data(client_sk)
        print('{}:{}'.format(client_sk, data))
        send_data(client_sk, data)
    except ConnectionError:
        print("Error")
    finally: 
        client_sk.close()

if __name__ == '__main__':
    sk1 = create_socket(host, port)
    local_addr = sk1.getsockname()
    print('local address: {}'.format(local_addr))
    while True:
        # chữa
        client_sk, client_addr = sk1.accept()
        print('client address: {}'.format(client_addr))
        thread = threading.Thread(target=process_client, args=[client_sk, client_addr], daemon=True)
        thread.start()
        print('Connect from {}'.format(client_addr))
