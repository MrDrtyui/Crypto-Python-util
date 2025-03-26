import requests
sess = requests.Session()

cookie = bytearray(b''.fromhex("28123600894ec0052e3abfa0039b98ec1efec27e389dcf65765bc4a5792bc8f7a1ba2a6b431f0c7d3ae93c4924a7e804f4f50b19b96c68d141c53dd904c381f40e05e93fa4180dc9a5dcc18381df5cd901c586d1075ae111db0bdff1f7e12477f6ea7ac9e6fe59152bd0d2b200680ccc88"))
def xor(A, B): return bytes([a ^ b for a, b in zip(A, B)])


cookie[68:68+1] = xor(cookie[68:68+1], xor(b'2', b'5'))
cookie[83:87+1] = xor(cookie[83:87+1], xor(b' true', b'false'))
cookie[89:109+1] = xor(cookie[89:109+1],
                       xor(b' "department": "sales', b' "allow-flag":   "yes'))


for i in range(len(cookie)):
    print(f'Position {i:3d}\t', end='')
    flipped = cookie[:]
    # флипаем у i-го байта младший бит — ксором на байт, у которого 1 только в младшем бите
    flipped[i] ^= 0b00000001
    res = sess.get("https://t-capybit-kdot8z7j.spbctf.org/funds",
                   cookies={"session": flipped.hex()})
    print(res.text)
