# Question 6
# Review word-frequency report.
# Pipeline of four steps:
#   (a) read_reviews()    - read the file safely
#   (b) word_frequency()  - clean and count the words
#   (c) top_words()       - rank them
#   (d) save_summary()    - write the summary

reviews_processed = 0     # number of comments read, reported by save_summary()


def read_reviews(filename):
    """Return the non-blank, stripped comments in the file as a list of
    strings."""
    global reviews_processed
    reviews = []
    try:
        with open(filename, "r") as file:
            for line in file:
                comment = line.strip()      # remove leading/trailing whitespace
                if comment != "":           # ignore blank lines
                    reviews.append(comment)
    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
    reviews_processed = len(reviews)
    return reviews


def word_frequency(reviews):
    """Return a dictionary of word -> count across all comments
    (case-insensitive)."""
    frequency = {}
    for comment in reviews:
        cleaned = "".join(ch for ch in comment.lower() if ch not in ".,!?;:")
        for word in cleaned.split():
            if word not in frequency:
                frequency[word] = 0
            frequency[word] += 1
    return frequency


def top_words(freq_dict, n):
    """Return the n most frequent words, highest count first, ties
    alphabetical."""
    ranked = sorted(freq_dict, key=lambda word: (-freq_dict[word], word))
    return ranked[:n]


def save_summary(filename, freq_dict, top_n):
    """Write the review summary report to the given file."""
    with open(filename, "w") as file:
        file.write(f"Total reviews processed: {reviews_processed}\n")
        file.write(f"Total unique words found: {len(freq_dict)}\n")
        file.write(f"Top {top_n} words:\n")
        for word in top_words(freq_dict, top_n):
            file.write(f"{word} : {freq_dict[word]}\n")


if __name__ == '__main__':
    comments = read_reviews("reviews.txt")
    counts = word_frequency(comments)
    save_summary("summary.txt", counts, 5)
    print("Summary written to summary.txt")
