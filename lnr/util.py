# sha256 for password
import hashlib

def get_sha256(password: str):
    str = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return str