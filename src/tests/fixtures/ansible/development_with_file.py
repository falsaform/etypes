from etypes import AutoLoader, EncryptedSecret, EncryptedSecret
from tests.fixtures.ansible.common import *

ENV="dev"

DATABASE_PASSWORD: EncryptedSecret = (
    "gAAAAABmUUD8A6zQUvRszrw2GdvGb5wkkzBMDc2Hm3FH3A44oQ5JFBvRuEGAdyWBO4hOxEKwImuXcj46UMzEhHBNKWfkakpM3Y-qYZMyKyUarZp2kGWHoUc="
)

AWS_ACCESS_SECRET_KEY: EncryptedSecret = (
    "gAAAAABmUUD8_bWUPQAeQmSVCl0kGg-HBEtnQx1DPlUPPA8692IjokRgpCjk2dktkLnbrQY3dcyc9GnGEoXFYKBZGd2ck3uFMw=="
)

AWS_SECRET_ACCESS_KEY: EncryptedSecret = (
    "gAAAAABmUUD8N7poMPImKHa406mC1wthjVzLbvrRvwTYrQ_AnY5yPkxSRQ4mx5Oo2daRyUoHh_QAB9vPraMdHsVy88Xpg9yfVhN9F_JYkMTvY9g8p38Djko="
)


DATABASES = {
    "default": {
        "DATABASE_PASSWORD": DATABASE_PASSWORD,
        "DATABASE_HOST": "postgres",
        "DATABASE_PORT": 5432,
        "DATABASE_NAME": "postgres",
    }
}

NUMBER = 3 * 60

AutoLoader(locals=locals(),  password_file="/tmp/dynamic_loader_password_file")
