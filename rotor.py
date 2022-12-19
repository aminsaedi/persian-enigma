from random import shuffle
import pickle

alphabet = "abcdefghijklmnopqrstuvwxyz"

r1 = list(alphabet)
shuffle(r1)

r2 = list(alphabet)
shuffle(r2)

r3 = list(alphabet)
shuffle(r3)

file = open("rotors", "wb")
pickle.dump([r1, r2, r3], file)
