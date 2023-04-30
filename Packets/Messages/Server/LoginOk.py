import time
from Utils.Writer import Writer


class LoginOk(Writer):

    def __init__(self, device, lowID, token):
        self.id = 20104
        self.version = 1
        self.device = device
        self.lowID = lowID
        self.token = token
        super().__init__(self.device)

    def encode(self):
        self.writeInt(0) #accountid
        self.writeInt(self.lowID)
        self.writeInt(0) #homeid
        self.writeInt(self.lowID)
        self.writeString(self.token) #token
        self.writeString() #facebook id
        self.writeString() #gamecenter id
        self.writeVInt(2) #major
        self.writeVInt(3) #minor
        self.writeVInt(2) #bild
        self.writeVInt(2) #content
        self.writeString("dev") #env
        self.writeVInt(0)
        self.writeVInt(0) #play time sec
        self.writeVInt(0) #days since start playing hello my name is l-wr-ol-wrfgi00iro0
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeVInt(0)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString("0.0.0.0")