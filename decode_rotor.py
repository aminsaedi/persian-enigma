import pickle


def decode():
    f = open("rotors.enigma", "rb")
    result = pickle.load(f)
    f.close()
    return result


alphabet = "abcdefghijklmnopqrstuvwxyz"
res = decode()
print(alphabet)
print(res[0])
print("------")
print(alphabet)
print(res[1])
print("------")
print(alphabet)
print(res[2])
