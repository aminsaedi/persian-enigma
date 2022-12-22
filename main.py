from reflector import reflector
from decode_rotor import decode

rotors = decode()

alphabet = "abcdefghijklmnopqrstuvwxyz"


def enigma_for_char(char):
    r0 = alphabet.find(char)
    r1 = rotors[0][r0]
    r1 = alphabet.find(r1)
    r2 = rotors[1][r1]
    r2 = alphabet.find(r2)
    r3 = rotors[2][r2]
    reflected = reflector(r3)
    r3_back_index = rotors[2].find(reflected)
    r3_back = alphabet[r3_back_index]
    r2_back_index = rotors[1].find(r3_back)
    r2_back = alphabet[r2_back_index]
    r1_back_index = rotors[0].find(r2_back)
    r1_back = alphabet[r1_back_index]

    return r1_back


plain = "a"
cipher = ""

for char in plain:
    cipher += enigma_for_char(char)

print("Plain: " + plain)
print("Cipher: " + cipher)
