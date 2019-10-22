import socket
import time
my_name = socket.getfqdn(socket.gethostname())
my_addr = socket.gethostbyname(my_name)


def logs_on(data):
    f = open("logs.txt", "a+", encoding='utf-8')
    f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"\n")
    f.write(my_addr+"\n")
    f.write(data+"\n")
    f.close()
    return 0
