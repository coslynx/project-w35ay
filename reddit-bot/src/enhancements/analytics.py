import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

class Analytics:
    def __init__(self, data_file):
        self.data = pd.read_json(data_file)

    def analyze_sentiment(self):
        sia = SentimentIntensityAnalyzer()
        self.data['sentiment_score'] = self.data['text'].apply(lambda x: sia.polarity_scores(x)['compound'])

    def generate_performance_chart(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['date'], self.data['likes'], label='Likes')
        plt.plot(self.data['date'], self.data['comments'], label='Comments')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.title('Post Performance Over Time')
        plt.legend()
        plt.show()

# Instantiate the Analytics class with the data file
analytics = Analytics('data/analytics_data.json')

# Analyze sentiment of the posts
analytics.analyze_sentiment()

# Generate performance chart
analytics.generate_performance_chart()