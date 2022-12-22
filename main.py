from reflector import reflector
from decode_rotor import decode

rotors = decode()

alphabet = "abcdefghijklmnopqrstuvwxyz"

total_rotate_count = 0


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

    global total_rotate_count
    total_rotate_count += 1
    rotors[0] = rotator(rotors[0])
    if (total_rotate_count % 26 == 0):
        rotors[1] = rotator(rotors[1])
    if (total_rotate_count % 52 == 0):
        rotors[2] = rotator(rotors[2])

    return r1_back


def rotator(input):
    output = ""
    for index in range(len(input) - 1):
        output += input[index + 1]
    output += input[0]
    return output



plain = "hihihihi"
cipher = ""

for char in plain:
    cipher += enigma_for_char(char)

print("Plain: " + plain)
print("Cipher: " + cipher)
