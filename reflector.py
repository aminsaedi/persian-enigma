alphabet = "abcdefghijklmnopqrstuvwxyz"
rev = alphabet[::-1]


def reflector(char):
    index = alphabet.index(char)
    result = rev[index]
    return result


def test_reflector():
    assert reflector("a") == "z"
    assert reflector("g") == "t"
    assert reflector("y") == "b"


if __name__ == "__main__":
    test_reflector()
    print("All test passed successfully!")
