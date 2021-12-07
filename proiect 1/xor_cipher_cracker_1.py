

def xor_text(text1, text2):
    key = ""
    for index in range(len(text1)):
        key += chr(ord(text1[index]) ^ ord(text2[index]))
    return key


input_file = open("input.txt", "r", newline='')
output_file = open("output.txt",  "r", newline='')

text1 = input_file.read()
text2 = output_file.read()

input_file.close()
output_file.close()

key_repeated = xor_text(text1, text2)

first_30_characters = key_repeated[:30]

key = None
for possible_length in range(10, 16):
    is_correct_length = True
    for index in range(possible_length):
        if first_30_characters[index] != first_30_characters[index + possible_length]:
            is_correct_length = False
    if is_correct_length:
        key = first_30_characters[:possible_length]

with open("key.txt", "w", newline='') as k:
    k.write(key)