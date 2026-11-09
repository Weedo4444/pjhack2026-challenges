'''
This is encoded flag:

UEpBVEt7QmFzaWNfQmFzZTY0fQ==

Take it, decode and get your first flag!
'''


import base64

encoded = "UEpBVEt7QmFzaWNfQmFzZTY0fQ=="

decoded = base64.b64decode(encoded).decode("utf-8")

print(decoded)