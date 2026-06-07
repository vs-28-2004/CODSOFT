import torch.nn as nn


class CaptionModel(nn.Module):
    def __init__(self, vocab_size, embedding_size=256):
        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            embedding_size
        )

        self.lstm = nn.LSTM(
            embedding_size,
            256,
            batch_first=True
        )

        self.linear = nn.Linear(
            256,
            vocab_size
        )

    def forward(self, captions):
        embedded = self.embedding(captions)

        output, _ = self.lstm(embedded)

        output = self.linear(output)

        return output