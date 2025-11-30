# sentence = "hola mundo the quick brown fox jumps over the lazy dog pelopincho"
# words = sentence.split()
# print(words)
#
# length_words = []
# for word in words:
#     if word != "the":
#         length_words.append(len(word))
#
# print(length_words)

sentence = "movistar arena monitoreo de redes y firewall, and also linux enterprise systems"
words = sentence.split()
sentences_length = [len(word) for word in words if word != 'y']
print(sentence)
print(words)
print(sentences_length)

# numbers exercise
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [number for number in numbers if number > 0]
print(newlist)


# extract names starting with a
names = ["Alex", "John", "Alice", "Mark", "Angela", "Bob"]
names_start_with_a = [name for name in names if name[0]== 'A']
print(names_start_with_a)

# multiply only even numbers by 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
triple_even = [number*3 for number in numbers if number%2 == 0]
print(triple_even)

# extract all letters except vowels
text = "List Comprehension"
letters = [letter for letter in text if letter.lower() not in ['a', 'e', 'i', 'o', 'u']]
print(letters)
