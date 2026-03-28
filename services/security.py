from pwdlib import PasswordHash

hasher = PasswordHash.recommended()

def get_password_hash(password: str):
    return hasher.hash(password)

def verify_password(password: str, hash_password: str):
    return hasher.verify(password, hash_password)