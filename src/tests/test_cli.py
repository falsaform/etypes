import pytest
import subprocess

from tests.utils import costruct_relative_path, create_temporary_copy
from etypes.processor import decrypt_file, encrypt_file


@pytest.mark.parametrize(
    "file_path, password",
    [
        (
            costruct_relative_path("fixtures/round_trip/simple_round_trip.py"),
            "TESTPASSWORD_1",
        ),
        (
            costruct_relative_path("fixtures/round_trip/transform_round_trip.py"),
            "TESTPASSWORD_2",
        ),
        (
            costruct_relative_path("fixtures/round_trip/complex_class_round_trip.py"),
            "TESTPASSWORD2",
        ),
    ],
)
def test_cli_round_trip(file_path, password):
    """
    Tests round trip encryption and decryption of a file via the cli
    The expectation is that the file should be encrypted
    """

    def run(verbose=True):
        # without verbose
        with create_temporary_copy(file_path) as fh:
            temp_path = fh.name
            original = open(temp_path, "r").read()
            if verbose:
                subprocess.call(["etypes", "encrypt", "-p", password, temp_path])
            else:
                subprocess.call(
                    ["etypes", "encrypt", "--verbose", "-p", password, temp_path]
                )

            encrypted = open(temp_path, "r").read()
            if verbose:
                subprocess.call(["etypes", "decrypt", "-p", password, temp_path])
            else:
                subprocess.call(
                    ["etypes", "decrypt", "--verbose", "-p", password, temp_path]
                )

            decrypted = open(temp_path, "r").read()
            assert original != encrypted
            assert original == decrypted

    run(verbose=True)
    run(verbose=False)
