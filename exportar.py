import socket, os
#os.popen("mysqldump -u root -p uriel bdd >  /home/uriel/BASH/tarea.sh")
os.popen("/home/uriel/")
ruta="/home/uriel/"
filename="university.sql"
HOST="192.168.43.90"
CPORT=9091
FPORT=9090
control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
control.connect((HOST,CPORT))
control.send("SEND" + filename)
control.close()
archivo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
archivo.connect((HOST,FPORT))
f=open(ruta+filename,"rb")
datos=f.read()
f.close()

archivo.send(datos)
archivo.close()
