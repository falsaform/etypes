from etypes import AutoLoader, EncryptedSecret, EncryptedSecret
from tests.fixtures.ansible.common import *

ENV="stage"

DATABASE_PASSWORD: EncryptedSecret = (
    "gAAAAABmUUEHlxGa1HzswigrUfKV9oU1aavt8H-kDTOpl-xQtjEv3tNAc8oeh8PPIJEtoeiZEhd7CB0tb5h_fpsZUlnI-QgjkA=="
)

AWS_ACCESS_SECRET_KEY: EncryptedSecret = (
    "gAAAAABmUUEHAWOALOo-n7e_Sg78dncvfW4vlR84W0BIFcNBtYDdHOEnZVf7_fN6JiougQLVPheiP3QG01ZnBi8NCUhdB7AN7w=="
)
AWS_SECRET_ACCESS_KEY: EncryptedSecret = (
    "gAAAAABmUUEH7xydud8bIrQ11psTXhC-qFBLRpfXKyGUh2udEm_fnRvmvGkd-CpUgjGI2iU68z77KLyOuPJV_WOH6zD4a0JMCw=="
)

DATABASES = {
    "default": {
        "DATABASE_PASSWORD": DATABASE_PASSWORD,
        "DATABASE_HOST": "postgres",
        "DATABASE_PORT": 5432,
        "DATABASE_NAME": "postgres",
    }
}

AutoLoader(locals(), password_var_name="ETYPES_PASSWORD")
