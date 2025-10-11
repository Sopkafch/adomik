# admin_socket.py
import socket
import threading
import os

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            print(message)

        except:
            break

def check_file(file):
    dir_list = os.listdir()
    if file in dir_list:
       return True
    else:
        return False

def uploadFile(sock):

    file_name = input('Выберите файл: ')
    if check_file(file_name):

        sock.send('upload file'.encode('utf-8'))

        file_size = os.path.getsize(file_name)

        sock.send(f'{file_name} | {file_size}'.encode('utf-8'))


        with open(file_name, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                sock.sendall(chunk)

        print('Файл отправлен')
    else:
        print('Файл не найден')



def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("45.143.93.78", 10000))
    sock.sendall(b'I8t12ok89u-k9u!@#e4')  # говорим серверу, что это админ

    # Запускаем поток, который слушает сервер
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    while True:
        try: 
            msg = input("$ ").strip()
            if not msg:
                continue

            if msg == 'upload file':
                uploadFile(sock)   
                continue    

            sock.sendall(msg.encode('utf-8'))

        except (KeyboardInterrupt, EOFError):
            print("\n[!] Выход")
            break
        except Exception as e:
            print(f"[!] Ошибка: {e}")
            break

    sock.close()

if __name__ == "__main__":
    main()
