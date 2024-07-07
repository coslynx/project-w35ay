import pandas as pd
import schedule
import time

class ScheduledPosting:
    def __init__(self):
        self.posts = pd.DataFrame(columns=['post_id', 'title', 'content', 'scheduled_time', 'subreddit'])

    def schedule_post(self, post_id, title, content, scheduled_time, subreddit):
        new_post = {'post_id': post_id, 'title': title, 'content': content, 'scheduled_time': scheduled_time, 'subreddit': subreddit}
        self.posts = self.posts.append(new_post, ignore_index=True)

    def post_at_scheduled_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        for index, row in self.posts.iterrows():
            if row['scheduled_time'] == current_time:
                self.post_to_reddit(row['title'], row['content'], row['subreddit'])
                self.posts = self.posts.drop(index)
    
    def post_to_reddit(self, title, content, subreddit):
        # Code to post content to Reddit goes here
        pass

    def start_scheduler(self):
        schedule.every(10).seconds.do(self.post_at_scheduled_time)
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    scheduled_posting = ScheduledPosting()
    scheduled_posting.schedule_post("123", "Sample Post", "This is a sample post content.", "2022-12-31 23:59:59", "r/example")
    scheduled_posting.start_scheduler()