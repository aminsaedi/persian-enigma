from reflector import reflector
from decode_rotor import decode as rotor_decode

decode_rotors = rotor_decode()
encode_rotors = rotor_decode()

alphabet = "abcdefghijklmnopqrstuvwxyz"

count_decode = 0
count_encode = 0


def decode_rotate():
    global count_decode
    count_decode += 1
    decode_rotors[0] = rotator(decode_rotors[0])
    if (count_decode % 26 == 0):
        decode_rotors[1] = rotator(decode_rotors[1])
    if (count_decode % 52 == 0):
        decode_rotors[2] = rotator(decode_rotors[2])


def encode_rotate():
    global count_encode
    count_encode += 1
    encode_rotors[0] = rotator(encode_rotors[0])
    if (count_encode % 26 == 0):
        encode_rotors[1] = rotator(encode_rotors[1])
    if (count_encode % 52 == 0):
        encode_rotors[2] = rotator(encode_rotors[2])


def rotator(input):
    output = ""
    for index in range(len(input) - 1):
        output += input[index + 1]
    output += input[0]
    return output


def enigma_for_char(char):
    r0 = alphabet.find(char)
    r1 = encode_rotors[0][r0]
    r1 = alphabet.find(r1)
    r2 = encode_rotors[1][r1]
    r2 = alphabet.find(r2)
    r3 = encode_rotors[2][r2]
    reflected = reflector(r3)
    r3_back_index = encode_rotors[2].find(reflected)
    r3_back = alphabet[r3_back_index]
    r2_back_index = encode_rotors[1].find(r3_back)
    r2_back = alphabet[r2_back_index]
    r1_back_index = encode_rotors[0].find(r2_back)
    r1_back = alphabet[r1_back_index]
    encode_rotate()
    return r1_back


def decode_char(char):
    r1 = decode_rotors[0][alphabet.find(char)]
    r2 = decode_rotors[1][alphabet.find(r1)]
    r3 = decode_rotors[2][alphabet.find(r2)]
    reflected = reflector(r3)
    r3_rev = alphabet[decode_rotors[2].find(reflected)]
    r2_rev = alphabet[decode_rotors[1].find(r3_rev)]
    r1_rev = alphabet[decode_rotors[0].find(r2_rev)]
    decode_rotate()
    return r1_rev


def encode(i):
    cipher = ""
    for char in i:
        cipher += enigma_for_char(char)
    return cipher


def decode(i):
    decoded = ""
    for char in i:
        decoded += decode_char(char)
    return decoded
