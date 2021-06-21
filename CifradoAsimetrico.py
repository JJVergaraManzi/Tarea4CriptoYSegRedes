class DH_Final(object):
    def __init__(self, pb_key1, pb_key2,pv_key):
        self.pb_key1 = pb_key1
        self.pb_key2 = pb_key2
        self.pv_key =  pv_key
        self.full = None

    def generate_partKey(self):
        partialkey= self.pb_key1**self.pb_key1
        partialkey= partialkey%self.pb_key2
        return partialkey
    
    def generateFullKey(self, pkr):
        full= pkr**self.pv_key
        full= full%self.pb_key2
        self.full= full
        return full
    
    def encriptMssg(self, mssg):
        encryptedMssg = ""
        key = self.full
        for i in mssg:
            encryptedMssg += chr(ord(c) -key)
        return encryptedMssg

    def DecriptMssg(self, mssg):
        decryptedMssg = ""
        key = self.full
        for i in mssg:
            decryptedMssg += chr(ord(c) -key)
        return decryptedMssg