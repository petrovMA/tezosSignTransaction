import base58check
import binascii
import ed25519
from pyblake2 import blake2b

secret = (base58check.b58decode(b'<private_key>').hex()[8:72])

operation = binascii.unhexlify(open("operation.hex", "rb").readline())
seed = binascii.unhexlify(secret)

h = blake2b(digest_size=32)
h.update(b'\x03' + operation)
digest = h.digest()

sk = ed25519.SigningKey(seed)
sig = sk.sign(digest)
print("Signature: " + sig.hex())
