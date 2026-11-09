'''
I've encrypted this flag with AES-256 in CBC mode

MrV6tMNzNODhN6K/BTktHbgl5Nl4ZJacby/zfeVEL7QYpUGW1bc4P2utIQ8EHrsy <- this is encrypted flag written in base64

b"abcdcbdaeffe21436587098523830cdc" <- this is key

b"1337337171137331" <- this is Initial Value

Try to retrieve it!
'''

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

encrypted = "MrV6tMNzNODhN6K/BTktHbgl5Nl4ZJacby/zfeVEL7QYpUGW1bc4P2utIQ8EHrsy"

key = b"abcdcbdaeffe21436587098523830cdc"
iv = b"1337337171137331"

data = base64.b64decode(encrypted)
cipher = AES.new(key, AES.MODE_CBC, iv)

flag = unpad(cipher.decrypt(data), 16)

print(flag.decode())
