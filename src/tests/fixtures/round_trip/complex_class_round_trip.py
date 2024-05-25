from etypes import DecryptedSecret


class SomeClientWithSecrets:
    CLIENT_SECRET_ID = None
    CLIENT_SECRET_KEY = None

    @classmethod
    def __init__(cls):
        # secure secrets
        cls.CLIENT_SECRET_ID: DecryptedSecret = "AEX1235HAN"
        cls.CLIENT_SECRET_KEY: DecryptedSecret = "*(SAN(!NF))(SDAS)"
