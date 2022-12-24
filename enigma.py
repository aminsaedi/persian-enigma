# from reflector import reflector
from decode_rotor import decode as rotors_generator

alphabet = "abcdefghijklmnopqrstuvwxyz"


def reflector(c):
    return alphabet[len(alphabet)-alphabet.find(c)-1]


class Enigma:

    r1, r2, r3 = rotors_generator()
    state = 0

    def rotator(self, input):
        return input[1:] + input[0]

    def decode_rotate(self):
        self.state += 1
        self.r1 = self.rotator(self.r1)
        if self.state % 26 == 0:
            self.r2 = self.rotator(self.r2)
        if self.state % (26 * 26) == 0:
            self.r3 = self.rotator(self.r3)

    def enigma(self, c):
        c1 = self.r1[alphabet.find(c)]
        c2 = self.r2[alphabet.find(c1)]
        c3 = self.r3[alphabet.find(c2)]
        reflected = reflector(c3)
        c3 = alphabet[self.r3.find(reflected)]
        c2 = alphabet[self.r2.find(c3)]
        c1 = alphabet[self.r1.find(c2)]
        self.decode_rotate()
        return c1

    def run(self, plain):
        cipher = ""
        for char in plain:
            cipher += self.enigma(char)
        return cipher


if __name__ == "__main__":
    e = Enigma()
    print(e.run("salamamin"))
    e2 = Enigma()
    print(e2.run("rpfixhlvs"))
