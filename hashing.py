import  bcrypt as bc
import socket
from time import time, sleep
import  PublicKey, CipherText

path = "C:\Users\juan2\Documents\cripto\Tarea4\Tarea4CriptoYSegRedes\HashyResultados\PotfileHash\hashcat-archivo1Dicc2.potfiles"
#hashArr1, hashArr2, hashArr3, hashArr4, hashArr5 = []
#password = b"TheSecretPassword55"

f1 = open("C:\Users\juan2\Documents\cripto\Tarea4\Tarea4CriptoYSegRedes\HashyResultados\PotfileHash\hashcat-archivo1Dicc2.potfiles", 'r')
f2 = open("C:\Users\juan2\Documents\cripto\Tarea4\Tarea4CriptoYSegRedes\HashyResultados\PotfileHash\hashcat-archivo2Dicc2.potfiles", 'r')
f3 = open("C:\Users\juan2\Documents\cripto\Tarea4\Tarea4CriptoYSegRedes\HashyResultados\PotfileHash\hashcat-archivo3Dicc2.potfiles", 'r')
f4 = open("C:\Users\juan2\Documents\cripto\Tarea4\Tarea4CriptoYSegRedes\HashyResultados\PotfileHash\hashcat-archivo4Dicc2.potfiles", 'r')
f5 = open("C:\Users\juan2\Documents\cripto\Tarea4\Tarea4CriptoYSegRedes\HashyResultados\PotfileHash\hashcat-archivo5Dicc2.potfiles", 'r')
port = 5012
s = socket.socket(socket.socket.AF_INET,socket.SOCK_STREAM)
lines = f.readlines()
s.bind(("127.0.0.1", port))
s.listen(2)
client , addr = s.accept()

t= []
t.append(f1.readlines())
t.append(f2.readlines())
t.append(f3.readlines())
t.append(f4.readlines())
t.append(f5.readlines())
passwd = [[],[],[],[],[]]
filepsswd = open("passwd", "w")

print("Cargando")



for i in range(0,len(t)):
    for j in range(0, len(t[i])):
        linea= t[i][j]
        if i== 0:
            passwd[i].append(linea[33:len(linea)].strip('\n'))
        if i== 1:
            passwd[i].append(linea[50:len(linea)].strip('\n'))
        if i== 2:
            passwd[i].append(linea[50:len(linea)].strip('\n'))
        if i== 3:
            passwd[i].append(linea[33:len(linea)].strip('\n'))
        filepsswd.writelines(passwd[i][len(passwd[i])-1]+"\n")
#hashed = bcrypt.hashpw(password, bcrypt.gensalt())
filepsswd.close()

for i in range(0, len(passwd)):
    fileReport= open("reports/bcryptReport"+str(i), "w")
    init = time()
    for j in range(0, len(passwd[i])):
        hasheado = 

cifAsim= open("CifradoAsimetrico", "r")
texto = cifAsim.readlines()
largo = len(texto)
for i in range(0, largo):