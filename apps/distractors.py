import os

from sense2vec import Sense2Vec

# Get the base directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the model directory
S2V_MODEL_PATH = os.path.join(BASE_DIR, "s2v_old")

# Load Sense2Vec model using the absolute path
s2v = Sense2Vec().from_disk(S2V_MODEL_PATH)


def get_distractors(word, s2v):
    similarWords = set()  # Using a set to avoid duplicates
    word = word.lower().replace(" ", "_")
    try:
        sense = s2v.get_best_sense(word)
        most_similar = s2v.most_similar(
            sense, n=5
        )  # Get more similar words to ensure enough distinct options
        for each_word in most_similar:
            clean_word = each_word[0].split("|")[0].replace("_", " ")
            similarWords.add(clean_word)  # Add to set, which ensures uniqueness
    except KeyError:
        return ["No distractors found"]

    # Remove the original word from the distractors if it's present
    if word.replace("_", " ") in similarWords:
        similarWords.remove(word.replace("_", " "))

    # Convert the set back to a list and return the first 3 distinct distractors
    return list(similarWords)[:3]


if __name__ == "__main__":
    print(get_distractors("Nepal", s2v))
