import pandas as pd

data = pd.read_csv("dataset/captions.txt")

print("Dataset loaded successfully")
print(data.head())

words = set()

for text in data["caption"]:
    for word in str(text).split():
        words.add(word)

print("Vocabulary Size:", len(words))