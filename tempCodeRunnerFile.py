from flask import Flask, render_template, request
from sentiment_model import analyze_sentiment
from news_fetcher import fetch_news

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    articles = []
    sentiment_counts = {"POSITIVE": 0, "NEGATIVE": 0, "NEUTRAL": 0}

    if request.method == "POST":
        query = request.form["query"]
        news = fetch_news(query)

        for article in news[:12]:  # limit to 12 for speed
            title = article.get("title", "")
            description = article.get("description", "")
            date = article.get("publishedAt", "")[:10]
            text = f"{title or ''} {description or ''}".strip()

            label, score = analyze_sentiment(text)

            # handle missing labels safely
            if label not in sentiment_counts:
                sentiment_counts[label] = 0
            sentiment_counts[label] += 1

            articles.append({
                "title": title,
                "description": description,
                "label": label,
                "score": round(score, 2),
                "date": date
            })

    return render_template("dashboard.html", articles=articles, counts=sentiment_counts)

if __name__ == "__main__":
    app.run(debug=True)
