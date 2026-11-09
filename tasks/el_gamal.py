'''
I encrypted flag with El Gamal: p = 10007, g = 5

x is in range: [ 2100,2200 ]

encrypted flag in hex is

1f6a199a019311300cb11ad31f731c2206ee202018380267111b1ac018dd1a5108800f3e1036183209fe199e261606b615d314740649233013c522c20fcc15061ab3250a07850a1922bf1fd30ce21b980b4a03eb1bca08ea217721781b3f1ca3137505a7149223c523ff0fea03ec08f7045108630d291a84
'''


p = 10007
### g = 5 # to w sumie jest zbędne, służy do generowania

hex_data = "1f6a199a019311300cb11ad31f731c2206ee202018380267111b1ac018dd1a5108800f3e1036183209fe199e261606b615d314740649233013c522c20fcc15061ab3250a07850a1922bf1fd30ce21b980b4a03eb1bca08ea217721781b3f1ca3137505a7149223c523ff0fea03ec08f7045108630d291a84"

data = [int(hex_data[i:i+4], 16) for i in range(0, len(hex_data), 4)]

for x in range(2100, 2201):
    flag = ""
    for a, b in zip(data[::2], data[1::2]):
        m = b * pow(a, -x, p) % p
        flag += chr(m)

    if flag.startswith("PJATK"):
        print("x =", x)
        print("Flaga:", flag)

