import os
import sys
import pytest
from etypes.exceptions import (
    PasswordError,
    NoPasswordProvidedError, 
    NoPasswordFileProvidedError,    
    )

def test_auto_loader_password():
    """
    Test decryptig a file automatically on import with a environment_var_
    """
    # set the expected environment variable password
    os.environ['DEVELOPMENT_PASSWORD'] = 'SAJSa!*90AHNSN'
    # import the test file
    from tests.fixtures.auto_loader import auto_loader_password
    
    assert auto_loader_password.DATABASES
    # confirm that the file has been decrypted and matches the expected password
    assert auto_loader_password.DATABASES['default']['DATABASE_PASSWORD'] == 'superSecretPassword'
    
def test_auto_loader_password_file():
    """
    Test decrypting a file automatically with a password file
    """
    # write the password to the expected file
    with open("/tmp/dynamic_loader_password_file", "w") as fp:
        fp.write('SAJSa!*90AHNSN')

    from tests.fixtures.auto_loader import auto_loader_password_file
    
    assert auto_loader_password_file.DATABASES
    # confirm that the file has been decrypted and matches the expected password
    assert auto_loader_password_file.DATABASES['default']['DATABASE_PASSWORD'] == 'superSecretPassword'


def test_auto_loader_password_exception_1():
    """
    Test decryptig a file automatically on import with a environment_var_
    """
    # set the expected environment variable password
    os.environ['DEVELOPMENT_PASSWORD'] = ''
    # import the test file

    with pytest.raises(NoPasswordProvidedError):
        from tests.fixtures.auto_loader import auto_loader_password
        # we reload the module as its already been imported in previous tests
        import importlib
        importlib.reload(auto_loader_password) 

def test_auto_loader_password_exception_2():
    """
    Test decryptig a file automatically on import with a environment_var_
    """
    # delete the environment variable to be sure its not set
    os.environ.pop('DEVELOPMENT_PASSWORD', None)
    # dont set the expected environment variable password

    with pytest.raises(NoPasswordProvidedError):
        from tests.fixtures.auto_loader import auto_loader_password
        # we reload the module as its already been imported in previous tests
        import importlib
        importlib.reload(auto_loader_password) 



def test_auto_loader_password_exception_3():
    """
    Test decrypting exception of the incorrect password set when importing a 
    file with AutoLoader set

    """
    # delete the environment variable to be sure its not set
    os.environ.pop('DEVELOPMENT_PASSWORD', None)
    os.environ['DEVELOPMENT_PASSWORD'] = 'incorrect_password'
    # dont set the expected environment variable password

    # import the test file
    from tests.fixtures.auto_loader import auto_loader_password
    with pytest.raises(PasswordError):
        # we reload the module as its already been imported in previous tests
        import importlib
        importlib.reload(auto_loader_password) 


     
def test_auto_loader_password_file_exception_1():
    """
    Test decrypting a file automatically with a password file
    No not provide the expected password file
    """
    # write the password to the expected file
    if os.path.isfile('/tmp/dynamic_loader_password_file'):
        os.remove('/tmp/dynamic_loader_password_file')

    from tests.fixtures.auto_loader import auto_loader_password_file
    with pytest.raises(NoPasswordFileProvidedError):
        # we reload the module as its already been imported in previous tests
        import importlib
        importlib.reload(auto_loader_password_file) 
    
  