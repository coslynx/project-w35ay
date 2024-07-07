import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class ContentManagement:
    def __init__(self):
        self.posts = pd.DataFrame(columns=['title', 'content', 'category', 'priority'])
    
    def add_post(self, title, content, category, priority):
        new_post = pd.DataFrame([[title, content, category, priority]], columns=['title', 'content', 'category', 'priority'])
        self.posts = pd.concat([self.posts, new_post], ignore_index=True)
    
    def remove_post(self, title):
        self.posts = self.posts[self.posts['title'] != title]
    
    def prioritize_posts(self):
        self.posts = self.posts.sort_values(by='priority', ascending=False)
    
    def categorize_posts(self):
        categories = self.posts['category'].unique()
        categorized_posts = {}
        for category in categories:
            categorized_posts[category] = self.posts[self.posts['category'] == category]
        return categorized_posts
    
    def analyze_sentiment(self):
        nltk.download('vader_lexicon')
        sia = SentimentIntensityAnalyzer()
        self.posts['sentiment_score'] = self.posts['content'].apply(lambda x: sia.polarity_scores(x)['compound'])
    
    def get_top_posts(self, n):
        return self.posts.nlargest(n, 'priority')