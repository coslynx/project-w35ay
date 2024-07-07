import praw
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

class ModerationAssistance:
    def __init__(self, reddit_client_id, reddit_client_secret, reddit_user_agent):
        self.reddit = praw.Reddit(client_id=reddit_client_id,
                                  client_secret=reddit_client_secret,
                                  user_agent=reddit_user_agent)
    
    def monitor_rules(self, subreddit_name):
        subreddit = self.reddit.subreddit(subreddit_name)
        for submission in subreddit.new(limit=10):
            if submission.report_reasons:
                submission.mod.remove()
    
    def flag_inappropriate_content(self, subreddit_name):
        subreddit = self.reddit.subreddit(subreddit_name)
        for submission in subreddit.new(limit=10):
            sia = SentimentIntensityAnalyzer()
            submission_text = submission.title + submission.selftext
            sentiment_score = sia.polarity_scores(submission_text)['compound']
            if sentiment_score < -0.5:
                submission.report(reason="Inappropriate content")
    
    def notify_moderators(self, subreddit_name, message):
        subreddit = self.reddit.subreddit(subreddit_name)
        moderators = subreddit.moderator()
        for mod in moderators:
            self.reddit.redditor(mod).message('Notification', message)
    
    def generate_analytics(self, subreddit_name):
        subreddit = self.reddit.subreddit(subreddit_name)
        post_scores = []
        for submission in subreddit.top(limit=10):
            post_scores.append(submission.score)
        
        plt.bar(range(len(post_scores)), post_scores)
        plt.xlabel('Post Number')
        plt.ylabel('Post Score')
        plt.title('Post Performance Analytics')
        plt.show()

# Example Usage:
# mod_assistance = ModerationAssistance('client_id', 'client_secret', 'user_agent')
# mod_assistance.monitor_rules('test_subreddit')
# mod_assistance.flag_inappropriate_content('test_subreddit')
# mod_assistance.notify_moderators('test_subreddit', 'Please review the flagged content.')
# mod_assistance.generate_analytics('test_subreddit')