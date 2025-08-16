import os 

class file:
  def __init__(self):
    self.filename = "EZU.json"
    self.APP_DATA_PATH = os.getenv("APPDATA")
    self.filePath = None
    

  def createFile(self):
      os.makedirs("EZU", exist_ok=True)
      self.filePath = os.path.join(self.APP_DATA_PATH, self.filename)

      try:
        with open(self.filePath, "x") as file:
          print("File created....")
      except FileExistsError as e:
        os.remove(self.filePath)


  def read(self, data):
      try:
        with open(self.filePath, 'r') as file:
          r = file.read()
          return r
      except IOError as e:
        print(f"error read a file: {e}")

  def write(self, data):
    try:
      with open(self.filePath, "a") as file:
        a = file.write(data)
    except IOError as e:
        print(f"error writing a file: {e}")

        

  def remove():
    pass

  #Soon to be implemented

  def deleteAll(self):
     with open(self.filePath, "w") as file:
          pass
    

