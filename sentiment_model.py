from transformers import pipeline

# Load sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text[:512])  # truncate long texts
    label = result[0]["label"].upper()
    score = result[0]["score"]
    return label, score
