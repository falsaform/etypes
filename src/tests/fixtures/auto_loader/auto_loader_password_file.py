from etypes import AutoLoader, EncryptedSecret


DATABASE_PASSWORD: EncryptedSecret = (
    "gAAAAABmUCuxhU-UOwlkaJhg9QDw67oGiFtNnMUZUIsgw2Ly4Ud6r6zZ4UPQ96NyvYlnrc_g6W_G4J1Q5AC7dIhVOJC_2ceRsyQG3ItzGudy1f48dWTkfH8="
)

AWS_ACCESS_SECRET_KEY: EncryptedSecret = (
    "gAAAAABmUEEmoVjZ8ndO6AaSs_5nOkTd8Vq_kN-6e2sVw6HL1JYRCp-FYeEOroocZqad7L6R11z_iUNWNafnCWqvmwpgHo4UAlT5TEN9M3ajWRElJ73P1Wk="
)
AWS_SECRET_ACCESS_KEY: EncryptedSecret = (
    "gAAAAABmUEEmGIcmi4AsCFKsNXqEeyTUu45Zo7CmVSAEDXogNbPFUlWZ-zwv3bDPRhxPqvE0B2njoIvm6RaLVt5ivWqmkMTr_iUJVnx_sjUGNGLMIEJrCDiZcFYB3QbqxXia1W8b7GXP"
)

DATABASES = {
    "default": {
        "DATABASE_PASSWORD": DATABASE_PASSWORD,
        "DATABASE_HOST": "postgres",
        "DATABASE_PORT": 5432,
        "DATABASE_NAME": "postgres",
    }
}

AutoLoader(locals(), password_file="/tmp/dynamic_loader_password_file")