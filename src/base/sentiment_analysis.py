import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def perform_sentiment_analysis(text):
    """
    Performs sentiment analysis on the given text using a pre-trained sentiment analysis model.

    Args:
        text (str): The text to be analyzed for sentiment.

    Returns:
        str: The predicted sentiment label ("Negative", "Neutral", or "Positive") of the input text.

    Raises:
        None

    Example:
        text = "I love this product! It exceeded my expectations."
        sentiment = perform_sentiment_analysis(text)
        print(sentiment)
        # Output: "Positive"
    """

    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt",
                       truncation=True, padding=True)

    # Perform forward pass through the model
    outputs = model(**inputs)

    # Get the predicted sentiment label
    predictions = torch.argmax(outputs.logits, dim=1).item()

    sentiment_labels = {0: "Negative", 1: "Neutral", 2: "Positive"}
    sentiment = sentiment_labels[predictions]

    return sentiment
