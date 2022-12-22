from random import shuffle
import pickle

alphabet = "abcdefghijklmnopqrstuvwxyz"

r1 = list(alphabet)
shuffle(r1)
r1 = ''.join(r1)

r2 = list(alphabet)
shuffle(r2)
r2 = ''.join(r2)

r3 = list(alphabet)
shuffle(r3)
r3 = ''.join(r3)

file = open("rotors.enigma", "wb")
pickle.dump([r1, r2, r3], file)
