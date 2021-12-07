

def hamming_distance(text1, text2):
    dist = 0
    for index in range(len(text1)):
        if text1[index] != text2[index]:
            dist += 1
    return dist


output_file = open("output.txt", "r", newline='')
encrypted_text = output_file.read()
output_file.close()

possible_key_lengths = {}
for key_length in range(10, 16):
    hamming_distances = position = counter = 0
    while position + 2 * key_length <= len(encrypted_text):
        section_one = encrypted_text[position:position + key_length]
        position += key_length
        section_two = encrypted_text[position:position + key_length]
        position += key_length
        hamming_distances += hamming_distance(section_one, section_two)
        counter += 1
        average_hamming_distance = hamming_distances / float(counter)

        possible_key_lengths[key_length] = average_hamming_distance / float(key_length)

# print(possible_key_lengths)
d = sorted(possible_key_lengths.items(), key=lambda item: item[1])
# print(d)
key_length = d[0][0]
key = []
for i in range(key_length):
    key.append({x: 0 for x in "ABCDEFGHIJKLMNOPQRTUVWXYZabcdefghijklmnopqrtuvwxyz0123456789"})

for poz in range(len(encrypted_text)):
    for charKey in "ABCDEFGHIJKLMNOPQRTUVWXYZabcdefghijklmnopqrtuvwxyz0123456789":
        if chr(ord(charKey) ^ ord(encrypted_text[poz])) in "abcdefghijklmnopqrtuvwxyz -.,":
            key[poz % key_length][charKey] += 1

# print(*key, sep="\n")

key_sol = ""
for ch in key:
    key_sol += max(ch, key=lambda key: ch[key])

with open("key.txt", "w", newline='') as k:
    k.write(key_sol)