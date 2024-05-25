import pytest

from tests.utils import  costruct_relative_path
from etypes.helpers import dynamic_import


def test_dynamic_loader():
    """
    Test loading a file with encrypted strings and loading them into globals
    """

    file_path = costruct_relative_path("fixtures/dynamic_loader/development.py")
    password = "DEVELOPMENT_PASSWORD"
    
    with pytest.raises(KeyError):
        # Check that there are no DATABASES in globals in this context
        globals()['DATABASES']
    
    # load the development python file in with the correct password
    dynamic_import(globals() , file_path, password=password)

    # grab the decrypted and loaded DATABASE property from globals
    DATABASES = globals()['DATABASES']
    assert DATABASES
    # confirm that the file has been decrypted and matches the expected password
    assert DATABASES['default']['DATABASE_PASSWORD'] == 'SuperSecurep@ssw0d'
    
    # cleanup globals as they can affect the next test
    del globals()['DATABASES']
    del globals()['DATABASE_PASSWORD']


def test_dynamic_complex_loader():
    """
    Test loading a complex file with encrypted strings and loading them into globals
    """

    file_path = costruct_relative_path("fixtures/dynamic_loader/development_complex.py")
    complex_password = 'SAJSa!*90AHNSN'
    
    with pytest.raises(KeyError):
        # Check that there are no DATABASE_PASSWORD in globals in this context
        globals()['DATABASE_PASSWORD']

    with pytest.raises(KeyError):
        # Check that there are no ANALYTICS_ID in globals in this context
        globals()['ANALYTICS_ID']
        
    
    # load the development python file in with the correct password
    dynamic_import(globals() , file_path, password=complex_password)

    # grab the decrypted and loaded DATABASE property from globals
    DATABASE_PASSWORD = globals()['DATABASE_PASSWORD']
    ANALYTICS_ID = globals()['ANALYTICS_ID']
    
    assert DATABASE_PASSWORD
    assert ANALYTICS_ID

    # confirm that the file has been decrypted and matches the expected results
    assert DATABASE_PASSWORD == "superSecretPassword"
    assert ANALYTICS_ID == 'GTM-XXXXX'
    