import math

letters = input("Determine the letters of the dictionary ex.'A,B,C': ")
probabilities = input("Enter their probability ex. '1/2,1/5,2/5': ")
length = 5

encoded = int(input("Input the encoded code: "))
encoded /= 10 ** (int(math.log10(encoded)) + 1)

probabilities = list(map(lambda x: int(x.split('/')[0]) / int(x.split('/')[1]), probabilities.split(',')))
letters = letters.split(',')

dictionary = {}
total_prob = 0

for i, letter in enumerate(letters):
    start_prob = total_prob
    total_prob += probabilities[i]
    dictionary[letter] = (start_prob, total_prob)

sorted_dict = sorted(dictionary.items(), key=lambda x: x[1])

decoded = ""
current_length = 0

while current_length < length:
    for letter, (start_prob, end_prob) in sorted_dict:
        if encoded < end_prob:
            mid_range = end_prob - start_prob
            decoded += letter
            current_length += 1
            break

    encoded = (encoded - start_prob) / mid_range

print(decoded)

input()
