import base64
import hashlib
from cryptography.fernet import Fernet



class EncryptOrDecrypyt():
  def __init__(self, key: str, detail: str, password: str, UserDataObj: dict):
    self.key = key
    self.detail = detail
    self.password = password
    self.token = None
    self.fernetObj = Fernet(self.key)

    #For Decryption
    self.UserDataObj = UserDataObj


  def UserInputconversion(self):

    hashed = hashlib.sha256(self.key.encode()).digest()
    base64Key = base64.urlsafe_b64encode(hashed)
    return base64Key

  def encrypt(self):
    encryptedDetail = self.fernetObj.encrypt(self.detail).decode()
    encryptedPassword = self.fernetObj.encrypt(self.password).decode()

    return {
      encryptedDetail: encryptedPassword
    }
    
  
  def decrypt(self):
    pass
    