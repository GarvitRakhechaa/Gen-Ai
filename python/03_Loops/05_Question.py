# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

input_string = "Garvit"
repeated_char = ""
for char in input_string:
    if input_string.count(char) == 1:
        print(char)
        break
