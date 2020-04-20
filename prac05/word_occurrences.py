"""
CP1404/CP5632 Practical
Word occurrences in a string
"""

"""Author: Nang Seng Khan
   Date: 20/04/2020 
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""

word_to_count = {}
text = input("Text: this is a collection of words of nice words this is a fun thing it is ")
text = "this is a collection of words of nice words this is a fun thing it is "
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
    words = list(word_to_count.keys())
    words.sort()
    max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))

