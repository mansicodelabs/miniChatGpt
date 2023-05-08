import string

# Read shakespear File
with open('tinyShakespearData', 'r') as f:
    content = f.read()

    # find all chars in the shakespear text
    chars = sorted(list(set(content)))

    # create a mapping from chars to integers
    stoi = {}
    itos = {}
    # enumerate chars (each char is associated with a number)
    integer_chars = enumerate(chars)
    # The loop assigns each pair of (index, character) in integer_chars to the variables i and c, respectively.
    for i, c in integer_chars:
        stoi[c] = i
        itos[i] = c
    print("stoi:", stoi)
    print("itos:", itos)


    # encoder
    def encode(string):
        return [stoi[char] for char in string]

    # decoder
    def decode(l):
        return ''.join([itos[i] for i in l])


    print(encode("hii there"))
    print(decode(encode("hii there")))
