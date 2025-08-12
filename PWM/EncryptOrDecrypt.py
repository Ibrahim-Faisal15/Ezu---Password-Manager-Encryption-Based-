import base64
import hashlib
from cryptography.fernet import Fernet



class EncryptOrDecrypyt():
  def __init__(self, key: str, detail: str, password: str):
    self.key = key
    self.detail = detail
    self.password = password
    self.token = None
    self.hashed = hashlib.sha256(self.key.encode()).digest()
    self.base64Key = base64.urlsafe_b64encode(self.hashed)
    self.fernetObj = Fernet(self.base64Key)

  def encrypt(self):
    encryptedDetail = self.fernetObj.encrypt(bytes(self.detail, "utf-8")).decode()
    encryptedPassword = self.fernetObj.encrypt(bytes(self.password, "utf-8")).decode()
    

    return {
      encryptedDetail: encryptedPassword
    }
    
  
  def decrypt(self, dictData: dict):
   
    encryptedDetail = list(dictData.keys())[0]
    encryptedPassword = list(dictData.values())[0]


    decryptedDetail = self.fernetObj.decrypt(encryptedDetail).decode()
    decryptedValue = self.fernetObj.decrypt(encryptedPassword).decode()
    return decryptedDetail, decryptedValue
    