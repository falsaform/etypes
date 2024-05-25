import pytest
import subprocess
import os
from tests.utils import costruct_relative_path

@pytest.mark.parametrize(
    "file_path, password, environment",
    [
        (
            costruct_relative_path("fixtures/ansible/development.py"),
            "development-password",
            "development"
        ),
        (
            costruct_relative_path("fixtures/ansible/staging.py"),
            "staging-password",
            "staging"
        ),
        (
            costruct_relative_path("fixtures/ansible/production.py"),
            "production-password",
            "production"
        ),
    ],
)
def test_ansible_vars_decrypt(file_path, password, environment):
    """
    Tests decryption of a file with 
    The expectation is that the file should be encrypted
    """

    env = os.environ.copy()
    env["ETYPES_FILE"] = file_path
    env["ETYPES_PASSWORD"] = password
    env["ANSIBLE_CONFIG"] = costruct_relative_path("ansible/ansible.cfg")
    env["ANSIBLE_STDOUT_CALLBACK"] = "yaml"

    command = [
        "ansible-playbook", "-i",
        costruct_relative_path("ansible/inventory.yml"),
        costruct_relative_path("ansible/server.yml"), 
        "-l", environment,
    ]
    result = subprocess.call(command, env=env)
    assert result == 0

def test_ansible_vars_decrypt_with_file():
    """
    Tests decryption of a file with 
    The expectation is that the file should be encrypted
    """

    password="development-password"
    password_file="/tmp/dynamic_loader_password_file"
    file_path = costruct_relative_path("fixtures/ansible/development_with_file.py")

    # remove the password file if it exists
    if os.path.isfile(password_file):
        os.remove(password_file)
   
    # write the password to the expected file
    with open(password_file, "w") as fp:
        fp.write(password)

    environment="development"
    env = os.environ.copy()
    env["ETYPES_FILE"] = file_path
    env["ANSIBLE_CONFIG"] = costruct_relative_path("ansible/ansible.cfg")
    env["ANSIBLE_STDOUT_CALLBACK"] = "yaml"
    command = [
        "ansible-playbook", "-i",
        costruct_relative_path("ansible/inventory.yml"),
        costruct_relative_path("ansible/server.yml"), 
        "-l", environment,
    ]
    result = subprocess.call(command, env=env)
    assert result == 0
