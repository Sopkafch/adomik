


        with open(file_name, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                sock.sendall(chunk)

        print('Файл отправлен')
    else:
        print('Файл не найден')



def main(

    sock.close()

if __name__ == "__main__":
    main()

