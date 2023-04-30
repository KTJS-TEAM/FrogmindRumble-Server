from Utils.Reader import ByteStream
from Packets.Messages.Server.LoginOk import LoginOk
from Packets.Messages.Server.OwnHomeData import OwnHomeData
from Logic.Player import Player


class Login(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)

    def decode(self):
        self.readInt()
        self.lowID = self.readInt()
        self.token = self.readString()

        self.major = self.ReadVint()
        self.build = self.ReadVint()
        self.minor = self.ReadVint()

        self.fingerprint = self.readString()
        self.readString()
        self.unkn = self.readString()
        self.readString()
        self.phoneModel = self.readString() #phone model
        self.adid = self.readString() #ADID
        self.osV = self.readString()
        self.isAndroid = self.ReadBool() #is android
        self.readString()
        self.unknown = self.readString()
        self.lang = self.readString() #language
        self.ReadVint()
        self.readString()
        self.ReadBool()
        self.ReadBool()
        self.readString()
        self.ReadVint()
        self.readString()
        self.readString()
        self.readString()
        self.readString()
        self.ReadVint()
        self.readString()

    def process(self):
        LoginOk(self.device, self.lowID, self.token).Send()
        OwnHomeData(self.device).Send()