
# Read shakespear File
with open('tinyShakespearData', 'r') as f:
    content = f.read()
    print("length of dataset in characters: ", len(content))

    chars = sorted(list(set(content)))
    print("chars: ", ''.join(chars))
    print(len(chars))


