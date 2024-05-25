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
        "-l", environment
    ]
    result = subprocess.call(command, env=env)
    