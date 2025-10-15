
    else:
        return False

def uploadFile(sock):

    file_name = input('Выберите файл: ')
    if check_file(file_name):

        sock.send('upload file'.encode('utf-8'))

        file_size = os.path.getsize(file_name)

        sock.send(f'{file_name} | {file_size}'.encode('utf-8'))


        with open
            print(f"[!] Ошибка: {e}")
            break

    sock.close()

if __name__ == "__main__":
    main()

