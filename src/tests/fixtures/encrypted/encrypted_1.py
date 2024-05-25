from etypes import EncryptedSecret, EncryptedSecret

POSTGRES_PASSWORD: EncryptedSecret = (
    "gAAAAABmT9yAQIIZu6LySLi5jYe4cA4QswdvHG_N_OOMnoJAJ5EVSVk_pXNHOsdl14LxEMl_1hrnOdnFBiat5Ij27rI4CtFOtg=="
)
GA_SECRET_ID: EncryptedSecret = (
    "gAAAAABmT9yA6HQOXF4BM6gvUG_ryKqrXK9BEgRY2W4lNQvDNBVbiCEOz50-viDLEMXA71upgcGgRbqvC-IAltbjE8w5MbSooJN5EV-8sVe1q3LndfBNzEg="
)


DATABASE = {
    "default": {"POSTGRES_PASSWORD": POSTGRES_PASSWORD, "POSTGRES_DB_NAME": "test"}
}
