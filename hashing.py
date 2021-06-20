import  bcrypt, glob, cv2

path = "C:/Users/juan2/Documents/tarea 4 criptografia/HashyResultados/PotfileHash/*.*"
#hashArr1, hashArr2, hashArr3, hashArr4, hashArr5 = []
#password = b"TheSecretPassword55"

for file in glob.glob(path):
    print(file)


#hashed = bcrypt.hashpw(password, bcrypt.gensalt())

