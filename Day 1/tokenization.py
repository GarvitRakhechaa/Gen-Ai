import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')
print(encoder.n_vocab)  # this is print vocab size

text = "Garvit is one of the best coder in the world"

tokens = encoder.encode(text)
print(tokens)

decoded = encoder.decode([44587, 25424, 382, 1001, 328, 290, 1636, 161238, 306, 290, 2375])
print(decoded)
