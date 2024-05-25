from etypes import EncryptedSecret

# Example of a django settings file
# password = SAJSa!*90AHNSN

DEBUG = True
ENVIRONMENT = "development"
BASE_URL = "https://some-website.dev"
ANALYTICS_ID: EncryptedSecret = (
    "gAAAAABmUCux5FJx-XhMpmc1bC3B1G9ZGtr9gimT7st2tBfQ7ZJgtY4rO14ydpCAXeYsRF6qm-V-p7s8VMMsbJHoydz44FNCVQ=="
)

DATABASE_NAME = "django"
DATABASE_USER = "django"
DATABASE_PASSWORD: EncryptedSecret = (
    "gAAAAABmUCuxhU-UOwlkaJhg9QDw67oGiFtNnMUZUIsgw2Ly4Ud6r6zZ4UPQ96NyvYlnrc_g6W_G4J1Q5AC7dIhVOJC_2ceRsyQG3ItzGudy1f48dWTkfH8="
)
DATABASE_HOST: EncryptedSecret = (
    "gAAAAABmUCuxJ6CDMjnxhVR-7GTujbKqyB5c0148jlSP06BA1nQq9FeE1C9lO5Yx9dBzJtai8IHDrrbEW3VC0kP--gnOqMYU9klQZDS9d68UETV5HfC7AUc="
)
DATABASE_PORT = 5432
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg",
        "NAME": DATABASE_NAME,
        "USER": DATABASE_USER,
        "PASSWORD": DATABASE_PASSWORD,
        "HOST": DATABASE_HOST,
        "PORT": DATABASE_PORT,
    }
}


# DJANGO
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

ALLOWED_HOSTS = [
    ".some-website.dev",
    ".api.some-website.dev",
]

# Mail settings
EMAIL_BACKEND = "app.backends.mail_backends.SafeMailGunEmailBackend"
DEFAULT_FROM_EMAIL = "some@email.address"
MAILGUN_SECRET_KEY: EncryptedSecret = (
    "gAAAAABmUCuxQaWg0qT7Eg7YRkGNwkLLGdusW4TfSIoI-1CyQZqbMuZhk0O2R1K-d4hcRVaNQcVKsqHLYoaWdSEtzv1JDkkBzAyhtzm6kcIKxudiipdpErkV_qlWr_fzR_ZhTMbxNyIi"
)
MAILGUN_DOMAIN_NAME = "MAILGUN"
MAILGUN_DEFAULT_FROM_ADDRESS = DEFAULT_FROM_EMAIL
ALLOWED_EMAIL_DOMAINS = None
ANYMAIL = {
    "MAILGUN_API_KEY": MAILGUN_SECRET_KEY,
    "MAILGUN_SEND_DEFAULTS": {"esp_extra": {"sender_domain": MAILGUN_DOMAIN_NAME}},
}

loaders = [
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    ),
]
