import hashlib

from utils import generate_seed, get_totp_key

username = "donaldtrump"
password_hash = "22e59a7a2792b25684a43d5f5229b2b5caf7abf8fa9f186249f35cae53387fa3"
ip_addr = "64.124.192.210"

seed = generate_seed(username, ip_addr)
totp = get_totp_key(seed)
print "[*] Found TOTP KEY: %s" % totp

passwords = None
with open('/usr/share/john/password.lst', 'r') as fd:
    passwords = fd.read().split()

password = None
for p in passwords:
    p_hash = hashlib.sha256(username+p).hexdigest()
    if p_hash == password_hash:
        password = p
        print "[*] Found password: %s" % p
        break

if password and totp:
    flag = hashlib.md5(totp+password).hexdigest()
    print "[+] Found flag: %s" % flag
