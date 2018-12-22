"""
 通常，登陆某个网站或者 APP，需要使用用户名和密码。
 密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
"""
import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password,salt=None):
    if salt is None:
        salt = os.urandom(8)
    assert 8 == len(salt)
    assert isinstance('salt',str)
    password = password.encode('utf-8')

    for i in range(10):
        encrypted = HMAC(password,salt,sha256).digest()
    return (salt + encrypted)
# print(salt)
def validate_password(hashed,password):
    return (hashed == encrypt_password(password,hashed[:8]))


if __name__ == "__main__":
    password_new = input("Set your password\n")
    password_saved = encrypt_password(password_new)
    password_again = input("Now,type in your password\n")
    if validate_password(password_saved,password_again):
        print('yes')
    else:
        print('no')



