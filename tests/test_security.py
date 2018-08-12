import pytest
import base64
from Crypto import Random
from Crypto.Cipher import AES
from ec2tool.security import Security

message = 'hello world'


@pytest.fixture()
def cipher():
    return Security('secret')

def test_decryption_of_string(cipher):
    """
    Assert encrypted string
    """
    decrypted = cipher.decrypt('U6DQfhE17od2Qe4TPZFJHn3LOMkpPDqip77e4b5uv7s=')
    assert decrypted == message

def test_incorrect_decrypt_message(cipher):
    """
    Assertion error raised if incorrect message
    string is attempted to be decrypted
    """
    with pytest.raises(AssertionError):
        decrypted = cipher.decrypt('U6DQfhE17od2Qe4TPZFJHn3LOMkpPDqip77e4b5uv7s=')
        assert decrypted == 'Wrong string'

def test_encryption_of_string(cipher):
    """
    Asserts the encrytion of string
    with base64
    """
    iv = Random.new().read(AES.block_size)
    encrypted = cipher.encrypt(message)
    assert base64.b64encode(base64.b64decode(encrypted)) == encrypted
