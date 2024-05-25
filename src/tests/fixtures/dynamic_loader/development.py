from etypes import EncryptedSecret

# password = DEVELOPMENT_PASSWORD


DATABASE_PASSWORD: EncryptedSecret = (
    "gAAAAABmT_vSzrPsyqnU0xPvmBvR9zWR7nT3G1MsyghuOCODeuwiskT5FMoFKucT81N5894LzFkxUXGsX8kOo6PPwaZab6eJ_UEMMWmAkVE2PjrH5Ghr8D8="
)
DATABASES = {
    "default": {
        "DATABASE_PASSWORD": DATABASE_PASSWORD,
    }
}
