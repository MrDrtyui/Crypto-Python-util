#!/usr/bin/python3
import requests
sess = requests.Session()

cookie = bytearray(b''.fromhex("28123600894ec0052e3ab9aa1f9bcfb35bae92387fcd8a27214ed5a229788af9f7ad36251c1d4d7f6af43f4372bfe406a4f90808fa32299d41cc7a825690c3b74952bd6be4415e9fb5d697cbd4d85ac900cb9cd3174de415855f90f0fce5673fa2a56cc6feb9101774de"))
def xor(A, B): return bytes([a ^ b for a, b in zip(A, B)])


cookie[76:80+1] = xor(cookie[76:80+1], xor(b' true', b'false'))
cookie[61:61+1] = xor(cookie[61:61+1], xor(b'2', b'5'))


for i in range(len(cookie)):
    flipped = cookie[:]
    flipped[i] ^= 0b11111111  # флипаем у i-го байта все биты
    res = sess.get("https://t-capybit-kdot8z7j.spbctf.org/funds",
                   cookies={"session": flipped.hex()})
    # берём байт 0x** из сообщения декодера utf-8
    leaked = res.text[res.text.find('0x'):][:4]
    leaked = int(leaked, 16) ^ 0b11111111  # флипаем биты обратно
    print(chr(leaked), end='', flush=True)
