import pytest

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
def test_round_trip_encryption(file_path, password):
    """
    Tests round trip encryption and decryption
    The expectation is that the original file should match the file  after encryption and decryption
    """

    with create_temporary_copy(file_path) as fh:
        temp_path = fh.name
        original = open(temp_path, "r").read()
        encrypt_file(temp_path, password)
        encrypted = open(temp_path, "r").read()
        decrypt_file(temp_path, password)
        decrypted = open(temp_path, "r").read()
        assert original != encrypted
        assert original == decrypted
