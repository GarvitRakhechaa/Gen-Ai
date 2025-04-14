def customTokenizer():
    chars = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ऑ', 'आ', 'अः', 'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'ल', 'व', 'श', 'ष', 'स', 'ह', 
        '०', '१', '२', '३', '४', '५', '६', '७', '८', '९', '॥', '॰', 'ऽ'
    ]

    tokens = {}
    def tokenMakerFunction():
        tokens.clear()
        for i in range(len(chars)):
            tokens[chars[i]] = (((i**3 + 5) * 3 + (i + 7)**2) % 1000)

    # tokenMakerFunction()

    def tokenConversionFunction():
        while True:
            user_input  = input("text for token conversion: ")
            token_sentence = []
            if isinstance(user_input, str):
                unavailable_chars = []
                for word in user_input.split():
                    for char in word:
                        if char not in chars and char not in unavailable_chars:
                            unavailable_chars.append(char)   
                print("acutally we dont have some of character but now we have added now please enter your input again")
                if unavailable_chars:
                    chars.extend(unavailable_chars)
                    tokenMakerFunction()
                    continue
                text_spilt = user_input.split()
                text_list = list(text_spilt)
                print(text_list)
                for text in text_list:
                    tokensum = 0
                    for char in text:
                        tokensum +=tokens[char]
                    token_sentence += [tokensum]
            print(token_sentence)
            break
    tokenMakerFunction()
    tokenConversionFunction()
customTokenizer()