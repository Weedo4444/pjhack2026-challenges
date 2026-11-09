'''
Your task is to sign with RSA this word:

message = "zolw"

with this values:

n = 4295229443 | e = 17 | d = 2779181297

After converting this string to a number

Flag is PJATK{signatureinhex} Fe, if signature in decimal is 1505034578, then flag is PJATK{59b50152} because 1505034578 in hex is 0x59b50152 -> 59b50152
'''

message = "zolw"
n = 4295229443
d = 2779181297

m = int.from_bytes(message.encode(), "big") #big endian
signature = pow(m, d, n)

print(f"PJATK{{{signature:x}}}")