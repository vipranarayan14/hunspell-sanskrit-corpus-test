import sys
import enchant

from enchant.tokenize import get_tokenizer

tknzr = get_tokenizer("en_US")

dictionary = enchant.Dict("sa_IN")

filepath = sys.argv[1]

print(f"Checking file: {filepath}")

text = open(filepath).read()

words = [word for word, _ in tknzr(text)]

results = [(word, dictionary.check(word)) for word in words]

correct_words = [result for result in results if result[1] is True]
incorrect_words = [result for result in results if result[1] is False]

total_words = len(words)
total_correct_words = len(correct_words)
total_incorrect_words = len(incorrect_words)
total_correct_words_perc = round((total_correct_words / total_words) * 100)
total_incorrect_words_perc = round((total_incorrect_words / total_words) * 100)

print(f"total words: {total_words}")
print(
    "total correct words: " f"{total_correct_words} i.e. {total_correct_words_perc} %"
)
print(
    "total incorrect words: "
    f"{total_incorrect_words} i.e. {total_incorrect_words_perc} %"
)
