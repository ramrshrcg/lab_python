#11)WAP to ask for a sentence and calculate the frequency of characters in the sentences.
sentence = input("enter a sentence")
frequency = {}
for char in sentence:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)
