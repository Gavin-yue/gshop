import hashlib

#加密算法
def set_password(pwd):
    md = hashlib.md5()
    md.update(pwd.encode('utf-8'))
    md5_pwd = md.hexdigest()
    return md5_pwd
