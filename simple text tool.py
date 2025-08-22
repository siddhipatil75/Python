# Simple Text Analysis Tool 
from collections import Counter
# Input paragraph
text = input("Enter a paragraph of text: ").lower()

# Remove punctuation
for ch in ",.!?;:":
    text = text.replace(ch, "")

# Split into words
words = text.split()

# 1. Count total number of words
total_words = len(words)
print(f"Total number of words: {total_words}")

# 2. Count frequency of each word
word_freq = Counter(words)
print("\nWord Frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")


# 3. Count vowels in the entire text
vowels = "aeiou"
vowel_count = sum(1 for ch in text if ch in vowels)
print(f"\nTotal number of vowels: {vowel_count}")
