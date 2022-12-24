import pickle


def decode():
    f = open("rotors.enigma", "rb")
    result = pickle.load(f)
    f.close()
    return result


alphabet = "abcdefghijklmnopqrstuvwxyz"
res = decode()
