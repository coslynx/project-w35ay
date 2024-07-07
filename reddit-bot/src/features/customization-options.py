import praw

class CustomizationOptions:
    def __init__(self, reddit_client):
        self.reddit = reddit_client

    def personalize_settings(self, subreddit, post_format, title, image):
        # Logic to personalize bot settings for specific subreddit requirements
        pass

    def choose_post_format(self, post_format):
        # Logic to choose post formats for each submission
        pass

    def set_post_title(self, title):
        # Logic to set post titles for each submission
        pass

    def set_post_image(self, image):
        # Logic to set images for each submission
        pass

# Instantiate Reddit client
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')

# Instantiate CustomizationOptions object
customization_options = CustomizationOptions(reddit)