def hello(word:str, chr:str) -> str:
    i: int = 0
    z: str = ""
    while i < len(word) - 1:
        if word[i] == chr:
            z = z + word[i]
        i += 1
    return z

print(hello("word", "r"))