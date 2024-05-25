from etypes import DecryptedSecret

POSTGRES_PASSWORD: DecryptedSecret = "BlahblahSecret"
GA_SECRET_ID: DecryptedSecret = "this_is_a_secret"


DATABASE = {
    "default": {"POSTGRES_PASSWORD": POSTGRES_PASSWORD, "POSTGRES_DB_NAME": "test"}
}
