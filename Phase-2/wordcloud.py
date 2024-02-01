from collections import Counter

def generate_word_cloud(text):
    words = text.split()
    word_counts = Counter(words)

    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    sample_text = """
   This is my phase 2 of my internship in codes on bytes . Word clouds are a popular way to visualize text data. They represent the frequency of words in a given text by displaying them in varying sizes, with more frequent words appearing larger."""
    generate_word_cloud(sample_text)

