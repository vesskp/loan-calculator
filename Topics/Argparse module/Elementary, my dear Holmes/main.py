#  write your code here 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file")
args = parser.parse_args()


def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)


filename = args.file
with open(filename, "r") as inf:
    decode_Caesar_cipher(inf.read(), -13)
