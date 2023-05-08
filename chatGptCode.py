import torch
import numpy

# Read shakespear File
with open('tinyShakespearData', 'r') as f:
    content = f.read()

    # find all chars in the shakespear text
    chars = sorted(list(set(content)))
    print(len(chars))
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

    # encode shakespear dataset and store it in a torch.tensor
    data = torch.tensor(encode(content), dtype=torch.long)
    print(data.shape, data.dtype)
    print(data[:1000])

    # split data into train and validation
    # first 90% will be train data
    n = int(0.9 * len(data))
    train_data = data[:n]
    val_data = data[n:]

    # ---------------------------------------------------------
    # why do we need x and y?t
    block_size = 8

    x = train_data[:block_size]
    y = train_data[1:block_size + 1]
    for t in range(block_size):
        context = x[:t + 1]
        target = y[t]
        print(f"when input is {context} the target: {target}")

    # ----------------------------------------------------------
    # how many sequences will we process in parallel

    batch_size = 4
    torch.manual_seed(1337)

    # if split is 'train' we use train data
    # this function ca be used during both training and validation
    def get_batch(split):
        data = train_data if split == 'train' else val_data
        # torch.randint(high, size) -> generates size(4) integers between 0 and high-1
        ix = torch.randint(len(data) - block_size, (batch_size,))
        # stacks 4 input sequences that have starting index as ix
        x = torch.stack([data[i:i + block_size] for i in ix])
        # stacks 4 output sequences that have starting index as ix+1
        y = torch.stack([data[i + 1:i + block_size + 1] for i in ix])
        return x, y




