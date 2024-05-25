from etypes import AutoLoader, EncryptedSecret, EncryptedSecret
from tests.fixtures.ansible.common import *

ENV="prod"


DATABASE_PASSWORD: EncryptedSecret = (
    "gAAAAABmUUEaikmBRqrh_I8jI8izkKqcalMZYczojsyrXNcsoxGPnbLRCUL301wNMX9IQtP2wxTZspfrV6bc8LLuVCWQ7j4nijt-T9-phpRY4acuNgvESwA="
)

AWS_ACCESS_SECRET_KEY: EncryptedSecret = (
    "gAAAAABmUUEaEgxIiZJWR5qdM-ds-YAWZeGxcvbqDTx_enq6loFyZztTpoFPmelmNHRkmOdA9s8G6IYktNXOCpptudrBlBad_w=="
)
AWS_SECRET_ACCESS_KEY: EncryptedSecret = (
    "gAAAAABmUUEauQR-rmZny1N3r3_eZ8_T6XlieYFzBdF8bU_DcF49imjqbo72K13UEDGpyY-VY320adCy_rmPihQaLmibyHfYdB-3_b4stk0EZvSQO8-xSuM="
)


DATABASES = {
    "default": {
        "DATABASE_PASSWORD": DATABASE_PASSWORD,
        "DATABASE_HOST": "postgres",
        "DATABASE_PORT": 5432,
        "DATABASE_NAME": "postgres",
    }
}

AutoLoader("ETYPES_PASSWORD", locals())
